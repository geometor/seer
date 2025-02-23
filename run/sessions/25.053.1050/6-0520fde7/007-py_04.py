import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    color_palette_correct = np.all(np.isin(np.unique(transformed_output), [0, 2]))
    correct_pixel_counts = True
    for color in np.unique(expected_output):
        if np.sum(expected_output == color) != np.sum(transformed_output == color):
            correct_pixel_counts = False
            break

    return {
        "pixels_off": int(pixels_off),
        "size_correct": bool(size_correct),
        "color_palette_correct": bool(color_palette_correct),
        "correct_pixel_counts": bool(correct_pixel_counts),
        "input_shape": input_grid.shape,
        "output_shape": expected_output.shape
    }
# Data
example1_input = np.array([[1, 0, 0, 5, 0, 1, 0], [0, 1, 0, 5, 1, 1, 1], [1, 0, 0, 5, 0, 0, 0]])
example1_expected = np.array([[0, 0, 0], [0, 2, 0], [0, 0, 0]])
example1_transformed = np.array([[2, 0, 2], [2, 0, 0], [2, 0, 2]])

example2_input = np.array([[1, 1, 0, 5, 0, 1, 0], [0, 0, 1, 5, 1, 1, 1], [1, 1, 0, 5, 0, 1, 0]])
example2_expected = np.array([[0, 2, 0], [0, 0, 2], [0, 2, 0]])
example2_transformed = np.array([[2, 0, 2], [0, 0, 0], [2, 0, 2]])

example3_input = np.array([[0, 0, 1, 5, 0, 0, 0], [1, 1, 0, 5, 1, 0, 1], [0, 1, 1, 5, 1, 0, 1]])
example3_expected = np.array([[0, 0, 0], [2, 0, 0], [0, 0, 2]])
example3_transformed = np.array([[0, 0, 2], [2, 0, 0], [0, 0, 0]])

#calculate and report
metrics1 = calculate_metrics(example1_input, example1_expected, example1_transformed)
metrics2 = calculate_metrics(example2_input, example2_expected, example2_transformed)
metrics3 = calculate_metrics(example3_input, example3_expected, example3_transformed)

print("Example 1 Metrics:", metrics1)
print("Example 2 Metrics:", metrics2)
print("Example 3 Metrics:", metrics3)