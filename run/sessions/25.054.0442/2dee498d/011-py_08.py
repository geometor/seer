import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    input_shape = input_grid.shape
    expected_shape = expected_output.shape
    transformed_shape = transformed_output.shape

    match = np.array_equal(expected_output, transformed_output)

    print(f"  Input Shape: {input_shape}")
    print(f"  Expected Shape: {expected_shape}")
    print(f"  Transformed Shape: {transformed_shape}")
    print(f"  Match: {match}")

    if not match:
      diff = expected_output.shape[1] - transformed_output.shape[1]
      print(f'Difference in Width {diff}')

# Example 1
print("Example 1:")
input1 = [[4, 5, 1, 1, 5, 4, 4, 5, 1], [5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 5, 4, 4, 5, 1, 1, 5, 4]]
expected1 = [[4, 5, 1], [5, 5, 5], [1, 5, 4]]
transformed1 = [[4, 5, 1, 1, 5, 4], [5, 5, 5, 5, 5, 5], [1, 5, 4, 4, 5, 1]]
analyze_example(input1, expected1, transformed1)

# Example 2
print("\nExample 2:")
input2 = [[2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1], [4, 2, 1, 4, 4, 2, 1, 4, 4, 2, 1, 4], [4, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4], [1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2]]
expected2 = [[2, 0, 0, 1], [4, 2, 1, 4], [4, 1, 2, 4], [1, 0, 0, 2]]
transformed2 = [[2, 0, 0, 1], [4, 2, 1, 4], [4, 1, 2, 4], [1, 0, 0, 2]]
analyze_example(input2, expected2, transformed2)

# Example 3
print("\nExample 3:")
input3 = [[2, 1, 2, 1, 2, 1], [2, 3, 2, 3, 2, 3]]
expected3 = [[2, 1], [2, 3]]
transformed3 = [[2, 1], [2, 3]]
analyze_example(input3, expected3, transformed3)
