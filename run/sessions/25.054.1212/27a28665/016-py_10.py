import numpy as np

def analyze_example(input_grid, expected_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)

    print(f"Input:\n{input_grid}")
    print(f"Expected Output:\n{expected_output}")

    # Count occurrences of each color in the input grid
    color_counts = {}
    for color in range(10):  # Colors 0-9
        color_counts[color] = np.sum(input_grid == color)
    print(f"Color Counts: {color_counts}")

    #find the number of non-zero pixels
    non_zero_pixels = np.count_nonzero(input_grid)
    print(f"Non-zero Pixels: {non_zero_pixels}")

    output_value = expected_output[0,0]
    print(f"Output Value: {output_value}")
    print("---")

# Example 1:
print("Example 1:")
input1 = [[5, 5, 0], [5, 0, 5], [0, 5, 0]]
expected_output1 = [[1]]
analyze_example(input1, expected_output1)

# Example 2:
print("Example 2:")
input2 = [[8, 0, 8], [0, 8, 0], [8, 0, 8]]
expected_output2 = [[2]]
analyze_example(input2, expected_output2)

# Example 3:
print("Example 4:")
input4 = [[0, 1, 1], [0, 1, 1], [1, 0, 0]]
expected_output4 = [[3]]
analyze_example(input4, expected_output4)

# Example 4:
print("Example 7:")
input7 = [[0, 5, 0], [5, 5, 5], [0, 5, 0]]
expected_output7 = [[6]]
analyze_example(input7, expected_output7)