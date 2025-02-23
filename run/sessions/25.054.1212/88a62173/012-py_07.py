"""
Divide the input grid into four quadrants and represent each quadrant in a 2x2 output grid.  If a quadrant contains any non-zero color, the corresponding output cell will have *that* color. If multiple non-zero colors exist in a quadrant, prioritize as follows: first, consider the colors present in the expected outputs. If a unique color exists, use that. If there's still ambiguity or no colors from expected are in the quadrant, if there is only one non-zero color in the quadrant, use that. If all quadrants are zero, return 0.
"""

import numpy as np
from collections import Counter

def get_representative_color(quadrant, expected_colors):
    """
    Determines the representative color for a quadrant.

    Args:
      quadrant: A numpy array representing the quadrant.
      expected_colors: a set of colors present in expected outputs.

    Returns:
      The representative color (int).
    """
    quadrant_counts = Counter(quadrant.flatten())
    
    # Remove 0 (background) from consideration
    if 0 in quadrant_counts:
        del quadrant_counts[0]

    if not quadrant_counts:  # If the quadrant is all zeros
        return 0

    non_zero_colors = list(quadrant_counts.keys())
    
    # Prioritize colors that appear in other "expected" outputs
    
    for color in expected_colors:
        if color in non_zero_colors:
            return color

    if len(non_zero_colors) == 1:
        return non_zero_colors[0]

    # If all the above fails, arbitrarily pick a color (should not happen)
    return non_zero_colors[0]
    

def transform(input_grid):
    """
    Transforms an input grid into a 2x2 output grid based on the presence of colors in each quadrant.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2, 2), dtype=int)

    # Calculate midpoints for quadrant divisions
    mid_row = (rows + 1) // 2
    mid_col = (cols + 1) // 2

    # Define quadrant boundaries
    quadrants = [
        (0, mid_row, 0, mid_col),       # Top-left
        (0, mid_row, mid_col, cols),   # Top-right
        (mid_row, rows, 0, mid_col),       # Bottom-left
        (mid_row, rows, mid_col, cols)    # Bottom-right
    ]

    expected_colors = set()

    # Iterate through quadrants and check for non-zero colors
    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = input_grid[row_start:row_end, col_start:col_end]
        # Get first non-zero value in quadrant

        quadrant_counts = Counter(quadrant.flatten())
        for color in quadrant_counts:
            if color != 0:
                expected_colors.add(color)

    # Iterate through quadrants and check for non-zero colors
    for i, (row_start, row_end, col_start, col_end) in enumerate(quadrants):
        quadrant = input_grid[row_start:row_end, col_start:col_end]
        # Get first non-zero value in quadrant
        representative_color = get_representative_color(quadrant, expected_colors)
        output_grid[i // 2, i % 2] = representative_color

    return output_grid.tolist()