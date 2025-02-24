import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    """Calculates matching, pixel differences, size correctness, and color palette correctness."""

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    
    expected_colors = set(np.unique(expected_output))
    transformed_colors = set(np.unique(transformed_output))
    color_palette_correct = expected_colors == transformed_colors
    
    # count the number of matching values of each color
    expected_counts = {}
    transformed_counts = {}
    for color in expected_colors:
        expected_counts[color] = np.sum(expected_output == color)
        transformed_counts[color] = np.sum(transformed_output == color)
    correct_pixel_counts = expected_counts == transformed_counts
        

    return {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
    }

# Example data (replace with actual data from the problem)
example1_input = np.array([
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
example1_expected = np.array([
    [8, 7, 8, 7, 8, 7, 8],
    [0, 7, 8, 7, 8, 7, 0],
    [0, 0, 8, 7, 8, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
example1_transformed = np.array([
    [0, 0, 8, 7, 8, 0, 0],
    [0, 0, 8, 7, 8, 0, 0],
    [0, 0, 8, 7, 8, 0, 0],
    [0, 0, 8, 0, 8, 0, 0],
    [0, 0, 8, 8, 8, 0, 0]
])

example2_input = np.array([
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])
example2_expected = np.array([
    [7, 8, 7, 8, 7, 8, 7, 0],
    [7, 8, 7, 8, 7, 8, 0, 0],
    [7, 8, 7, 8, 7, 0, 0, 0],
    [0, 8, 7, 8, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])
example2_transformed = np.array([
    [0, 8, 7, 8, 0, 0, 0, 0],
    [0, 8, 7, 8, 0, 0, 0, 0],
    [0, 8, 7, 8, 0, 0, 0, 0],
    [0, 8, 7, 8, 0, 0, 0, 0],
    [0, 8, 0, 8, 0, 0, 0, 0],
    [0, 8, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

metrics1 = calculate_metrics(example1_input, example1_expected, example1_transformed)
metrics2 = calculate_metrics(example2_input, example2_expected, example2_transformed)

print("Example 1 Metrics:", metrics1)
print("Example 2 Metrics:", metrics2)
