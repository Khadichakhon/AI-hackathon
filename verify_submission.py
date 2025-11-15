"""
Verify Curve-Ball Submission Format
Ensures all 11 prediction files are correctly formatted
"""
import json
import os
import numpy as np


def verify_curve_ball_submission():
    """Verify all curve-ball submission files are properly formatted"""
    print("="*60)
    print("VERIFYING CURVE-BALL SUBMISSION")
    print("="*60)
    
    required_files = [f"example{i:02d}_guess.json" for i in range(1, 12)]
    missing_files = []
    invalid_files = []
    valid_files = []
    
    for filename in required_files:
        if not os.path.exists(filename):
            missing_files.append(filename)
            continue
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            errors = []
            
            # Check structure
            if 'train' not in data:
                errors.append("Missing 'train' key")
            
            if 'test' not in data:
                errors.append("Missing 'test' key")
            elif not isinstance(data['test'], list):
                errors.append("'test' is not a list")
            elif len(data['test']) == 0:
                errors.append("Empty 'test' array")
            elif 'input' not in data['test'][0]:
                errors.append("Missing 'input' in test[0]")
            elif 'output' not in data['test'][0]:
                errors.append("Missing 'output' in test[0]")
            else:
                # Check output is a 2D list
                output = data['test'][0]['output']
                if not isinstance(output, list):
                    errors.append("Output is not a list")
                elif len(output) == 0:
                    errors.append("Output is empty")
                elif not isinstance(output[0], list):
                    errors.append("Output is not a 2D list")
                else:
                    # Check output is rectangular
                    output_arr = np.array(output)
                    if output_arr.ndim != 2:
                        errors.append(f"Output is not 2D (shape: {output_arr.shape})")
            
            if errors:
                invalid_files.append((filename, errors))
            else:
                output_shape = np.array(data['test'][0]['output']).shape
                valid_files.append((filename, output_shape))
            
        except json.JSONDecodeError as e:
            invalid_files.append((filename, [f"Invalid JSON: {str(e)}"]))
        except Exception as e:
            invalid_files.append((filename, [f"Error: {str(e)}"]))
    
    # Print results
    print(f"\n✓ Valid files: {len(valid_files)}/{len(required_files)}")
    for filename, shape in valid_files:
        print(f"  ✓ {filename} - Output shape: {shape}")
    
    if missing_files:
        print(f"\n✗ Missing files: {len(missing_files)}")
        for f in missing_files:
            print(f"  ✗ {f}")
    
    if invalid_files:
        print(f"\n✗ Invalid files: {len(invalid_files)}")
        for filename, errors in invalid_files:
            print(f"  ✗ {filename}:")
            for error in errors:
                print(f"    - {error}")
    
    is_ready = len(valid_files) == len(required_files)
    
    print("\n" + "="*60)
    if is_ready:
        print("✓ SUBMISSION IS READY!")
        print(f"All {len(required_files)} files are properly formatted.")
        print("\nNext steps:")
        print("1. Submit all *_guess.json files via Google Form:")
        print("   https://forms.gle/LdGDR8RGqjP4re5U9")
        print("2. Submit by Sunday 6:00 AM")
    else:
        print("✗ SUBMISSION NEEDS FIXES")
        print(f"Fix the errors above before submitting.")
    print("="*60)
    
    return is_ready


if __name__ == "__main__":
    verify_curve_ball_submission()

