import numpy as np
from collections import Counter

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    background_color = Counter(input_grid.flatten()).most_common(1)[0][0]
    distinct_colors = sorted(list(set(input_grid.flatten()) - {background_color}))
    num_distinct_colors = len(distinct_colors)
    
    # Count rows with distinct colors
    rows_with_distinct_colors = 0
    for row in input_grid:
        if any(pixel != background_color for pixel in row):
            rows_with_distinct_colors += 1

    # Count columns with distinct colors (this definition might be refined)
    cols_with_distinct_colors = 0
    for j in range(input_grid.shape[1]):
      if any(pixel != background_color for pixel in input_grid[:,j]):
        cols_with_distinct_colors += 1
            
    print("--- Example Analysis ---")
    print(f"Background Color: {background_color}")
    print(f"Distinct Colors: {distinct_colors}")
    print(f"Number of Distinct Colors: {num_distinct_colors}")
    print(f"Rows with Distinct Colors: {rows_with_distinct_colors}")
    print(f"Cols with Distinct Colors: {cols_with_distinct_colors}")
    print(f"Expected Output Shape: {expected_output.shape}")
    print(f"Transformed Output Shape: {transformed_output.shape}")
    print(f"Colors in Expected Output: {set(expected_output.flatten())}")
    print(f"Colors in Transformed Output: {set(transformed_output.flatten())}")


# Example Data (replace with your actual example data)
example1_input = [[1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 1, 1, 1, 1], [1, 2, 2, 3, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
example1_expected = [[2, 2, 0], [2, 2, 3], [0, 0, 2]]
example1_transformed = [[2, 2], [3, 3], [0, 0]]

example2_input = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 3, 1, 2, 1, 1], [1, 1, 3, 1, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
example2_expected = [[3, 0, 2], [3, 0, 2]]
example2_transformed = [[3, 3], [2, 2]]

example3_input = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 5, 5, 1, 1, 1], [1, 5, 5, 1, 1, 1], [1, 6, 6, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
example3_expected = [[5, 5], [5, 5], [6, 6]]
example3_transformed = [[5, 5], [6, 6], [0, 0]]

analyze_example(example1_input, example1_expected, example1_transformed)
analyze_example(example2_input, example2_expected, example2_transformed)
analyze_example(example3_input, example3_expected, example3_transformed)