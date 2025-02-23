"""
This program transforms an input grid containing two maroon rectangles into an output grid where the rectangles
are partially recolored to blue and green, and surrounded by green and blue filling.
"""

import numpy as np

def find_object(grid, color):
    # Find the bounding box of the object of the given color.
    rows, cols = np.where(grid == color)
    if len(rows) == 0:
        return None  # Object not found
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the two maroon rectangles
    top_left_start, top_left_end = find_object(input_grid, 9)
    bottom_right_start, bottom_right_end = find_object(input_grid, 9)
    
    # Check if the top-left rectangle exists
    if top_left_start is not None:
        # Top-Left Maroon Shape Transformation

        # Fill right with green
        output_grid[top_left_start[0]:top_left_end[0]+1, top_left_end[1] + 1:top_left_end[1] + 3] = 3
        # Fill below with blue
        output_grid[top_left_end[0] + 1:top_left_end[0] + 3, top_left_start[1]:top_left_end[1]+1] = 1

        # Change top two rows to green
        output_grid[top_left_start[0]:top_left_start[0] + 2, top_left_start[1]:top_left_end[1] + 1] = 3
        # Change leftmost two columns to green
        output_grid[top_left_start[0]:top_left_end[0] + 1, top_left_start[1]:top_left_start[1] + 2] = 3
        # Change the remaining to blue
        output_grid[top_left_start[0] + 2:top_left_end[0] + 1, top_left_start[1] + 2:top_left_end[1] + 1] = 1


    # Check if the bottom-right rectangle exists
    if bottom_right_start is not None:
        # Bottom-Right Maroon Shape Transformation
        
        # Fill left with blue
        output_grid[bottom_right_start[0]:bottom_right_end[0]+1, bottom_right_start[1]-2:bottom_right_start[1]] = 1
        #Fill above with green
        output_grid[bottom_right_start[0]-2:bottom_right_start[0], bottom_right_start[1]:bottom_right_end[1]+1] = 3

        # Change rightmost two columns to green
        output_grid[bottom_right_start[0]:bottom_right_end[0] + 1, bottom_right_end[1] - 1:bottom_right_end[1] + 1] = 3
        # Change bottom two rows to green
        output_grid[bottom_right_end[0] - 1:bottom_right_end[0] + 1, bottom_right_start[1]:bottom_right_end[1] + 1] = 3
        # Change the remaining to blue
        output_grid[bottom_right_start[0]:bottom_right_end[0] - 1, bottom_right_start[1]:bottom_right_end[1] - 1] = 1

    return output_grid