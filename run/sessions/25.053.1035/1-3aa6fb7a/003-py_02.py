import numpy as np
from io import StringIO

def calculate_metrics(input_str, expected_str, transformed_str):
    input_grid = np.loadtxt(StringIO(input_str), dtype=int)
    expected_grid = np.loadtxt(StringIO(expected_str), dtype=int)
    transformed_grid = np.loadtxt(StringIO(transformed_str), dtype=int)

    pixels_off = np.sum(expected_grid != transformed_grid)
    size_correct = input_grid.shape == expected_grid.shape == transformed_grid.shape
    
    unique_expected, counts_expected = np.unique(expected_grid, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed_grid, return_counts=True)

    color_palette_correct = np.array_equal(np.sort(unique_expected), np.sort(unique_transformed))
    correct_pixel_counts = np.array_equal(counts_expected, counts_transformed)

    report = {
        'pixels_off': int(pixels_off),
        'size_correct': bool(size_correct),
        'color_palette_correct': bool(color_palette_correct),
        'correct_pixel_counts':  bool(correct_pixel_counts)
    }
    return report

input_str = """
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
expected_str = """
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
transformed_str = """
0 0 0 0 0 0 0
0 1 0 0 0 0 0
0 1 8 0 0 0 0
0 0 0 0 1 8 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""

report = calculate_metrics(input_str, expected_str, transformed_str)
print(report)
