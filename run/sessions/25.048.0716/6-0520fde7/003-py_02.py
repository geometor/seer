"""
Transforms the input grid to the output grid by focusing on a 3x3 region centered around a gray object (color 5).
It changes the color of blue cells within this region to red and fills the rest with white.
"""

import numpy as np

def find_gray_center(input_grid):
    # Find the gray object (color 5) in the middle row.
    middle_row_index = input_grid.shape[0] // 2
    middle_row = input_grid[middle_row_index]
    gray_indices = np.where(middle_row == 5)[0]
    if gray_indices.size > 0:
        return (middle_row_index, gray_indices[0])  # Return the first gray object's column if multiple exist
    return None

def transform(input_grid):
    # Initialize output_grid as all white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the central gray object.
    center_coords = find_gray_center(input_grid)

    if center_coords:
        # Define 3x3 region boundaries based on input.
        row_start = center_coords[0] - 1
        row_end = center_coords[0] + 2
        col_start = center_coords[1] - 1
        col_end = center_coords[1] + 2

        # Extract the 3x3 subgrid from the input grid
        subgrid = input_grid[row_start:row_end, col_start:col_end]
      
        # Find relative coordinates of blue cells (color 1) within subgrid
        blue_coords = np.where(subgrid == 1)

        # Transform identified blue cells in the relative coordinates to red.
        for r, c in zip(blue_coords[0], blue_coords[1]):
              output_grid[r,c] = 2
    return output_grid