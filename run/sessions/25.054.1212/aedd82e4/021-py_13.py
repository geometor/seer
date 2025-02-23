import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape
    color_palette_correct = np.all(np.isin(transformed_output, [0, 1, 2]))
    unique_expected, counts_expected = np.unique(expected_output, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed_output, return_counts=True)
    
    correct_pixel_counts = True
    for color in unique_expected:
        if color not in unique_transformed or counts_expected[unique_expected == color][0] != counts_transformed[unique_transformed==color][0]:
            correct_pixel_counts = False
            break

    print(f"Pixels Off: {pixels_off}")
    print(f"Size Correct: {size_correct}")
    print(f"Color Palette Correct: {color_palette_correct}")
    print(f"Correct Pixel Counts: {correct_pixel_counts}")


print("Example 1:")
analyze_example(
    [[0, 2, 2], [0, 2, 2], [2, 0, 0]],
    [[0, 2, 2], [0, 2, 2], [1, 0, 0]],
    [[0, 2, 2], [0, 2, 2], [2, 1, 1]],
)

print("\nExample 2:")
analyze_example(
    [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 0, 2], [0, 2, 0, 0]],
    [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 0, 1], [0, 2, 0, 0]],
    [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 1, 2], [0, 2, 1, 1]],
)

print("\nExample 3:")
analyze_example(
    [[2, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 2], [0, 0, 0, 0], [0, 2, 2, 2]],
    [[2, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 1], [0, 0, 0, 0], [0, 2, 2, 2]],
    [[2, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 2], [0, 0, 1, 1], [0, 2, 2, 2]],
)

print("\nExample 4:")
analyze_example(
    [[2, 2, 0], [2, 0, 2], [0, 2, 0]],
    [[2, 2, 0], [2, 0, 1], [0, 1, 0]],
    [[2, 2, 0], [2, 1, 2], [0, 2, 1]],
)
