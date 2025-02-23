import numpy as np

def analyze_example(input_grid, expected_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)

    height, width = input_grid.shape
    output_height, output_width = expected_output.shape

    print(f"Input Dimensions: {height}x{width}")
    print(f"Output Dimensions: {output_height}x{output_width}")

    if output_height != 2 * height:
        print("ERROR: Output height is not double the input height.")
        return

    if output_width != width:
        print("ERROR: Output width does not match input width.")
        return
    
    row_mapping = {} # input row -> list of output rows

    for i in range(height):
        input_row = tuple(input_grid[i])
        row_mapping[i] = []
        for j in range(output_height):
            output_row = tuple(expected_output[j])
            if np.array_equal(input_row, output_row):
                row_mapping[i].append(j)
    print(row_mapping)


# Example Data (from the prompt)
example1_input = [[9, 9, 5, 9], [5, 5, 9, 9], [9, 5, 9, 9]]
example1_output = [[9, 9, 5, 9], [5, 5, 9, 9], [9, 5, 9, 9], [9, 9, 5, 9], [5, 5, 9, 9], [9, 5, 9, 9]]

example2_input = [[4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1]]
example2_output = [[4, 4, 4, 1], [1, 1, 1, 1], [4, 1, 1, 4], [4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1]]

example3_input = [[9, 4, 9, 4], [9, 9, 4, 4], [4, 4, 4, 4]]
example3_output = [[4, 4, 4, 4], [9, 9, 4, 4], [9, 4, 9, 4], [9, 4, 9, 4], [9, 9, 4, 4], [4, 4, 4, 4]]

example4_input = [[3, 3, 5, 5], [3, 5, 5, 3], [5, 5, 3, 3]]
example4_output = [[5, 5, 3, 3], [3, 5, 5, 3], [3, 3, 5, 5], [3, 3, 5, 5], [3, 5, 5, 3], [5, 5, 3, 3]]

print("Example 1:")
analyze_example(example1_input, example1_output)
print("\nExample 2:")
analyze_example(example2_input, example2_output)
print("\nExample 3:")
analyze_example(example3_input, example3_output)
print("\nExample 4:")
analyze_example(example4_input, example4_output)