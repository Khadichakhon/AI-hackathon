"""
Run all tasks: generate predictions, verify submission, create demo
"""
import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and show output"""
    print(f"\n{'='*60}")
    print(f"Running: {cmd}")
    print('='*60)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("="*60)
    print("Mizzou AGI Hackathon 2025 - Complete Pipeline")
    print("="*60)
    
    # Step 1: Generate predictions
    print("\n[Step 1/4] Generating predictions for all curve-ball tasks...")
    success = run_command(f'{sys.executable} generate_predictions.py')
    if not success:
        print("⚠ Warning: Prediction generation had issues")
    
    # Step 2: Verify submission
    print("\n[Step 2/4] Verifying submission format...")
    success = run_command(f'{sys.executable} verify_submission.py')
    if not success:
        print("⚠ Warning: Submission verification had issues")
    
    # Step 3: Evaluate format (without ground truth)
    print("\n[Step 3/4] Evaluating curve-ball set format...")
    success = run_command(f'{sys.executable} evaluation_metrics.py')
    if not success:
        print("⚠ Warning: Evaluation had issues")
    
    print("\n[Step 4/4] Complete!")
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("1. Review generated predictions in *_guess.json files")
    print("2. Submit predictions via Google Form:")
    print("   https://forms.gle/LdGDR8RGqjP4re5U9")
    print("3. Create video demo: python video_demo.py")
    print("4. After submission, download ground truth and evaluate metrics")
    print("="*60)

if __name__ == "__main__":
    main()

