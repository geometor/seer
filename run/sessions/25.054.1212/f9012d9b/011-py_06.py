import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    metrics = {
        "input_shape": input_grid.shape,
        "output_shape": expected_output.shape,
        "transformed_shape": transformed_output.shape,
        "input_unique_colors": np.unique(input_grid).tolist(),
        "output_unique_colors": np.unique(expected_output).tolist(),
        "transformed_unique_colors": np.unique(transformed_output).tolist(),
        "match": np.array_equal(expected_output, transformed_output)
    }
    return metrics

# Example data (from the prompt)
example1_input = [[2, 1, 2, 1, 2], [1, 1, 1, 1, 1], [2, 1, 2, 1, 2], [0, 0, 1, 1, 1], [0, 0, 2, 1, 2]]
example1_expected = [[1, 1], [2, 1]]
example1_transformed = [[1], [2]]

example2_input = [[8, 6, 0, 6], [6, 8, 6, 8], [8, 6, 8, 6], [6, 8, 6, 8]]
example2_expected = [[8]]
example2_transformed = [[8]]

example3_input = [[2, 2, 5, 2, 2, 5, 2], [2, 2, 5, 2, 2, 5, 2], [5, 5, 5, 5, 5, 5, 5], [2, 2, 5, 2, 2, 5, 2], [2, 2, 5, 2, 2, 5, 2], [5, 5, 5, 5, 5, 0, 0], [2, 2, 5, 2, 2, 0, 0]]
example3_expected = [[5, 5], [5, 2]]
example3_transformed = [[5, 5], [5, 2]]

# Analyze each example
metrics1 = analyze_example(example1_input, example1_expected, example1_transformed)
metrics2 = analyze_example(example2_input, example2_expected, example2_transformed)
metrics3 = analyze_example(example3_input, example3_expected, example3_transformed)

print("Example 1 Metrics:", metrics1)
print("Example 2 Metrics:", metrics2)
print("Example 3 Metrics:", metrics3)
