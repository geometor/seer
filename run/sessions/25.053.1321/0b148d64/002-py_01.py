"""
The input grid is cropped to the bounding box defined by the red pixels.
The azure pixels are removed, leaving only the red and white pixels within the bounding box.
"""

import numpy as np

def get_bounding_box(grid, color):
    # Find rows and cols containing the specified color
    rows = np.any(grid == color, axis=1)
    cols = np.any(grid == color, axis=0)
    # Get min and max row/col indices
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    return rmin, rmax, cmin, cmax

def transform(input_grid):
    """
    Crops the input grid to the bounding box of the red pixels.
    """
    # Convert input_grid to a NumPy array for easier manipulation.
    input_grid = np.array(input_grid)

    # Find the bounding box coordinates for the red pixels (color 2).
    rmin, rmax, cmin, cmax = get_bounding_box(input_grid, 2)

    # Crop the grid to the bounding box.
    output_grid = input_grid[rmin:rmax+1, cmin:cmax+1]

    return output_grid.tolist()