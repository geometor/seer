"""
Find the contiguous region of 1s (blue object) in the input grid. Change all pixels in this region to 2 (red).
Create a new output grid of the same dimensions, filled with 0s. Place the transformed red object at the top-left (0,0).
"""

import numpy as np

def find_object(grid):
    """Finds the bounding box of the contiguous region of 1s."""
    rows, cols = np.where(grid == 1)
    if len(rows) == 0:
        return None  # No object found
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    """Transforms the input grid by moving the blue object to the top-left and changing its color to red."""
    # Find the object's bounding box
    object_bounds = find_object(input_grid)

    # Initialize output grid with 0s
    output_grid = np.zeros_like(input_grid)

    if object_bounds:
        (min_row, min_col), (max_row, max_col) = object_bounds
        # Extract the object and change its color to red (2)
        object_region = input_grid[min_row:max_row+1, min_col:max_col+1]
        object_width = max_col - min_col + 1
        object_height = max_row - min_row + 1

        for r in range(object_height):
            for c in range(object_width):
                if object_region[r,c] == 1:
                    output_grid[r,c] = 2

    return output_grid