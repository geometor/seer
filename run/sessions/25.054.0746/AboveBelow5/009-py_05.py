import numpy as np
from collections import Counter

def count_colors(grid):
    """Counts the occurrences of each color in the grid."""
    flattened = grid.flatten()
    return Counter(flattened)

# Example 1 Data
input_grid_1 = np.array([
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 3, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1]
])
expected_output_1 = np.array([
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 3, 0, 0, 0, 3, 0, 0, 0],
    [0, 3, 0, 0, 0, 3, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1]
])
transformed_output_1 = np.array([
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 3, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 3],
    [0, 3, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0, 1]
])

# Example 2 Data
input_grid_2 = np.array([
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 4, 0, 0, 0],
    [0, 4, 0, 4, 0, 4, 0, 0, 0],
    [0, 4, 0, 4, 0, 7, 0, 0, 4],
    [0, 4, 0, 4, 0, 4, 0, 0, 4]
])
expected_output_2 = np.array([
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 7, 0, 0, 0],
    [0, 4, 0, 4, 0, 7, 0, 0, 0],
    [0, 4, 0, 4, 0, 7, 0, 0, 4],
    [0, 4, 0, 4, 0, 4, 0, 0, 4]
])
transformed_output_2 = np.array([
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 0, 0, 0, 0],
    [0, 4, 0, 4, 0, 4, 0, 0, 0],
    [0, 4, 0, 4, 0, 4, 0, 0, 0],
    [0, 4, 0, 4, 0, 7, 0, 0, 4],
    [0, 4, 0, 4, 0, 4, 0, 0, 4]
])

print("Example 1 Color Counts:")
print("Input:", count_colors(input_grid_1))
print("Expected Output:", count_colors(expected_output_1))
print("Transformed Output:", count_colors(transformed_output_1))

print("\nExample 2 Color Counts:")
print("Input:", count_colors(input_grid_2))
print("Expected Output:", count_colors(expected_output_2))
print("Transformed Output:", count_colors(transformed_output_2))