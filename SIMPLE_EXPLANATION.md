# Simple Explanation - What We're Doing

## What is ARC?

**ARC = Abstraction and Reasoning Corpus**

Think of it like this:
- You see a pattern (training examples)
- The pattern shows: "if input looks like THIS, output should be THAT"
- You need to figure out the rule/pattern
- Then apply that rule to a new test input

**Example:**
- Training: Shows 3 examples where triangles are flipped upside down
- Pattern: "Flip triangles vertically"
- Test: New triangle → Apply flip → Get answer

## What is the Hackathon Goal?

1. **Build a solver** that can figure out patterns automatically ✅ DONE
2. **Test it** on 11 secret tasks (curve-ball set) ✅ DONE (predictions made)
3. **Submit predictions** via Google Form ⏳ DO THIS NOW
4. **Report metrics** in 5-minute presentation ⏳ NEED TO DO

## What Do Those Files Mean?

### Input Files (example01.json - example11.json)
- **11 puzzles/tasks** given to you
- Each has training examples (showing patterns)
- Each has a test input (what you need to solve)

### Your Predictions (*_guess.json files)
- **Your solver's answers** to those 11 test inputs
- These are what you SUBMIT to the competition

### Verification Output
- Checks your files are formatted correctly ✅
- Says "SUBMISSION IS READY!" = You can submit ✅

### Demo Output
- Creates images showing your solver working
- For your 30-second video demonstration

## What Are Performance Metrics?

Two numbers you need to report:

### 1. Task-Level Accuracy
- **Meaning:** How many tasks did you solve completely correctly?
- **Format:** `X / 11 = Y%` (for curve-ball set)
- **Example:** If you got 3 out of 11 right = `3 / 11 = 27.3%`

### 2. Pixel Correctness  
- **Meaning:** What percentage of pixels were correct (even if task was wrong)?
- **Format:** `Z%`
- **Example:** `65.4%` means 65% of all pixels were correct

## How to See Your Performance?

Run this command:
```bash
python check_performance.py
```

This will test your solver on the **training examples** (what we can verify).

**Note:** 
- We can't see test set performance until after submission (organizers have answers)
- But we can see how well it learns patterns from training data

## What You Need to Do NOW

1. ✅ **Predictions are made** (11 *_guess.json files)
2. ✅ **Files are verified** (format is correct)
3. ⏳ **SUBMIT via Google Form:** https://forms.gle/LdGDR8RGqjP4re5U9
4. ⏳ **Check performance** (run check_performance.py to see training accuracy)

## Simple Checklist

- [x] Solver built
- [x] Predictions generated  
- [x] Files verified
- [ ] **Submit predictions** ← DO THIS
- [ ] Check training performance ← RUN check_performance.py
- [ ] Download public evaluation set (for presentation metrics)
- [ ] Create video demo

