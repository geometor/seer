"""
The transformation extracts the first instance of a horizontally repeating pattern in the input grid to produce the output. The width of the repeating pattern is determined dynamically for each input.
"""

import numpy as np

def get_pattern_width(input_grid):
    """
    Finds the width of the repeating pattern.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])

    for width in range(1, cols + 1):
        is_repeating = True
        for r in range(rows):
            for c in range(cols - width):
                if input_grid[r][c] != input_grid[r][c + width]:
                    is_repeating = False
                    break
            if not is_repeating:
                break
        if is_repeating:
            return width
    return cols # If no repetition is found, return full width

def transform(input_grid):
    """
    Extracts the first instance of a horizontally repeating pattern.
    The pattern width is determined dynamically.
    """
    # Get the dimensions of the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Determine the width of the repeating unit (output grid width).
    output_cols = get_pattern_width(input_grid)

    # Initialize the output grid.
    output_grid = []

    # Extract the leftmost sub-grid of the determined width.
    for i in range(rows):
        output_grid.append(input_grid[i][:output_cols])

    return output_grid