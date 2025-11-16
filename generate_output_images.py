"""
Generate PNG images from ARC prediction files
Creates visualizations showing test inputs and predicted outputs
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

def generate_output_images_for_task(task_num, output_dir='example_output_pngs', predictions_dir='example_outputs'):
    """Generate PNG images for a single task's output"""
    guess_filename = os.path.join(predictions_dir, f"example{task_num:02d}_guess.json")
    
    if not os.path.exists(guess_filename):
        print(f"✗ File not found: {guess_filename}")
        return False
    
    try:
        # Load prediction data
        with open(guess_filename, 'r') as f:
            prediction_data = json.load(f)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Create colormap
        cmap, norm = create_colormap()
        
        # Get test data
        test_examples = prediction_data.get('test', [])
        if not test_examples:
            print(f"  ✗ No test data in {guess_filename}")
            return False
        
        for i, test_example in enumerate(test_examples):
            test_input = test_example['input']
            predicted_output = test_example.get('output', [])
            
            if not predicted_output:
                print(f"  ✗ No output in test example {i+1}")
                continue
            
            # Create figure with input and output side by side
            input_arr = np.array(test_input)
            output_arr = np.array(predicted_output)
            
            fig, axes = plt.subplots(1, 2, figsize=(12, 6), dpi=150)
            
            # Input image (left)
            ax = axes[0]
            ax.imshow(input_arr, cmap=cmap, norm=norm, interpolation='nearest')
            ax.set_title(f'Task {task_num:02d} - Test Input', fontsize=12, fontweight='bold', pad=10)
            ax.set_xticks([])
            ax.set_yticks([])
            
            # Add grid lines
            h, w = input_arr.shape
            ax.set_xticks(np.arange(-0.5, w, 1), minor=True)
            ax.set_yticks(np.arange(-0.5, h, 1), minor=True)
            ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
            
            # Output image (right)
            ax = axes[1]
            ax.imshow(output_arr, cmap=cmap, norm=norm, interpolation='nearest')
            ax.set_title(f'Task {task_num:02d} - Predicted Output', fontsize=12, fontweight='bold', pad=10)
            ax.set_xticks([])
            ax.set_yticks([])
            
            # Add grid lines
            h, w = output_arr.shape
            ax.set_xticks(np.arange(-0.5, w, 1), minor=True)
            ax.set_yticks(np.arange(-0.5, h, 1), minor=True)
            ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
            
            # Main title
            plt.suptitle(f'ARC Solver - Task {task_num:02d} Prediction', 
                        fontsize=14, fontweight='bold', y=0.98)
            plt.tight_layout(rect=[0, 0, 1, 0.96])
            
            # Save image
            if i == 0:
                output_path = Path(output_dir) / f"example{task_num:02d}_output.png"
            else:
                output_path = Path(output_dir) / f"example{task_num:02d}_output_{i+1}.png"
            
            fig.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close(fig)
        
        print(f"  ✓ Generated output image for Task {task_num:02d}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {guess_filename}: {e}")
        import traceback
        traceback.print_exc()
        return False

def generate_all_output_images():
    """Generate PNG images for all predicted outputs"""
    print("="*70)
    print("GENERATING PNG IMAGES FROM ARC PREDICTIONS")
    print("="*70)
    
    output_dir = 'example_output_pngs'
    predictions_dir = 'example_outputs'
    os.makedirs(output_dir, exist_ok=True)
    
    success_count = 0
    
    for i in range(1, 12):
        print(f"\n[{i}/11] Processing Task {i:02d}...")
        if generate_output_images_for_task(i, output_dir, predictions_dir):
            success_count += 1
    
    print("\n" + "="*70)
    print(f"✓ IMAGE GENERATION COMPLETE!")
    print(f"Successfully created images for {success_count}/11 tasks")
    print(f"Images saved to: {output_dir}/")
    print("="*70)
    
    # Print generated files
    print("\nGenerated files:")
    for i in range(1, 12):
        output_file = Path(output_dir) / f"example{i:02d}_output.png"
        if output_file.exists():
            print(f"  ✓ {output_file.name}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    generate_all_output_images()

