"""
1.  **Identify Red Pixels:** Locate all red (value 2) pixels in the input grid.
2.  **Combine into Single Shape:** Consider all of the red pixels to make up a single combined object
3.  **Determine Interior Pixels**: Within the single shape, identify pixels that are not on the edge. I.e. their neighbors include only pixels within the object.
4.  **Transform Interior Pixels:** Change the color of all "interior" red pixels identified in step 3 to green (value 3).
5.  **Clear Remaining Pixels:** Change all non-interior red pixels and any other colored pixels to white (value 0).
"""

import numpy as np

def get_red_pixels(grid):
    """
    Finds all red pixels in the grid.

    Args:
        grid: The input grid.

    Returns:
        A set of (row, col) coordinates of red pixels.
    """
    red_pixels = set()
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                red_pixels.add((r, c))
    return red_pixels

def get_interior_pixels(red_pixels, rows, cols):
    """
    Finds the interior pixels of a combined shape.
    """
    interior_pixels = set()
    for r, c in red_pixels:
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        is_interior = True
        for nr, nc in neighbors:
            if not (0 <= nr < rows and 0 <= nc < cols and (nr, nc) in red_pixels):
                is_interior = False
                break
        if is_interior:
            interior_pixels.add((r, c))
    return interior_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # find all red pixels
    red_pixels = get_red_pixels(input_grid)
    rows, cols = len(input_grid), len(input_grid[0])

    # find interior red pixels
    interior_red_pixels = get_interior_pixels(red_pixels, rows, cols)
    
    # change color of interior pixels
    for r, c in interior_red_pixels:
        output_grid[r][c] = 3

    return output_grid