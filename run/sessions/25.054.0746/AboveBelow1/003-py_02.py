import numpy as np
from typing import List, Tuple

def analyze_results(input_grid, expected_output, transformed_output):
    """Analyzes the transformation results."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == transformed_output.shape
    
    # using sets to determine uniqueness and then sorting for consistent ordering
    input_colors = sorted(list(set(input_grid.flatten())))
    expected_colors = sorted(list(set(expected_output.flatten())))
    transformed_colors = sorted(list(set(transformed_output.flatten())))
    
    color_palette_correct = expected_colors == transformed_colors

    input_counts = {color: np.sum(input_grid == color) for color in input_colors}
    expected_counts = {color: np.sum(expected_output == color) for color in expected_colors}
    transformed_counts = {color: np.sum(transformed_output == color) for color in transformed_colors}

    correct_pixel_counts = expected_counts == transformed_counts

    return {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "input_colors": input_colors,
        "expected_colors": expected_colors,
        "transformed_colors": transformed_colors,
        "input_counts": input_counts,
        "expected_counts": expected_counts,
        "transformed_counts": transformed_counts
    }

# Example data (replace with your actual data)
example1_input = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4]
]
example1_expected = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
example1_transformed = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

example2_input = [
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0]
]
example2_expected = [
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
example2_transformed = [
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [0, 0, 0, 6, 6, 6, 0, 0, 0, 6, 6, 6, 6, 0, 6, 6],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 6, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0]
]

example3_input = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
example3_expected = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
example3_transformed = [
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
results1 = analyze_results(example1_input, example1_expected, example1_transformed)
results2 = analyze_results(example2_input, example2_expected, example2_transformed)
results3 = analyze_results(example3_input, example3_expected, example3_transformed)

print("Example 1 Results:", results1)
print("Example 2 Results:", results2)
print("Example 3 Results:", results3)
