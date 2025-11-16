"""
Generate PNG images from ARC JSON task files
Creates colored grid visualizations for all inputs and outputs
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from pathlib import Path

# ARC color palette (0 = black, 1-9 = distinct colors)
ARC_COLORS = {
    0: '#000000',  # Black (background)
    1: '#0074D9',  # Blue
    2: '#FF4136',  # Red
    3: '#2ECC40',  # Green
    4: '#FFDC00',  # Yellow
    5: '#AAAAAA',  # Grey
    6: '#F012BE',  # Fuchsia
    7: '#FF851B',  # Orange
    8: '#7FDBFF',  # Aqua
    9: '#870C25',  # Maroon
}

def create_colormap():
    """Create a custom colormap for ARC colors"""
    colors = [ARC_COLORS[i] if i in ARC_COLORS else '#000000' for i in range(10)]
    cmap = mcolors.ListedColormap(colors)
    bounds = list(range(11))
    norm = mcolors.BoundaryNorm(bounds, cmap.N)
    return cmap, norm

def grid_to_image(grid, cmap, norm, title=''):
    """Convert a 2D grid to a matplotlib image"""
    arr = np.array(grid)
    h, w = arr.shape
    
    fig, ax = plt.subplots(figsize=(max(w/2, 4), max(h/2, 4)), dpi=100)
    im = ax.imshow(arr, cmap=cmap, norm=norm, interpolation='nearest')
    
    # Add grid lines for clarity
    ax.set_xticks(np.arange(-0.5, w, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, h, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Remove axis labels
    ax.set_xticks([])
    ax.set_yticks([])
    
    if title:
        ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
    
    plt.tight_layout()
    return fig

def generate_images_for_task(task_num, output_dir='example_inputs', examples_dir='examples'):
    """Generate PNG images for a single task"""
    filename = os.path.join(examples_dir, f"example{task_num:02d}.json")
    
    if not os.path.exists(filename):
        print(f"✗ File not found: {filename}")
        return False
    
    try:
        # Load task data
        with open(filename, 'r') as f:
            task_data = json.load(f)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Create colormap
        cmap, norm = create_colormap()
        
        # Generate single comprehensive image for all training examples
        train_examples = task_data.get('train', [])
        if train_examples:
            num_train = len(train_examples)
            # Each training example gets 2 subplots (input + output), arranged in 2 rows
            cols = num_train
            rows = 2  # Input row and Output row
            
            # Create figure with appropriate size
            fig_width = max(cols * 2.5, 8)
            fig_height = max(rows * 3, 6)
            fig, axes = plt.subplots(rows, cols, figsize=(fig_width, fig_height), dpi=100)
            
            # Handle single example case
            if num_train == 1:
                axes = axes.reshape(2, 1)
            
            # Top row: Inputs, Bottom row: Outputs
            for i, example in enumerate(train_examples):
                # Input (top row)
                ax = axes[0, i] if num_train > 1 else axes[0, 0]
                input_arr = np.array(example['input'])
                ax.imshow(input_arr, cmap=cmap, norm=norm, interpolation='nearest')
                ax.set_title(f'Input {i+1}', fontsize=10, fontweight='bold', pad=8)
                ax.set_xticks([])
                ax.set_yticks([])
                
                # Add grid lines
                h, w = input_arr.shape
                ax.set_xticks(np.arange(-0.5, w, 1), minor=True)
                ax.set_yticks(np.arange(-0.5, h, 1), minor=True)
                ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.3, alpha=0.3)
                
                # Output (bottom row)
                ax = axes[1, i] if num_train > 1 else axes[1, 0]
                output_arr = np.array(example['output'])
                ax.imshow(output_arr, cmap=cmap, norm=norm, interpolation='nearest')
                ax.set_title(f'Output {i+1}', fontsize=10, fontweight='bold', pad=8)
                ax.set_xticks([])
                ax.set_yticks([])
                
                # Add grid lines
                h, w = output_arr.shape
                ax.set_xticks(np.arange(-0.5, w, 1), minor=True)
                ax.set_yticks(np.arange(-0.5, h, 1), minor=True)
                ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.3, alpha=0.3)
            
            # Main title
            plt.suptitle(f'Task {task_num:02d} - All Training Examples', 
                        fontsize=14, fontweight='bold', y=0.995)
            plt.tight_layout(rect=[0, 0, 1, 0.97])
            
            # Save single image per task
            output_path = Path(output_dir) / f"example{task_num:02d}.png"
            fig.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close(fig)
        
        print(f"  ✓ Generated images for Task {task_num:02d}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {filename}: {e}")
        import traceback
        traceback.print_exc()
        return False

def generate_all_images(examples_dir='examples', output_dir='example_inputs'):
    """Generate PNG images for all 11 tasks"""
    print("="*70)
    print("GENERATING PNG IMAGES FROM ARC JSON FILES")
    print("="*70)
    
    os.makedirs(output_dir, exist_ok=True)
    
    success_count = 0
    
    for i in range(1, 12):
        print(f"\n[{i}/11] Processing Task {i:02d}...")
        if generate_images_for_task(i, output_dir, examples_dir):
            success_count += 1
    
    print("\n" + "="*70)
    print(f"✓ IMAGE GENERATION COMPLETE!")
    print(f"Successfully created images for {success_count}/11 tasks")
    print(f"Images saved to: {output_dir}/")
    print("="*70)
    
    # Print generated files
    print("\nGenerated files:")
    for i in range(1, 12):
        output_file = Path(output_dir) / f"example{i:02d}.png"
        if output_file.exists():
            print(f"  ✓ example{i:02d}.png")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    generate_all_images()

