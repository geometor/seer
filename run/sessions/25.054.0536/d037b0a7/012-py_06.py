"""
1. Find Red: Identify all pixels that are the color red (value 2) in the input grid.
2. Identify Top Pixels in Relevant Columns: For *each column* that contains at least one red pixel,
   find the color of the top pixel (the pixel in the first row) of that column.
3. Propagate Downward: For each red pixel found, change the color of all pixels *directly below* it
   (in the same column, and *starting from the next row down*) to the top-row pixel's color for that column.
   If a column does not have a red pixel, it is left unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of red pixels.
    If a red pixel is found, all pixels below it in that
    *column* become the color of the top pixel in that column.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Find Red Pixels
    red_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))

    # 2. & 3. Propagate Downward within Columns
    for r, c in red_pixels:
        top_color = input_grid[0, c] # Get top color of *this* column
        for next_row in range(r + 1, rows): # Start from row *after* red
            output_grid[next_row, c] = top_color  # Fill with top color

    return output_grid