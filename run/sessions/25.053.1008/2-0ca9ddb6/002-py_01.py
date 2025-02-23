"""
1.  **Identify Key Pixels:** Locate the red (2) and blue (1) pixels in the input grid.
2.  **Red Pixel Transformation:** For the red pixel, add two yellow (4) pixels: one directly above and one directly below its original position.
3.  **Blue Pixel Transformation:** For the blue pixel, add three orange (7) pixels: one directly above, one to it's right, and one more to the right of that.
4.  **Preserve Originals:** Keep the original red and blue pixels in their original positions.
5. **Output:** output is created by adding these pixels to the input.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    """Finds the coordinates of a pixel of the specified color."""
    for r, row in enumerate(grid):
        for c, pixel in enumerate(row):
            if pixel == color:
                return (r, c)  # row, col
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find red and blue pixels
    red_pos = find_pixel_by_color(input_grid, 2)
    blue_pos = find_pixel_by_color(input_grid, 1)

    # Add yellow pixels around red pixel
    if red_pos:
        r, c = red_pos
        if r > 0:
            output_grid[r - 1, c] = 4  # Above
        if r < rows - 1:
            output_grid[r + 1, c] = 4  # Below

    # Add orange pixels around blue pixel
    if blue_pos:
        r, c = blue_pos
        if r > 0:
          output_grid[r-1,c] = 7 # Above
        if c < cols - 1:
            output_grid[r, c + 1] = 7     # Right 1
        if c < cols - 2:
            output_grid[r, c + 2] = 7  # Right 2

    return output_grid