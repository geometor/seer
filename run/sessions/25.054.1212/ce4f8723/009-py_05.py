import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape  #this is changed in this task
    unique_colors_input = np.unique(input_grid)
    unique_colors_output = np.unique(expected_output)
    color_palette_correct = np.array_equal(np.sort(unique_colors_input), np.sort(unique_colors_output))
    
    input_counts = {color: np.sum(input_grid == color) for color in unique_colors_input}
    expected_counts = {color: np.sum(expected_output == color) for color in unique_colors_output}
    correct_pixel_counts = input_counts == expected_counts
    
    print(f"Pixels Off: {pixels_off}")
    print(f"Size Correct: {size_correct}")
    print(f"Unique Colors in Input: {unique_colors_input}")
    print(f"Unique Colors in Output: {unique_colors_output}")    
    print(f"Color Palette Correct: {color_palette_correct}")
    print(f"Input Pixel Counts: {input_counts}")
    print(f"Expected Output Pixel Counts: {expected_counts}")    
    print(f"Correct Pixel Counts: {correct_pixel_counts}")



print("Example 1:")
analyze_example(
    [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0], [4, 4, 4, 4], [2, 2, 2, 2], [0, 0, 2, 2], [2, 2, 0, 0], [0, 0, 2, 2]],
    [[3, 3, 3, 3], [0, 3, 3, 3], [3, 3, 0, 0], [3, 0, 3, 3]],
    [[3, 3, 0, 0], [0, 3, 0, 3], [0, 3, 0, 0], [3, 0, 3, 0]]
)

print("\nExample 2:")
analyze_example(
    [[1, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1], [4, 4, 4, 4], [0, 0, 0, 2], [0, 0, 0, 2], [2, 2, 2, 2], [2, 2, 0, 2]],
    [[3, 3, 3, 3], [0, 3, 0, 3], [3, 3, 3, 3], [3, 3, 0, 3]],
    [[3, 3, 3, 0], [0, 3, 0, 3], [0, 0, 3, 3], [3, 3, 0, 3]]
)

print("\nExample 3:")
analyze_example(
    [[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [1, 1, 1, 1], [4, 4, 4, 4], [2, 2, 0, 2], [0, 0, 2, 0], [0, 2, 0, 0], [2, 0, 2, 0]],
    [[3, 3, 0, 3], [3, 0, 3, 0], [3, 3, 0, 3], [3, 3, 3, 3]],
    [[3, 3, 0, 0], [3, 0, 3, 0], [3, 3, 0, 3], [3, 3, 3, 3]]
)

print("\nExample 4:")
analyze_example(
    [[1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [4, 4, 4, 4], [2, 2, 0, 0], [0, 0, 2, 0], [2, 2, 0, 0], [0, 0, 2, 0]],
    [[3, 3, 3, 0], [3, 3, 3, 3], [3, 3, 3, 3], [0, 3, 3, 3]],
    [[3, 0, 3, 0], [3, 3, 0, 3], [3, 0, 3, 3], [0, 3, 0, 3]]
)