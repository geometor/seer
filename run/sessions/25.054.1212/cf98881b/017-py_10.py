import numpy as np

def analyze_example(input_grid, expected_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)

    input_colors = set(input_grid.flatten())
    output_colors = set(expected_output.flatten())
    input_shape = input_grid.shape
    output_shape = expected_output.shape

    match = np.array_equal(input_grid, expected_output)  # Check if shapes and values match
    size_correct = input_shape == output_shape
    color_palette_correct = input_colors == output_colors
    
    # create count of pixels that are the same between
    correct_pixel_count = 0
    if match:
        correct_pixel_count = input_shape[0] * input_shape[1]
    else:
        # compare pixel by pixel, only valid if sizes are the same:
        if size_correct:
            correct_pixel_count = np.sum(input_grid == expected_output)
    
    pixels_different = -1
    if size_correct:
        pixels_different = (input_shape[0] * input_shape[1]) - correct_pixel_count
    
    print(f"  Input Colors: {input_colors}")
    print(f"  Output Colors: {output_colors}")
    print(f"  Input Shape: {input_shape}")
    print(f"  Output Shape: {output_shape}")
    print(f"  Direct Match: {match}")
    print(f"  Size Correct: {size_correct}")
    print(f"  Color Palette Correct: {color_palette_correct}")
    print(f"  Correct Pixel Count (if sizes are equal): {correct_pixel_count}")
    print(f"  Number of pixels different (if size are equal): {pixels_different}")

# Example Usage (using the provided examples) - make sure to adjust the lists below
example_inputs = [
    [[0, 4, 0, 4, 2, 9, 9, 0, 0, 2, 0, 0, 0, 0], [0, 4, 0, 0, 2, 0, 0, 9, 9, 2, 0, 1, 0, 0], [4, 0, 0, 0, 2, 0, 0, 0, 0, 2, 1, 1, 1, 0], [4, 4, 4, 4, 2, 9, 0, 9, 0, 2, 1, 1, 0, 1]],
    [[4, 4, 4, 4, 2, 9, 0, 9, 0, 2, 0, 0, 0, 1], [4, 4, 0, 0, 2, 9, 9, 0, 0, 2, 1, 0, 0, 0], [4, 0, 4, 4, 2, 0, 0, 0, 9, 2, 0, 1, 0, 1], [0, 0, 0, 0, 2, 0, 0, 9, 0, 2, 1, 0, 1, 0]],
    [[4, 4, 4, 0, 2, 9, 9, 0, 9, 2, 0, 1, 0, 1], [0, 4, 0, 4, 2, 0, 0, 9, 0, 2, 0, 1, 0, 0], [0, 4, 0, 4, 2, 0, 0, 9, 9, 2, 1, 0, 0, 1], [4, 0, 4, 4, 2, 9, 9, 9, 0, 2, 0, 0, 0, 1]],
    [[0, 0, 0, 4, 2, 0, 0, 0, 9, 2, 0, 0, 0, 0], [4, 4, 0, 4, 2, 9, 0, 9, 0, 2, 0, 0, 0, 0], [4, 0, 4, 4, 2, 0, 9, 9, 0, 2, 1, 1, 0, 1], [0, 4, 4, 4, 2, 0, 9, 0, 0, 2, 1, 1, 1, 1]],
    [[4, 0, 4, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 1], [4, 4, 4, 4, 2, 0, 0, 0, 9, 2, 1, 1, 0, 0], [0, 4, 4, 4, 2, 0, 9, 9, 0, 2, 1, 1, 0, 1], [0, 4, 4, 0, 2, 0, 0, 9, 0, 2, 0, 1, 0, 1]]
]

example_outputs = [
    [[9, 4, 0, 4], [0, 4, 9, 9], [4, 1, 1, 0], [4, 4, 4, 4]],
    [[4, 4, 4, 4], [4, 4, 0, 0], [4, 1, 4, 4], [1, 0, 9, 0]],
    [[4, 4, 4, 9], [0, 4, 9, 4], [1, 4, 9, 4], [4, 9, 4, 4]],
    [[0, 0, 0, 4], [4, 4, 9, 4], [4, 9, 4, 4], [1, 4, 4, 4]],
    [[4, 0, 4, 1], [4, 4, 4, 4], [1, 4, 4, 4], [0, 4, 4, 1]]
]

for i, (input_grid, expected_output) in enumerate(zip(example_inputs, example_outputs)):
    print(f"Example {i + 1}:")
    analyze_example(input_grid, expected_output)
    print("-" * 40)
