import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == transformed_output.shape if len(input_grid.shape) == len(transformed_output.shape) else (len(input_grid.shape) == 2 and transformed_output.shape == (1,1))
    
    # find white pixels in the input
    input_white_pixels = np.sum(input_grid == 0)
    output_value = transformed_output[0,0]

    print(f"  Input White Pixels: {input_white_pixels}")
    print(f"  Output Value: {output_value}")
    print(f"  Match: {match}")
    print(f"  Pixels Off: {pixels_off}")
    print(f"  Size Correct: {size_correct}")
    print("---")


# Example 1:
print("Example 1:")
input1 = [[5, 5, 0], [5, 0, 5], [0, 5, 0]]
expected_output1 = [[1]]
transformed_output1 = [[4]]
analyze_example(input1, expected_output1, transformed_output1)

# Example 2:
print("Example 2:")
input2 = [[8, 0, 8], [0, 8, 0], [8, 0, 8]]
expected_output2 = [[2]]
transformed_output2 = [[4]]
analyze_example(input2, expected_output2, transformed_output2)

# Example 4:
print("Example 4:")
input4 = [[0, 1, 1], [0, 1, 1], [1, 0, 0]]
expected_output4 = [[3]]
transformed_output4 = [[2]]
analyze_example(input4, expected_output4, transformed_output4)

# Example 7:
print("Example 7:")
input7 = [[0, 5, 0], [5, 5, 5], [0, 5, 0]]
expected_output7 = [[6]]
transformed_output7 = [[4]]
analyze_example(input7, expected_output7, transformed_output7)
