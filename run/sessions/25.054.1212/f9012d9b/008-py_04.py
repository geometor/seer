"""
Finds the most frequent non-zero color in the input grid and returns a 1x1 grid with that color.
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    """
    Transforms the input grid by finding most frequent non-zero color.

    Args:
        input_grid (list of lists): input grid
    Returns:
        (list of lists): 1x1 grid with most freq color
    """
    # Flatten the input grid to a 1D array.
    flat_grid = np.array(input_grid).flatten()

    # Count the occurrences of each color, excluding 0.
    color_counts = Counter(color for color in flat_grid if color != 0)

    # Find the most frequent color.
    most_frequent_color = color_counts.most_common(1)[0][0]

    # Create a 1x1 output grid with the most frequent color.
    output_grid = [[most_frequent_color]]

    return output_grid