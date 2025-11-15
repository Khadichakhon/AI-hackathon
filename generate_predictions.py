"""
Generate predictions for all curve-ball tasks using the advanced solver
"""
import json
import os
from solver import AdvancedARCSolver


def generate_all_predictions():
    """Generate predictions for all 11 curve-ball tasks"""
    print("="*60)
    print("GENERATING PREDICTIONS FOR ALL CURVE-BALL TASKS")
    print("="*60)
    
    solver = AdvancedARCSolver()
    predictions = {}
    
    for i in range(1, 12):
        filename = f"example{i:02d}.json"
        guess_filename = f"example{i:02d}_guess.json"
        
        if not os.path.exists(filename):
            print(f"✗ File not found: {filename}")
            continue
        
        try:
            # Load task
            with open(filename, 'r') as f:
                task_data = json.load(f)
            
            print(f"\n[{i}/11] Processing {filename}...")
            print(f"  Training examples: {len(task_data['train'])}")
            
            # Solve the task
            test_input = task_data['test'][0]['input']
            predicted_output = solver.solve_task(task_data['train'], test_input)
            
            # Store prediction
            prediction_data = {
                "train": task_data['train'],
                "test": [{"input": test_input, "output": predicted_output}]
            }
            
            # Save prediction
            with open(guess_filename, 'w') as f:
                json.dump(prediction_data, f, separators=(',', ':'))  # Compact format
            
            output_shape = (len(predicted_output), len(predicted_output[0]))
            print(f"  ✓ Generated prediction - Output shape: {output_shape}")
            print(f"  ✓ Saved to: {guess_filename}")
            
            predictions[guess_filename] = prediction_data
            
        except Exception as e:
            print(f"  ✗ Error processing {filename}: {e}")
            continue
    
    print("\n" + "="*60)
    print("PREDICTION GENERATION COMPLETE")
    print(f"Generated {len(predictions)} prediction files")
    print("="*60)
    
    return predictions


if __name__ == "__main__":
    generate_all_predictions()

