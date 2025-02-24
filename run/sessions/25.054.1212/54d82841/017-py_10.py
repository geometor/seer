import numpy as np
from collections import Counter

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example and returns a report."""
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = None if match else np.where(expected_output != transformed_output)
    size_correct = input_grid.shape != transformed_output.shape and expected_output.shape == transformed_output.shape
    color_palette_correct = set(np.unique(transformed_output)) <= set(np.unique(expected_output))

    expected_counts = Counter(expected_output.flatten())
    transformed_counts = Counter(transformed_output.flatten())
    correct_pixel_counts = expected_counts == transformed_counts

    report = {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
    }
    return report

# Example Data (replace with actual grid data from the problem)
example1_input = [[0, 6, 6, 6, 0, 0, 0, 0], [0, 6, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6], [0, 0, 0, 0, 0, 6, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
example1_expected = [[0, 6, 6, 6, 0, 0, 0, 0], [0, 6, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6], [0, 0, 0, 0, 0, 6, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 4, 0, 0, 0, 4, 0]]
example1_transformed = [[0, 6, 6, 6, 0, 0, 0, 0], [0, 6, 0, 6, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 6, 6], [0, 0, 0, 0, 0, 6, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

example2_input = [[0, 3, 3, 3, 0], [0, 3, 0, 3, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
example2_expected = [[0, 3, 3, 3, 0], [0, 3, 0, 3, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 4, 0, 0]]
example2_transformed = [[0, 3, 3, 3, 0], [0, 3, 0, 3, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

example3_input = [[0, 0, 0, 0, 0, 0, 0], [0, 8, 8, 8, 0, 0, 0], [0, 8, 0, 8, 6, 6, 6], [0, 0, 0, 0, 6, 0, 6], [0, 0, 0, 0, 0, 0, 0]]
example3_expected = [[0, 0, 0, 0, 0, 0, 0], [0, 8, 8, 8, 0, 0, 0], [0, 8, 0, 8, 6, 6, 6], [0, 0, 0, 0, 6, 0, 6], [0, 0, 4, 0, 0, 4, 0]]
example3_transformed = [[0, 0, 0, 0, 0, 0, 0], [0, 8, 8, 8, 0, 0, 0], [0, 8, 0, 8, 6, 6, 6], [0, 0, 0, 0, 6, 0, 6], [0, 0, 0, 0, 0, 0, 0], [0, 4, 0, 0, 4, 0, 0]]

report1 = analyze_example(example1_input, example1_expected, example1_transformed)
report2 = analyze_example(example2_input, example2_expected, example2_transformed)
report3 = analyze_example(example3_input, example3_expected, example3_transformed)

print("Example 1 Report:", report1)
print("Example 2 Report:", report2)
print("Example 3 Report:", report3)
