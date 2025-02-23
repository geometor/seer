"""
1. Identify the single non-white color in the input grid.
2. Count the number of pixels of that color in the input grid.
3. Create a new grid with one row and a number of columns equal to the count from step 2.
4. Fill all the cells of the new grid with the identified non-white color.
"""

import numpy as np

def get_non_white_color(grid):
    """Helper function to extract the single non-white color from a grid."""
    # Flatten the grid and get unique colors
    unique_colors = np.unique(grid)
    # Filter out white (0) and return the remaining color
    non_white_colors = unique_colors[unique_colors != 0]
    return non_white_colors[0] if len(non_white_colors) > 0 else 0

def count_non_white_pixels(grid, color):
    """Helper function to count the occurrences of a specific color in a grid."""
    return np.count_nonzero(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the identified rule."""
    input_grid = np.array(input_grid)

    # 1. Identify the single non-white color.
    non_white_color = get_non_white_color(input_grid)

    # 2. Count the number of pixels of that color.
    pixel_count = count_non_white_pixels(input_grid, non_white_color)

    # 3. Create a new grid with one row and the appropriate number of columns.
    output_grid = np.full((1, pixel_count), non_white_color)

    # 4. The grid is already filled, so no further action is needed.

    return output_grid