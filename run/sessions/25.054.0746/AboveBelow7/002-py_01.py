"""
The transformation rule is to swap the vertical positions of a yellow rectangle and a green U-shape within the grid, while preserving their shapes and keeping the white background unchanged.
"""

import numpy as np

def find_object(grid, color, shape_type):
    """
    Finds an object of specified color and shape type in the grid.
    Returns a list of (row, col) coordinates of the object's pixels.
    """
    coords = []
    if shape_type == "rectangle":
        rows, cols = np.where(grid == color)
        if len(rows) > 0:
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)
            for r in range(min_row, max_row + 1):
                for c in range(min_col, max_col + 1):
                    coords.append((r, c))
    elif shape_type == "U-shape":
        rows, cols = np.where(grid == color)
        if len(rows) > 0:
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)
            for r in range(min_row, max_row + 1):
                for c in range(min_col, max_col + 1):
                    coords.append((r, c)) # Add all points for now, refine U-shape detection later if needed
    return coords

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the yellow rectangle
    yellow_coords = find_object(input_grid, 4, "rectangle")

    # Find the green U-shape
    green_coords = find_object(input_grid, 3, "U-shape")
    
    # Clear the original positions of the yellow rectangle and green structure in the output grid
    for r, c in yellow_coords:
        output_grid[r, c] = 0
    for r, c in green_coords:
        output_grid[r, c] = 0        

    # Calculate the vertical shift needed for swapping
    yellow_min_row = min(r for r, c in yellow_coords)
    green_min_row = min(r for r, c in green_coords)
    shift = green_min_row - yellow_min_row

    # Move yellow rectangle down
    for r, c in yellow_coords:
        output_grid[r + shift, c] = 4

    # move the green structure up
    shift = yellow_min_row - green_min_row
    for r, c in green_coords:
        output_grid[r + shift, c] = 3


    return output_grid