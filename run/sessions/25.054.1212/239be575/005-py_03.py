import numpy as np

# Input grids for all examples
input_grids = [
    np.array([[0, 0, 8, 0, 8],
              [2, 2, 8, 0, 0],
              [2, 2, 0, 0, 8],
              [0, 0, 0, 2, 2],
              [8, 8, 0, 2, 2]]),
    np.array([[0, 8, 0, 0, 0, 0, 0],
              [2, 2, 0, 8, 8, 8, 0],
              [2, 2, 8, 8, 0, 2, 2],
              [0, 0, 8, 0, 0, 2, 2],
              [0, 8, 0, 0, 8, 0, 0]]),
    np.array([[8, 2, 2, 8, 8, 0, 0],
              [0, 2, 2, 0, 0, 0, 8],
              [0, 8, 8, 0, 0, 8, 0],
              [0, 0, 8, 0, 0, 0, 8],
              [8, 0, 8, 8, 8, 2, 2],
              [8, 0, 0, 0, 0, 2, 2]]),
    np.array([[8, 8, 0, 0, 2, 2, 0],
              [0, 8, 8, 0, 2, 2, 8],
              [0, 0, 0, 8, 0, 8, 0],
              [8, 0, 0, 0, 0, 0, 0],
              [0, 2, 2, 0, 8, 0, 8],
              [0, 2, 2, 8, 8, 0, 8]]),
    np.array([[8, 0, 0, 0, 0, 8, 0],
              [0, 0, 2, 2, 0, 8, 0],
              [8, 0, 2, 2, 0, 0, 0],
              [0, 0, 8, 0, 0, 8, 0],
              [0, 0, 8, 2, 2, 0, 8],
              [8, 0, 0, 2, 2, 8, 0]]),
    np.array([[8, 0, 0, 2, 2, 8],
              [8, 0, 8, 2, 2, 0],
              [0, 0, 0, 0, 8, 0],
              [2, 2, 8, 0, 8, 0],
              [2, 2, 0, 0, 0, 8],
              [0, 8, 8, 0, 8, 0]]),
]

# Count azure pixels for each input
azure_counts = [np.count_nonzero(grid == 8) for grid in input_grids]

# Output the counts along with the expected output
for i, count in enumerate(azure_counts):
    expected = 8 if i in [1, 2, 4] else 0  # Expected outputs based on problem description
    print(f"Example {i+1}: Azure Count = {count}, Expected Output = {expected}")