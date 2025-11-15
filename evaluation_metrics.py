"""
Evaluation Metrics for ARC Tasks
Calculates task-level accuracy and pixel correctness
"""
import json
import numpy as np
import os


def calculate_task_level_accuracy(predictions_dict, ground_truth_dict):
    """
    Calculate Correct/Incorrect task-level accuracy.
    
    Args:
        predictions_dict: Dict of {task_id: {'train': [...], 'test': [{'input': [...], 'output': [...]}]}}
        ground_truth_dict: Same format as predictions
    
    Returns:
        tuple: (correct_count, total_count, percentage)
    """
    correct = 0
    total = 0
    
    for task_id in ground_truth_dict:
        if task_id not in predictions_dict:
            print(f"Warning: Missing prediction for {task_id}")
            total += 1
            continue
        
        pred_data = predictions_dict[task_id]
        true_data = ground_truth_dict[task_id]
        
        # Check if test arrays exist
        if 'test' not in pred_data or len(pred_data['test']) == 0:
            print(f"Warning: No test predictions for {task_id}")
            total += 1
            continue
        
        if 'test' not in true_data or len(true_data['test']) == 0:
            print(f"Warning: No ground truth for {task_id}")
            total += 1
            continue
        
        pred_output = np.array(pred_data['test'][0]['output'])
        true_output = np.array(true_data['test'][0]['output'])
        
        # Exact match check (all pixels, colors, and positions must match)
        if np.array_equal(pred_output, true_output):
            correct += 1
        else:
            print(f"Task {task_id} incorrect")
        
        total += 1
    
    percentage = (correct / total * 100) if total > 0 else 0
    return correct, total, percentage


def calculate_pixel_correctness(predictions_dict, ground_truth_dict):
    """
    Calculate pixel-level accuracy across all grids.
    
    Args:
        predictions_dict: Dict of predictions
        ground_truth_dict: Dict of ground truth
    
    Returns:
        float: Average pixel accuracy percentage
    """
    all_pixel_accuracies = []
    
    for task_id in ground_truth_dict:
        if task_id not in predictions_dict:
            continue
        
        pred_data = predictions_dict[task_id]
        true_data = ground_truth_dict[task_id]
        
        if 'test' not in pred_data or len(pred_data['test']) == 0:
            continue
        if 'test' not in true_data or len(true_data['test']) == 0:
            continue
        
        pred_output = np.array(pred_data['test'][0]['output'])
        true_output = np.array(true_data['test'][0]['output'])
        
        # Handle dimension mismatches by cropping to common size
        min_h = min(pred_output.shape[0], true_output.shape[0])
        min_w = min(pred_output.shape[1], true_output.shape[1])
        
        pred_crop = pred_output[:min_h, :min_w]
        true_crop = true_output[:min_h, :min_w]
        
        # Calculate pixel accuracy for this task
        correct_pixels = np.sum(pred_crop == true_crop)
        total_pixels = min_h * min_w
        
        if total_pixels > 0:
            task_pixel_acc = (correct_pixels / total_pixels) * 100
            all_pixel_accuracies.append(task_pixel_acc)
    
    # Average across all tasks
    avg_pixel_accuracy = np.mean(all_pixel_accuracies) if all_pixel_accuracies else 0
    return avg_pixel_accuracy


def load_predictions_from_files(directory=".", prefix="", suffix="_guess.json"):
    """Load all prediction files from directory"""
    predictions = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(suffix) and filename.startswith(prefix):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    predictions[filename] = json.load(f)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    return predictions


def load_ground_truth_from_files(directory=".", prefix="", suffix=".json", exclude_guess=True):
    """Load all ground truth files from directory"""
    ground_truth = {}
    
    for filename in os.listdir(directory):
        if filename.endswith(suffix) and filename.startswith(prefix):
            if exclude_guess and "_guess" in filename:
                continue
            
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    ground_truth[filename] = json.load(f)
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    return ground_truth


def evaluate_curve_ball_set():
    """
    Evaluate the curve-ball dataset (example01-11)
    This evaluates predictions against themselves for format checking.
    You'll need ground truth from results page to get real accuracy.
    """
    print("="*60)
    print("CURVE-BALL DATASET EVALUATION")
    print("="*60)
    
    # Load predictions
    predictions = load_predictions_from_files(prefix="example", suffix="_guess.json")
    print(f"\nLoaded {len(predictions)} prediction files")
    
    # Verify format
    print("\nVerifying submission format...")
    format_errors = []
    for filename, data in predictions.items():
        if 'train' not in data:
            format_errors.append(f"{filename}: missing 'train' key")
        elif 'test' not in data:
            format_errors.append(f"{filename}: missing 'test' key")
        elif len(data['test']) == 0:
            format_errors.append(f"{filename}: empty 'test' array")
        elif 'output' not in data['test'][0]:
            format_errors.append(f"{filename}: missing 'output' in test[0]")
        else:
            output_shape = np.array(data['test'][0]['output']).shape
            print(f"  ✓ {filename} - Output shape: {output_shape}")
    
    if format_errors:
        print("\n✗ Format errors found:")
        for error in format_errors:
            print(f"  ✗ {error}")
    else:
        print("\n✓ All files formatted correctly!")
    
    return predictions


def print_evaluation_results(correct, total, task_acc, pixel_acc):
    """Print formatted evaluation results"""
    print("\n" + "="*60)
    print("EVALUATION RESULTS")
    print("="*60)
    print(f"Task-Level Accuracy: {correct} / {total} = {task_acc:.2f}%")
    print(f"Pixel Correctness: {pixel_acc:.2f}%")
    print("="*60)


if __name__ == "__main__":
    # Evaluate curve-ball set format
    predictions = evaluate_curve_ball_set()
    
    print("\n" + "="*60)
    print("NOTE: To get actual accuracy metrics:")
    print("1. After submission, download ground truth from results page:")
    print("   https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home")
    print("2. Load both predictions and ground truth")
    print("3. Run calculate_task_level_accuracy() and calculate_pixel_correctness()")
    print("="*60)
    
    # Example usage (when you have ground truth):
    # ground_truth = load_ground_truth_from_files(prefix="example", suffix=".json")
    # correct, total, task_acc = calculate_task_level_accuracy(predictions, ground_truth)
    # pixel_acc = calculate_pixel_correctness(predictions, ground_truth)
    # print_evaluation_results(correct, total, task_acc, pixel_acc)

