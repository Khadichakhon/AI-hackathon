"""
Check Your Performance Metrics - Simple Explanation
"""
import json
import numpy as np
from solver import AdvancedARCSolver
from evaluation_metrics import calculate_task_level_accuracy, calculate_pixel_correctness

print("="*70)
print("YOUR PERFORMANCE METRICS - SIMPLE EXPLANATION")
print("="*70)

print("\n📊 WHAT ARE WE MEASURING?")
print("1. Task-Level Accuracy: How many tasks did you solve correctly?")
print("2. Pixel Correctness: What % of pixels were correct?")

print("\n" + "="*70)
print("TESTING ON TRAINING EXAMPLES (What We Can Verify)")
print("="*70)

solver = AdvancedARCSolver()
all_correct = 0
all_total = 0
all_pixel_accuracies = []

for i in range(1, 12):
    filename = f"example{i:02d}.json"
    try:
        with open(filename, 'r') as f:
            task_data = json.load(f)
        
        task_correct = 0
        task_total = len(task_data['train'])
        task_pixel_accs = []
        
        print(f"\n📁 Task {i:02d}: {task_total} training examples")
        
        # Test on each training example (using others to learn pattern)
        for j, example in enumerate(task_data['train']):
            input_arr = np.array(example['input'])
            output_arr = np.array(example['output'])
            
            # Use other examples to predict this one
            other_examples = [ex for k, ex in enumerate(task_data['train']) if k != j]
            if len(other_examples) == 0:
                other_examples = [example]
            
            predicted = solver.solve_task(other_examples, input_arr)
            predicted_arr = np.array(predicted)
            
            # Check if correct
            is_correct = np.array_equal(predicted_arr, output_arr)
            
            if is_correct:
                task_correct += 1
                all_correct += 1
                status = "✓ CORRECT"
            else:
                status = "✗ WRONG"
            
            # Pixel accuracy
            min_h = min(predicted_arr.shape[0], output_arr.shape[0])
            min_w = min(predicted_arr.shape[1], output_arr.shape[1])
            
            pred_crop = predicted_arr[:min_h, :min_w]
            true_crop = output_arr[:min_h, :min_w]
            
            correct_pixels = np.sum(pred_crop == true_crop)
            total_pixels = min_h * min_w
            
            if total_pixels > 0:
                pixel_acc = (correct_pixels / total_pixels) * 100
                task_pixel_accs.append(pixel_acc)
                all_pixel_accuracies.append(pixel_acc)
            
            print(f"   Example {j+1}: {status} ({pixel_acc:.1f}% pixels correct)")
        
        task_acc = (task_correct / task_total * 100) if task_total > 0 else 0
        task_pixel_acc = np.mean(task_pixel_accs) if task_pixel_accs else 0
        
        all_total += task_total
        
        print(f"   → Task {i:02d} Summary: {task_correct}/{task_total} correct ({task_acc:.1f}%)")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
        continue

# Overall results
print("\n" + "="*70)
print("YOUR OVERALL PERFORMANCE")
print("="*70)

overall_task_acc = (all_correct / all_total * 100) if all_total > 0 else 0
overall_pixel_acc = np.mean(all_pixel_accuracies) if all_pixel_accuracies else 0

print(f"\n✅ Task-Level Accuracy: {all_correct} / {all_total} = {overall_task_acc:.2f}%")
print(f"✅ Pixel Correctness: {overall_pixel_acc:.2f}%")

print("\n" + "="*70)
print("WHAT THIS MEANS:")
print("="*70)
print(f"- Your solver correctly solved {all_correct} out of {all_total} training examples")
print(f"- On average, {overall_pixel_acc:.1f}% of pixels were correct")
print("\nNOTE: This is on TRAINING examples (we can verify these).")
print("Test set results come from organizers after submission.")

print("\n" + "="*70)
print("NEXT STEPS:")
print("="*70)
print("1. ✅ Your predictions are ready (11 *_guess.json files)")
print("2. ⏳ SUBMIT via: https://forms.gle/LdGDR8RGqjP4re5U9")
print("3. ⏳ Check results Sunday morning after 9 AM")
print("="*70)

