# Mizzou AGI Hackathon 2025 - Complete Checklist

## ✅ What We've Built

### 1. Advanced ARC Solver (`solver.py`)
- Multi-strategy pattern detection
- Geometric transformations (flips, rotations, transpositions)
- Boundary/frame detection patterns
- Region filling patterns
- Object manipulation (tip detection)
- Color transformations
- Pattern-specific transformations

### 2. Prediction Generation (`generate_predictions.py`)
- Automatically generates predictions for all 11 curve-ball tasks
- Creates `*_guess.json` files in correct format

### 3. Submission Verification (`verify_submission.py`)
- Verifies all 11 prediction files are correctly formatted
- Checks JSON structure, output format, and shape consistency

### 4. Evaluation Metrics (`evaluation_metrics.py`)
- Calculates task-level accuracy (Correct/Incorrect)
- Calculates pixel correctness percentage
- Ready to use once ground truth is available

### 5. Video Demo (`video_demo.py`)
- Creates 30-second demonstration
- Shows: Startup → Intermediate Process → Final Output
- Generates visualization images

### 6. Complete Pipeline (`run_all.py`)
- Runs all steps in sequence
- Generates predictions → Verifies → Evaluates

## 📋 Action Checklist

### Before Submission (SUNDAY 6:00 AM)

- [ ] **Generate Predictions**
  ```bash
  python generate_predictions.py
  ```
  - This creates all 11 `*_guess.json` files

- [ ] **Verify Submission Format**
  ```bash
  python verify_submission.py
  ```
  - Ensure all files are correctly formatted
  - All 11 files should show ✓

- [ ] **Test on Example**
  ```bash
  python test_solver.py
  ```
  - Verify solver works correctly
  - Check predictions look reasonable

### Submission (SUNDAY 6:00 AM)

- [ ] **Submit Curve-Ball Predictions**
  - Go to: https://forms.gle/LdGDR8RGqjP4re5U9
  - Upload all 11 `*_guess.json` files:
    - `example01_guess.json`
    - `example02_guess.json`
    - ...
    - `example11_guess.json`
  - Submit before **Sunday 6:00 AM**

### For Presentation (Round 1 Judging)

- [ ] **Evaluate on Public Evaluation Set**
  - Download from: https://arcprize.org/guide
  - Run solver on evaluation set
  - Calculate metrics:
    ```python
    from evaluation_metrics import calculate_task_level_accuracy, calculate_pixel_correctness
    # Load predictions and ground truth
    correct, total, task_acc = calculate_task_level_accuracy(predictions, ground_truth)
    pixel_acc = calculate_pixel_correctness(predictions, ground_truth)
    ```
  - Report in presentation:
    - Task-Level Accuracy: `X / Y = Z%`
    - Pixel Correctness: `Z%`

- [ ] **Create Video Demo (30 seconds)**
  ```bash
  python video_demo.py
  ```
  - Record the output showing:
    1. **Startup**: How solver is launched
    2. **Intermediate Process**: Display detected patterns/transformations
    3. **Final Output**: Show generated output grid
  - Use first curve-ball task (`example01.json`)
  - Include in 5-minute presentation

- [ ] **Check Curve-Ball Results**
  - After Sunday 9:00 AM, check results at:
    https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home
  - Calculate actual accuracy metrics
  - Update presentation with actual results

## 📊 Expected Metrics Format

### In Your 5-Minute Presentation:

**1. Task-Level Accuracy**
- Format: `23 / 120 = 19.2%`
- Example: "Our solver correctly solved 23 out of 120 tasks, achieving 19.2% task-level accuracy."

**2. Pixel Correctness**
- Format: `83.4%`
- Example: "The solver achieved 83.4% pixel correctness across all test grids."

**3. Video Demonstration**
- 30-second video showing autonomous solver
- Must show: startup → intermediate → final output

## 🔧 Quick Commands

### Generate Everything:
```bash
python run_all.py
```

### Generate Predictions Only:
```bash
python generate_predictions.py
```

### Verify Submission:
```bash
python verify_submission.py
```

### Test Solver:
```bash
python test_solver.py
```

### Create Video Demo:
```bash
python video_demo.py
```

## 📁 File Structure

```
AI-hackathon/
├── solver.py                 # Advanced ARC solver
├── generate_predictions.py   # Generate all predictions
├── verify_submission.py      # Verify submission format
├── evaluation_metrics.py     # Calculate metrics
├── video_demo.py            # Create video demo
├── test_solver.py           # Test solver
├── run_all.py               # Complete pipeline
├── README.md                # Documentation
├── HACKATHON_CHECKLIST.md   # This file
├── example01.json - example11.json  # Curve-ball dataset
└── example01_guess.json - example11_guess.json  # Predictions
```

## ⚠️ Important Notes

1. **Deadline**: Curve-ball predictions must be submitted by **Sunday 6:00 AM**
2. **Format**: All `*_guess.json` files must be in correct JSON format
3. **Video**: 30-second demo is required for presentation
4. **Autonomous**: Solver must run autonomously without manual tuning
5. **Metrics**: Both task-level accuracy and pixel correctness must be reported

## 🎯 Winning Strategy

1. **Multiple Strategies**: Solver tries multiple pattern detection strategies
2. **Robust Detection**: Handles geometric transforms, region filling, object manipulation
3. **Format Verification**: Ensures all submissions are correctly formatted
4. **Complete Pipeline**: Automated generation and verification
5. **Demonstration**: Clear video showing autonomous operation

## 📞 Resources

- **ARC Prize Guide**: https://arcprize.org/guide
- **Curve-Ball Submission**: https://forms.gle/LdGDR8RGqjP4re5U9
- **Results Page**: https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home

---

## 🚀 Final Steps

1. Run `python generate_predictions.py` to generate all predictions
2. Run `python verify_submission.py` to verify format
3. Submit all 11 `*_guess.json` files via Google Form
4. Create video demo for presentation
5. Evaluate on public set and report metrics
6. Check results Sunday morning and update metrics

**GOOD LUCK! 🏆**

