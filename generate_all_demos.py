"""
Generate demo PNGs for all 11 curve-ball tasks
Creates visualizations showing training examples, test input, and predicted output
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import os
from solver import AdvancedARCSolver

def generate_demo_for_task(task_num):
    """Generate demo visualization for a single task"""
    filename = f"example{task_num:02d}.json"
    guess_filename = f"example{task_num:02d}_guess.json"
    
    if not os.path.exists(filename):
        print(f"✗ File not found: {filename}")
        return False
    
    try:
        # Load task data
        with open(filename, 'r') as f:
            task_data = json.load(f)
        
        # Load prediction
        with open(guess_filename, 'r') as f:
            prediction_data = json.load(f)
        
        solver = AdvancedARCSolver()
        
        # Prepare data
        train_examples = task_data['train']
        test_input = np.array(task_data['test'][0]['input'])
        predicted_output = np.array(prediction_data['test'][0]['output'])
        
        # Create figure with multiple subplots
        num_train = len(train_examples)
        fig = plt.figure(figsize=(15, 5))
        
        # Show first training example
        if num_train > 0:
            train_input1 = np.array(train_examples[0]['input'])
            train_output1 = np.array(train_examples[0]['output'])
            
            plt.subplot(2, 4, 1)
            plt.imshow(train_input1, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Input 1', fontsize=10, fontweight='bold')
            plt.axis('off')
            
            plt.subplot(2, 4, 2)
            plt.imshow(train_output1, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Output 1', fontsize=10, fontweight='bold')
            plt.axis('off')
        
        # Show second training example if available
        if num_train > 1:
            train_input2 = np.array(train_examples[1]['input'])
            train_output2 = np.array(train_examples[1]['output'])
            
            plt.subplot(2, 4, 3)
            plt.imshow(train_input2, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Input 2', fontsize=10, fontweight='bold')
            plt.axis('off')
            
            plt.subplot(2, 4, 4)
            plt.imshow(train_output2, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Output 2', fontsize=10, fontweight='bold')
            plt.axis('off')
        else:
            # Fill empty spaces
            plt.subplot(2, 4, 3)
            plt.axis('off')
            plt.subplot(2, 4, 4)
            plt.axis('off')
        
        # Show test input
        plt.subplot(2, 4, 5)
        plt.imshow(test_input, cmap='viridis', interpolation='nearest')
        plt.title(f'Task {task_num:02d} - Test Input', fontsize=10, fontweight='bold')
        plt.axis('off')
        
        # Show predicted output
        plt.subplot(2, 4, 6)
        plt.imshow(predicted_output, cmap='viridis', interpolation='nearest')
        plt.title(f'Task {task_num:02d} - Predicted Output', fontsize=10, fontweight='bold')
        plt.axis('off')
        
        # Show additional training example if available
        if num_train > 2:
            train_input3 = np.array(train_examples[2]['input'])
            train_output3 = np.array(train_examples[2]['output'])
            
            plt.subplot(2, 4, 7)
            plt.imshow(train_input3, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Input 3', fontsize=10, fontweight='bold')
            plt.axis('off')
            
            plt.subplot(2, 4, 8)
            plt.imshow(train_output3, cmap='viridis', interpolation='nearest')
            plt.title(f'Task {task_num:02d} - Training Output 3', fontsize=10, fontweight='bold')
            plt.axis('off')
        else:
            # Fill empty spaces
            plt.subplot(2, 4, 7)
            plt.axis('off')
            plt.subplot(2, 4, 8)
            plt.axis('off')
        
        plt.suptitle(f'ARC Solver Demo - Task {task_num:02d} ({filename})', 
                     fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        
        # Save the figure
        output_filename = f"demo_task{task_num:02d}_complete.png"
        plt.savefig(output_filename, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"  ✓ Created: {output_filename}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {filename}: {e}")
        return False

def generate_all_demos():
    """Generate demo visualizations for all 11 tasks"""
    print("="*70)
    print("GENERATING DEMO PNGs FOR ALL 11 CURVE-BALL TASKS")
    print("="*70)
    
    solver = AdvancedARCSolver()
    success_count = 0
    
    for i in range(1, 12):
        print(f"\n[{i}/11] Processing Task {i:02d}...")
        if generate_demo_for_task(i):
            success_count += 1
    
    print("\n" + "="*70)
    print(f"✓ DEMO GENERATION COMPLETE!")
    print(f"Successfully created {success_count}/11 demo images")
    print("="*70)
    print("\nGenerated files:")
    for i in range(1, 12):
        filename = f"demo_task{i:02d}_complete.png"
        if os.path.exists(filename):
            print(f"  ✓ {filename}")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    generate_all_demos()

