import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    input_height, input_width = input_grid.shape
    expected_height, expected_width = expected_output.shape
    transformed_height, transformed_width = transformed_output.shape

    blue_line_col = -1
    for j in range(input_width):
        if all(input_grid[:, j] == 1):
            blue_line_col = j
            break

    print(f"  Input Dimensions: {input_height}x{input_width}")
    print(f"  Expected Output Dimensions: {expected_height}x{expected_width}")
    print(f"  Transformed Output Dimensions: {transformed_height}x{transformed_width}")
    print(f"  Blue Line Column: {blue_line_col}")

    # Compare expected and transformed outputs
    if expected_output.shape == transformed_output.shape:
        diff = expected_output != transformed_output
        pixels_off = np.sum(diff)
        print(f"  Pixels Different: {pixels_off}")
    else:
        print("  Output dimensions do not match, cannot compare pixels.")

# Example Data (replace with your actual data)
examples = [
    (
        [[0, 9, 9, 1, 9, 9, 9],
         [0, 0, 9, 1, 9, 9, 0],
         [9, 0, 9, 1, 9, 9, 0],
         [0, 0, 0, 1, 9, 0, 0],
         [0, 9, 9, 1, 9, 9, 9]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]]
    ),
    (
        [[0, 0, 0, 1, 9, 0, 0],
         [9, 0, 9, 1, 9, 9, 9],
         [0, 9, 9, 1, 9, 9, 9],
         [0, 0, 0, 1, 9, 9, 9],
         [0, 9, 9, 1, 9, 9, 9]],
        [[0, 8, 8],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]]
    ),
     (
        [[9, 0, 0, 1, 9, 0, 9],
         [9, 0, 0, 1, 0, 9, 0],
         [9, 0, 0, 1, 9, 0, 0],
         [0, 9, 9, 1, 0, 9, 9],
         [0, 0, 9, 1, 0, 9, 0]],
        [[0, 8, 0],
         [0, 0, 8],
         [0, 8, 8],
         [8, 0, 0],
         [8, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]]
    ),
      (
        [[0, 9, 9, 1, 9, 0, 9],
         [9, 0, 0, 1, 9, 0, 0],
         [9, 9, 9, 1, 9, 9, 9],
         [0, 9, 0, 1, 0, 0, 0],
         [9, 0, 0, 1, 9, 0, 0]],
        [[0, 0, 0],
         [0, 8, 8],
         [0, 0, 0],
         [8, 0, 8],
         [0, 8, 8]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]]
    ),
      (
        [[0, 9, 9, 1, 9, 0, 9],
         [9, 0, 9, 1, 9, 9, 9],
         [9, 9, 9, 1, 0, 0, 9],
         [9, 0, 0, 1, 9, 0, 0],
         [9, 9, 9, 1, 0, 0, 9]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]],
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [8, 8, 8],
         [0, 0, 0]]
    ),
]

for i, (input_grid, expected_output, transformed_output) in enumerate(examples):
    print(f"Example {i+1}:")
    analyze_example(input_grid, expected_output, transformed_output)