import numpy as np
from typing import Tuple, List, Dict

def analyze_transformation(input_grid: np.ndarray, expected_output: np.ndarray, transformed_output: np.ndarray) -> Dict:
    """
    Analyzes the transformation results, providing detailed metrics and comparisons.

    Args:
        input_grid: The original input grid.
        expected_output: The expected output grid.
        transformed_output: The actual output grid produced by the transformation function.

    Returns:
        A dictionary containing analysis results, including:
        - match (bool): Whether the transformed output matches the expected output.
        - pixels_off (int): The number of pixels that differ between the expected and transformed outputs.
        - size_correct (bool): Whether the input and output grids have the same dimensions.
        - color_palette_correct (bool): Whether the transformed output uses only colors present in the input.
        - correct_pixel_counts (bool): correct pixel counts of each color
    """
    
    # Ensure that transformed_output is a NumPy array. This prevents common errors
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = 0 if match else np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape == transformed_output.shape
    
    input_colors = set(np.unique(input_grid))
    transformed_colors = set(np.unique(transformed_output))
    color_palette_correct = transformed_colors.issubset(input_colors.union({1})) # Allow for the introduction of blue (1)

    expected_counts = {color: np.sum(expected_output == color) for color in set(np.unique(expected_output)).union(input_colors)}
    transformed_counts = {color: np.sum(transformed_output == color) for color in set(np.unique(transformed_output)).union(input_colors)}
    
    correct_pixel_counts = expected_counts == transformed_counts

    analysis = {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "expected_counts": expected_counts,
        "transformed_counts": transformed_counts

    }
    return analysis