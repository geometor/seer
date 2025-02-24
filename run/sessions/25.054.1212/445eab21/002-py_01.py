"""
1. Identify the target object: Locate the contiguous region of azure (8) pixels within the input grid.
2. Determine the bounding box:** Find the smallest rectangle that completely encloses the azure region.
3. Extract the bounding box:** Create a new grid containing only the pixels within the determined bounding box. In this example, the bounding box of the azure object is a 2 x 2 square.
4. Present only the bounding box in the new grid, forming the output.
"""

import numpy as np

def find_bounding_box(grid, target_color):
    # Find coordinates of target color
    rows, cols = np.where(grid == target_color)

    # Handle case where target color is not found
    if len(rows) == 0:
        return None, None, None, None

    # Calculate min and max row/col
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Define target color (azure)
    target_color = 8

    # Find the bounding box of the target color
    min_row, max_row, min_col, max_col = find_bounding_box(input_grid, target_color)

    # Handle case where target_color not present
    if min_row is None:
       return [[]]

    # Extract the bounding box region
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()