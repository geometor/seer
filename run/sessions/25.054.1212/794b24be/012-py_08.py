"""
Counts the number of blue pixels in the input grid. Creates a red bar in the
first row of the output grid. The width of the red bar is equal to the number of
blue pixels, capped at the width of the grid (3).  If there were any blue
pixels, a single red pixel is placed in the second row. The x-coordinate of
this pixel is the same as the x-coordinate of the last blue pixel in the input
grid. All other pixels are white.
"""

import numpy as np

def _find_last_blue_pixel_x(input_grid):
    """Finds the x-coordinate of the last blue pixel."""
    blue_pixels = np.where(input_grid == 1)
    blue_x_coords = blue_pixels[1]
    return blue_x_coords[-1] if blue_x_coords.size > 0 else -1

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.

    Args:
        input_grid: A 3x3 NumPy array representing the input grid.

    Returns:
        A 3x3 NumPy array representing the transformed output grid.
    """
    # Initialize output_grid as all white.
    output_grid = np.zeros_like(input_grid)

    # Count blue pixels.
    blue_count = np.sum(input_grid == 1)

    # Determine the width of the red bar (capped at grid width).
    red_bar_width = min(blue_count, input_grid.shape[1]) # shape[1] is width

    # Create the red bar in the first row.
    output_grid[0, :red_bar_width] = 2

    # Find the x-coordinate of the last blue pixel.
    last_blue_x = _find_last_blue_pixel_x(input_grid)

    # Place a single red pixel in the second row if blue pixels exist.
    if last_blue_x != -1:
        output_grid[1, last_blue_x] = 2

    return output_grid