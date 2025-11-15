"""
Test the solver and generate predictions
"""
import json
import numpy as np
import os
from solver import AdvancedARCSolver

# Test on example01
print("Testing solver on example01...")
with open('example01.json', 'r') as f:
    task_data = json.load(f)

solver = AdvancedARCSolver()

# Test on training examples first
print("\nTesting on training examples:")
for i, example in enumerate(task_data['train'][:3]):
    input_arr = np.array(example['input'])
    output_arr = np.array(example['output'])
    predicted = solver.solve_task([example], input_arr)
    
    is_correct = np.array_equal(np.array(predicted), output_arr)
    print(f"  Training example {i+1}: {'✓' if is_correct else '✗'} {'Correct' if is_correct else 'Incorrect'}")

# Test on actual test input
print("\nTesting on test input:")
test_input = np.array(task_data['test'][0]['input'])
predicted_output = solver.solve_task(task_data['train'], test_input)

print(f"  Input shape: {test_input.shape}")
print(f"  Output shape: {np.array(predicted_output).shape}")

# Compare with existing guess
with open('example01_guess.json', 'r') as f:
    existing_guess = json.load(f)

existing_output = np.array(existing_guess['test'][0]['output'])
predicted_arr = np.array(predicted_output)

if np.array_equal(predicted_arr, existing_output):
    print("  ✓ Matches existing guess")
else:
    print("  ⚠ Different from existing guess")
    print(f"    Existing shape: {existing_output.shape}")
    print(f"    New shape: {predicted_arr.shape}")

print("\nSolver test complete!")

