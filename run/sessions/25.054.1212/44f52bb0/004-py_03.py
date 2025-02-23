import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    red_count = np.count_nonzero(input_grid == 2)
    match = np.array_equal(expected_output, transformed_output)
    output_value = expected_output.flatten()[0]

    print(f"  Red Count: {red_count}")
    print(f"  Output Value: {output_value}")
    print(f"  Match: {match}")
    print("---")

print("Example 1:")
analyze_example([[2, 0, 2], [0, 2, 0], [2, 0, 2]], [[1]], [[1]])

print("Example 2:")
analyze_example([[2, 0, 0], [2, 0, 0], [0, 2, 0]], [[7]], [[1]])

print("Example 3:")
analyze_example([[2, 0, 2], [2, 0, 2], [2, 0, 2]], [[1]], [[1]])

print("Example 4:")
analyze_example([[0, 0, 0], [2, 0, 2], [0, 0, 0]], [[1]], [[1]])

print("Example 5:")
analyze_example([[2, 2, 0], [0, 2, 2], [0, 0, 0]], [[7]], [[1]])

print("Example 6:")
analyze_example([[2, 2, 0], [0, 2, 0], [0, 0, 0]], [[7]], [[1]])
