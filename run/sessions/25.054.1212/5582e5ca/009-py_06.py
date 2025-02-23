import numpy as np
from collections import Counter

def analyze_grid(grid, grid_name):
    """Analyzes a single grid and provides relevant metrics."""
    grid_array = np.array(grid)
    unique_values = np.unique(grid_array)
    value_counts = Counter(grid_array.flatten())
    dimensions = grid_array.shape
    print(f"Analysis of {grid_name}:")
    print(f"  Dimensions: {dimensions}")
    print(f"  Unique Values: {unique_values}")
    print(f"  Value Counts: {value_counts}")
    

# Example Data (from the prompt)
example1_input = [[4, 4, 8], [6, 4, 3], [6, 3, 0]]
example1_expected_output = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
example1_transformed_output = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

example2_input = [[6, 8, 9], [1, 8, 1], [9, 4, 9]]
example2_expected_output = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
example2_transformed_output = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

example3_input = [[4, 6, 9], [6, 4, 1], [8, 8, 6]]
example3_expected_output = [[6, 6, 6], [6, 6, 6], [6, 6, 6]]
example3_transformed_output = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

# Analyze each grid
analyze_grid(example1_input, "Example 1 Input")
analyze_grid(example1_expected_output, "Example 1 Expected Output")
analyze_grid(example1_transformed_output, "Example 1 Transformed Output")

analyze_grid(example2_input, "Example 2 Input")
analyze_grid(example2_expected_output, "Example 2 Expected Output")
analyze_grid(example2_transformed_output, "Example 2 Transformed Output")

analyze_grid(example3_input, "Example 3 Input")
analyze_grid(example3_expected_output, "Example 3 Expected Output")
analyze_grid(example3_transformed_output, "Example 3 Transformed Output")
