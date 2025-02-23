"""
1. Identify the unique non-white color: Examine the input grid and determine the single color (represented by an integer 1-9) that is present, excluding white (0).
2. Count the target pixels: Count the number of pixels in the input grid that have the identified color.
3. Create the output grid: Create a new grid with a height of 1 and a width equal to the count from step 2.
4. Fill the output grid: Fill all cells of the output grid with the color identified in step 1.
"""

import numpy as np

def _get_unique_non_white_color(grid):
    """Helper function to find the unique non-white color in the grid."""
    non_white_colors = np.unique(grid[grid != 0])
    if len(non_white_colors) == 1:
        return non_white_colors[0]
    else:
        return None  # Or raise an exception, depending on desired behavior

def _count_pixels_of_color(grid, color):
    """Helper function to count pixels of a specific color."""
    return np.count_nonzero(grid == color)

def transform(input_grid):
    """
    Transforms the input grid based on the identified transformation rule.
    """
    # 1. Identify the unique non-white color.
    unique_color = _get_unique_non_white_color(input_grid)
    
    if unique_color is None:
        return np.array([]) # Return empty if no unique color

    # 2. Count the target pixels.
    pixel_count = _count_pixels_of_color(input_grid, unique_color)

    # 3. Create the output grid.
    output_grid = np.full((1, pixel_count), unique_color, dtype=int)

    # 4. Fill the output grid (already done in step 3).

    return output_grid