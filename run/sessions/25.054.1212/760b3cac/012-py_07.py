"""
1.  **Identify Individual Azure Pixels:** Locate all pixels with the value azure (8) in the input grid.

2.  **Iterative Horizontal Expansion:** For each azure pixel:
    *   Expand one pixel to the left. If the pixel to the left is white (0), change it to azure (8). Continue expanding left, one pixel at a time, as long as the encountered pixel is white (0). Stop when a non-white pixel or the left edge of the grid is reached.
    *   Expand one pixel to the right. If the pixel to the right is white (0), change it to azure (8). Continue expanding right, one pixel at a time, as long as the encountered pixel is white (0). Stop when a non-white pixel or the right edge of the grid is reached.

3.  **Preservation:** Pixels that are not azure (8) in the original input grid remain unchanged.

4. **Row Constraint**: Azure pixels will only appear on output rows that had one or more azure pixels on the same row of the input.
"""

import numpy as np

def get_azure_pixels(grid):
    """
    Locates all azure (8) pixels in the grid.
    Returns a list of (row, col) tuples.
    """
    rows, cols = grid.shape
    azure_pixels = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8:
                azure_pixels.append((r, c))
    return azure_pixels

def expand_pixel_horizontally(grid, row, col):
    """
    Expands a single azure pixel horizontally, filling white (0) pixels,
    until blocked by other colors or grid edges.
    """
    output_grid = np.copy(grid)
    rows, cols = output_grid.shape

    # Expand left
    c = col - 1
    while c >= 0 and output_grid[row, c] == 0:
        output_grid[row, c] = 8
        c -= 1

    # Expand Right
    c = col + 1
    while c < cols and output_grid[row, c] == 0:
        output_grid[row, c] = 8
        c += 1

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # get azure pixels
    azure_pixels = get_azure_pixels(input_grid)

    # expand each pixel horizontally
    for r, c in azure_pixels:
        output_grid = expand_pixel_horizontally(output_grid, r, c)
    return output_grid