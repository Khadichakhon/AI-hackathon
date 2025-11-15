# Action Checklist - What To Do Now

## ✅ Immediate Actions (Before Submission)

### 1. Generate Predictions for All 11 Tasks
```bash
python generate_predictions.py
```
**What this does:**
- Loads all 11 curve-ball tasks (example01.json - example11.json)
- Uses the advanced solver to generate predictions
- Saves predictions as `example01_guess.json` through `example11_guess.json`

**Expected output:** 11 `*_guess.json` files created

### 2. Verify Submission Format
```bash
python verify_submission.py
```
**What this does:**
- Checks all 11 prediction files are correctly formatted
- Verifies JSON structure is correct
- Ensures output format matches requirements

**Expected output:** "✓ SUBMISSION IS READY!" with all files valid

### 3. Check Your Predictions
```bash
# Quick check - see what files you have
python test_solver.py
```

## 📤 Submit (By Sunday 6:00 AM)

### 4. Submit Curve-Ball Predictions
1. Go to: **https://forms.gle/LdGDR8RGqjP4re5U9**
2. Upload all 11 `*_guess.json` files:
   - `example01_guess.json`
   - `example02_guess.json`
   - `example03_guess.json`
   - `example04_guess.json`
   - `example05_guess.json`
   - `example06_guess.json`
   - `example07_guess.json`
   - `example08_guess.json`
   - `example09_guess.json`
   - `example10_guess.json`
   - `example11_guess.json`
3. Submit before **Sunday 6:00 AM**

## 📊 For Your Presentation (Round 1 Judging)

### 5. Evaluate on Public Evaluation Set
1. **Download public evaluation set:**
   - Go to: **https://arcprize.org/guide**
   - Download the evaluation dataset

2. **Run solver on evaluation set:**
   - Create a script to run solver on all evaluation tasks
   - Use `solver.py` with your `AdvancedARCSolver`

3. **Calculate metrics:**
   ```python
   from evaluation_metrics import calculate_task_level_accuracy, calculate_pixel_correctness
   
   # Load your predictions and ground truth
   predictions = {...}  # Your predictions
   ground_truth = {...}  # Ground truth from evaluation set
   
   # Calculate metrics
   correct, total, task_acc = calculate_task_level_accuracy(predictions, ground_truth)
   pixel_acc = calculate_pixel_correctness(predictions, ground_truth)
   
   print(f"Task-Level Accuracy: {correct} / {total} = {task_acc:.2f}%")
   print(f"Pixel Correctness: {pixel_acc:.2f}%")
   ```

4. **Report in presentation:**
   - Task-Level Accuracy: `X / Y = Z%` (e.g., `23 / 120 = 19.2%`)
   - Pixel Correctness: `Z%` (e.g., `83.4%`)

### 6. Create 30-Second Video Demo
```bash
python video_demo.py
```
**What to record:**
1. **Startup (3-5 seconds):** Show launching solver/loading task
2. **Intermediate Process (10-15 seconds):** Show detected patterns, transformations
3. **Final Output (5-7 seconds):** Show generated output grid

**Video requirements:**
- Use first curve-ball task (`example01.json`)
- Must show autonomous operation (no manual tuning)
- Total length: up to 30 seconds
- Play during your 5-minute presentation

### 7. Check Curve-Ball Results (Sunday Morning)
1. After Sunday 9:00 AM, check results at:
   **https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home**

2. Download ground truth files

3. Calculate actual metrics using `evaluation_metrics.py`

## 🎯 Quick Command Summary

```bash
# 1. Generate predictions
python generate_predictions.py

# 2. Verify submission
python verify_submission.py

# 3. Test solver
python test_solver.py

# 4. Create video demo
python video_demo.py

# 5. Run complete pipeline (does steps 1-3)
python run_all.py
```

## ⚠️ Important Deadlines

- **Curve-Ball Submission:** Sunday 6:00 AM ⏰
- **Results Available:** Sunday morning before 9:00 AM
- **Presentation:** Round 1 Judging (check schedule)

## 📋 What You Need for Presentation

1. ✅ Task-Level Accuracy metric (from public evaluation set)
2. ✅ Pixel Correctness metric (from public evaluation set)
3. ✅ 30-second video demo (showing autonomous solver)
4. ✅ Curve-ball results (available Sunday morning)

## 🚀 Start Here

**Run these commands in order:**

```bash
# Step 1: Generate all predictions
python generate_predictions.py

# Step 2: Verify everything is correct
python verify_submission.py

# Step 3: If verification passes, submit via Google Form
# Then prepare your presentation materials
```

Good luck! 🏆

