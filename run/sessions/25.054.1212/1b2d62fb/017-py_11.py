import numpy as np
from collections import Counter

def analyze_grid(grid, grid_name):
    """Analyzes a single grid and provides metrics."""
    print(f"Analysis of {grid_name}:")
    print(f"  Dimensions: {grid.shape}")
    unique, counts = np.unique(grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    print(f"  Color Counts: {color_counts}")
    print("----")

# Provided Example Data
example_inputs = [
    np.array([[0, 9, 9, 8, 9, 9, 9],
              [0, 0, 9, 8, 9, 9, 0],
              [9, 0, 9, 8, 9, 9, 0],
              [0, 0, 0, 8, 9, 0, 0],
              [0, 9, 9, 8, 9, 9, 9]]),
    np.array([[0, 0, 0, 8, 9, 0, 0],
              [9, 0, 9, 8, 9, 9, 9],
              [0, 9, 9, 8, 9, 9, 9],
              [0, 0, 0, 8, 9, 9, 9],
              [0, 9, 9, 8, 9, 9, 9]]),
    np.array([[9, 0, 0, 8, 9, 0, 9],
              [9, 0, 0, 8, 0, 9, 0],
              [9, 0, 0, 8, 9, 0, 0],
              [0, 9, 9, 8, 0, 9, 9],
              [0, 0, 9, 8, 0, 9, 0]]),
    np.array([[0, 9, 9, 8, 9, 0, 9],
              [9, 0, 0, 8, 9, 0, 0],
              [9, 9, 9, 8, 9, 9, 9],
              [0, 9, 0, 8, 0, 0, 0],
              [9, 0, 0, 8, 9, 0, 0]]),
    np.array([[0, 9, 9, 8, 9, 0, 9],
              [9, 0, 9, 8, 9, 9, 9],
              [9, 9, 9, 8, 0, 0, 9],
              [9, 0, 0, 8, 9, 0, 0],
              [9, 9, 9, 8, 0, 0, 9]])
]
example_outputs = [
    np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 8, 8],
              [0, 0, 0]]),
    np.array([[0, 8, 8],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]),
    np.array([[0, 8, 0],
              [0, 0, 8],
              [0, 8, 8],
              [8, 0, 0],
              [8, 0, 0]]),
    np.array([[0, 0, 0],
              [0, 8, 8],
              [0, 0, 0],
              [8, 0, 8],
              [0, 8, 8]]),
    np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 8, 8],
              [0, 0, 0]])
]

# Analyze each input and output
for i, (inp, out) in enumerate(zip(example_inputs, example_outputs)):
    analyze_grid(inp, f"Input Example {i+1}")
    analyze_grid(out, f"Output Example {i+1}")
