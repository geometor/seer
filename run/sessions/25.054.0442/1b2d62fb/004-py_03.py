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
        pixels_off = None

    # Analyze regions to the right of the blue line.
    if blue_line_col != -1 and blue_line_col < input_width - 1:
        region_to_right = input_grid[:, blue_line_col + 1:]
        print(f"  Region to Right Dimensions: {region_to_right.shape}")

        #Count non-black pixels
        non_black_count = np.sum(region_to_right != 0)
        print(f"  Non-black Pixels to Right: {non_black_count}")

        # Check for azure pixels
        azure_pixels_expected = np.sum(expected_output == 8)
        azure_pixels_transformed = np.sum(transformed_output == 8)

        print(f" Expected Azure Pixels: {azure_pixels_expected}")
        print(f" Transformed Azure Pixels: {azure_pixels_transformed}")


    else:
        print("  No region to the right of the blue line.")
        non_black_count = None
        azure_pixels_expected = None
        azure_pixels_transformed = None

    return {
        "input_dims": (input_height, input_width),
        "expected_dims": (expected_height, expected_width),
        "transformed_dims": (transformed_height, transformed_width),
        "blue_line_col": blue_line_col,
        "pixels_off": pixels_off,
        "region_to_right_dims": region_to_right.shape if 'region_to_right' in locals() else None,
        "non_black_pixels_to_right": non_black_count,
        "azure_pixels_expected": azure_pixels_expected,
        "azure_pixels_transformed": azure_pixels_transformed,
    }
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

results = []
for i, (input_grid, expected_output, transformed_output) in enumerate(examples):
    print(f"Example {i+1}:")
    result = analyze_example(input_grid, expected_output, transformed_output)
    results.append(result)
