"""
Video Demo Script for 30-Second ARC Solver Demonstration
Shows: 1) Startup 2) Intermediate Process 3) Final Output
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import time
from solver import AdvancedARCSolver


def record_video_demo(task_file='example01.json', output_prefix='demo'):
    """
    Enhanced demo function for 30-second video recording.
    Shows: 1) Startup 2) Intermediate process 3) Final output
    
    Args:
        task_file: Path to the first curve-ball task JSON file
        output_prefix: Prefix for saved images
    """
    print("="*60)
    print("ARC SOLVER AUTONOMOUS DEMO")
    print("="*60)
    
    # 1. STARTUP (3-5 seconds)
    print("\n[1/4] STARTUP - Launching solver...")
    solver = AdvancedARCSolver()
    print("✓ Solver initialized")
    
    # Load first curve-ball task
    print(f"[1/4] Loading curve-ball task: {task_file}")
    with open(task_file, 'r') as f:
        task_data = json.load(f)
    print(f"✓ Loaded task with {len(task_data['train'])} training examples")
    
    # 2. INTERMEDIATE PROCESS (10-15 seconds)
    print("\n[2/4] INTERMEDIATE PROCESS - Analyzing patterns...")
    
    # Show first training example
    input_grid1 = np.array(task_data['train'][0]['input'])
    output_grid1 = np.array(task_data['train'][0]['output'])
    
    fig1, axes1 = plt.subplots(1, 2, figsize=(10, 5))
    axes1[0].imshow(input_grid1, cmap='viridis', interpolation='nearest')
    axes1[0].set_title('Training Input 1', fontsize=14, fontweight='bold')
    axes1[0].axis('off')
    
    axes1[1].imshow(output_grid1, cmap='viridis', interpolation='nearest')
    axes1[1].set_title('Training Output 1', fontsize=14, fontweight='bold')
    axes1[1].axis('off')
    
    plt.suptitle('Pattern Analysis - Training Example', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_step1_training.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"  → Analyzed training example 1")
    print(f"    Input shape: {input_grid1.shape}, Output shape: {output_grid1.shape}")
    
    # Show second training example if available
    if len(task_data['train']) > 1:
        input_grid2 = np.array(task_data['train'][1]['input'])
        output_grid2 = np.array(task_data['train'][1]['output'])
        print(f"  → Analyzed training example 2")
        print(f"    Input shape: {input_grid2.shape}, Output shape: {output_grid2.shape}")
    
    # 3. PROCESSING TEST INPUT (5-8 seconds)
    print("\n[3/4] PROCESSING - Applying pattern to test input...")
    test_input = np.array(task_data['test'][0]['input'])
    
    fig2, ax2 = plt.subplots(1, 1, figsize=(6, 6))
    ax2.imshow(test_input, cmap='viridis', interpolation='nearest')
    ax2.set_title('Test Input', fontsize=14, fontweight='bold')
    ax2.axis('off')
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_step2_test.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"  → Test input shape: {test_input.shape}")
    
    # Generate prediction
    print("  → Applying learned pattern...")
    predicted_output = solver.solve_task(task_data['train'], task_data['test'][0]['input'])
    predicted_arr = np.array(predicted_output)
    
    # 4. FINAL OUTPUT (5-7 seconds)
    print("\n[4/4] FINAL OUTPUT - Generated solution:")
    
    fig3, ax3 = plt.subplots(1, 1, figsize=(6, 6))
    ax3.imshow(predicted_arr, cmap='viridis', interpolation='nearest')
    ax3.set_title('Predicted Output', fontsize=14, fontweight='bold')
    ax3.axis('off')
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_step3_output.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    # Create side-by-side comparison
    fig4, axes4 = plt.subplots(1, 3, figsize=(15, 5))
    
    axes4[0].imshow(input_grid1, cmap='viridis', interpolation='nearest')
    axes4[0].set_title('Training Input', fontsize=12)
    axes4[0].axis('off')
    
    axes4[1].imshow(test_input, cmap='viridis', interpolation='nearest')
    axes4[1].set_title('Test Input', fontsize=12)
    axes4[1].axis('off')
    
    axes4[2].imshow(predicted_arr, cmap='viridis', interpolation='nearest')
    axes4[2].set_title('Predicted Output', fontsize=12)
    axes4[2].axis('off')
    
    plt.suptitle('ARC Solver Demo - Complete Pipeline', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{output_prefix}_complete.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("\n" + "="*60)
    print("✓ DEMO COMPLETE")
    print(f"Task: {task_file}")
    print(f"Training examples analyzed: {len(task_data['train'])}")
    print(f"Output shape: {predicted_arr.shape}")
    print(f"Images saved with prefix: {output_prefix}_")
    print("="*60)
    
    return predicted_output


if __name__ == "__main__":
    # Run demo on first curve-ball task
    record_video_demo('example01.json', 'demo')

