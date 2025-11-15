# Mizzou AGI Hackathon 2025 - ARC Solver

## Overview
Advanced ARC (Abstraction and Reasoning Corpus) solver for the 2025 Mizzou AGI Hackathon. This solver implements multiple pattern detection strategies to solve ARC tasks autonomously.

## Files Structure

### Core Files
- **`solver.py`** - Advanced ARC solver with multiple pattern detection strategies:
  - Geometric transformations (flip, rotate, transpose)
  - Boundary/frame detection patterns
  - Region filling patterns
  - Object manipulation (tip detection, etc.)
  - Color transformations

- **`generate_predictions.py`** - Generate predictions for all 11 curve-ball tasks
- **`verify_submission.py`** - Verify submission format correctness
- **`evaluation_metrics.py`** - Calculate task-level accuracy and pixel correctness
- **`video_demo.py`** - Create 30-second demo video
- **`run_all.py`** - Run complete pipeline

### Data Files
- **`example01.json` - `example11.json`** - Curve-ball dataset (11 tasks)
- **`example01_guess.json` - `example11_guess.json`** - Generated predictions

## Quick Start

### 1. Generate Predictions
```bash
python generate_predictions.py
```
This generates predictions for all 11 curve-ball tasks and saves them as `*_guess.json` files.

### 2. Verify Submission Format
```bash
python verify_submission.py
```
This verifies all 11 prediction files are correctly formatted.

### 3. Run Complete Pipeline
```bash
python run_all.py
```
This runs all steps: generate predictions, verify format, and evaluate.

### 4. Create Video Demo
```bash
python video_demo.py
```
This creates the 30-second video demonstration showing the solver in action.

## Submission Instructions

### Curve-Ball Dataset Submission
1. Ensure all 11 `*_guess.json` files are generated and verified
2. Submit via Google Form: https://forms.gle/LdGDR8RGqjP4re5U9
3. Deadline: Sunday 6:00 AM

### Public Evaluation Set
1. Download public evaluation set from: https://arcprize.org/guide
2. Run solver on evaluation set
3. Calculate metrics using `evaluation_metrics.py`
4. Report metrics in 5-minute presentation

### Video Demonstration
1. Record 30-second video showing solver running autonomously
2. Video should include:
   - Startup: How solver is launched
   - Intermediate: Display detected patterns/transformations
   - Final: Show generated output grid
3. Use first curve-ball task (`example01.json`)
4. Play video during 5-minute presentation

## Evaluation Metrics

### Task-Level Accuracy
- Measures if predicted output exactly matches validated solution
- All pixels, colors, and positions must match exactly
- Format: `X / Y = Z%` (e.g., `23 / 120 = 19.2%`)

### Pixel Correctness
- Percentage of correctly predicted pixels across all test grids
- Average pixel accuracy across the dataset
- Format: `X%` (e.g., `83.4%`)

## Results

### Curve-Ball Dataset
- After submission deadline, results will be posted at:
  https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home
- Results available Sunday morning before 9 AM

## Solver Strategy

The solver implements a multi-strategy approach:

1. **Geometric Transformations** - Detects flips, rotations, transpositions
2. **Boundary Patterns** - Detects frame/rectangle drawing patterns
3. **Region Filling** - Detects color filling patterns (rows, columns, regions)
4. **Object Manipulation** - Detects tip detection and manipulation
5. **Color Transformations** - Detects color mapping patterns

The solver tries each strategy in order and uses the first one that matches the training pattern.

## Requirements

- Python 3.6+
- numpy
- scipy (optional, falls back to manual implementation if not available)
- matplotlib (for visualization and video demo)

## Notes

- The solver is designed to work autonomously without manual tuning
- All predictions are generated automatically from training examples
- Format verification ensures submission correctness
- Evaluation metrics can be calculated once ground truth is available

## Contact

For questions about the hackathon requirements:
- ARC Prize Guide: https://arcprize.org/guide
- Curve-Ball Submission: https://forms.gle/LdGDR8RGqjP4re5U9
- Results Page: https://sites.google.com/umsystem.edu/2025agihackathoncurveballdata/home

