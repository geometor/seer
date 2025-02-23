import numpy as np

def describe_grid(grid):
    """Provides a textual description of a grid."""
    rows, cols = grid.shape
    description = f"Grid size: {rows}x{cols}\n"
    unique, counts = np.unique(grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    description += "Color counts: " + str(color_counts) + "\n"
    return description

# Example data (from the prompt)
inputs = [
    np.array([[0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 2, 2, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 4, 4, 0, 1, 1, 0],
              [0, 0, 0, 0, 4, 4, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 0, 0, 0, 4, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 4, 4, 4],
              [0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
              [0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 4, 0, 0, 0]])
]

expected_outputs = [
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 2, 2, 0, 4, 4, 0, 1, 1, 0],
              [0, 2, 2, 0, 4, 4, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 2, 2, 2, 1, 1, 1, 4, 4, 4],
              [0, 2, 2, 2, 1, 1, 1, 4, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 4, 0, 0, 0],
              [0, 1, 0, 2, 0, 0, 4, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
]

transformed_outputs = []
for inp in inputs:
  transformed_outputs.append(transform(inp))

for i, (inp, exp, trans) in enumerate(zip(inputs, expected_outputs, transformed_outputs)):
    print(f"Example {i+1}:")
    print("Input:")
    print(describe_grid(inp))
    print("Expected Output:")
    print(describe_grid(exp))
    print("Transformed Output:")
    print(describe_grid(trans))
    print("-" * 20)