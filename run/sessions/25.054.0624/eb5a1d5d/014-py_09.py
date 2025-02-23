"""
The transformation extracts the nested rectangles from the input grid and represents them in a compressed form in the output grid. The output grid has a green border representing the outermost green rectangle, an azure border representing the second rectangle, a red border for the third, and a single blue pixel in the center for the innermost shape.
"""

import numpy as np

def get_object_bounds(grid, color):
    # Find the min and max row and col indices for a given color
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None  # Color not found
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Initialize output_grid as all green (3)
    output_grid = np.full((7, 7), 3)

    # Get bounds for azure (8) rectangle
    azure_bounds = get_object_bounds(input_grid, 8)
    if azure_bounds:
        min_row, max_row, min_col, max_col = azure_bounds
        # Represent azure rectangle with a border inside the green
        output_grid[1:6, 1:6] = 8

    # Get bounds for red (2) rectangle
    red_bounds = get_object_bounds(input_grid, 2)
    if red_bounds:
        min_row, max_row, min_col, max_col = red_bounds
        #Represent red rectangle with border within the azure.
        output_grid[2:5, 2:5] = 2

    # get bounds for blue (1) object
    blue_bounds = get_object_bounds(input_grid, 1)
    if blue_bounds:
        # Represent center as single blue pixel
        output_grid[3, 3] = 1


    return output_grid