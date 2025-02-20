"""
Transforms the input grid by extracting a 3x3 sub-grid centered around the vertically middle gray cell,
changing the central cell and its immediate vertical neighbors (if gray and within the 3x3 area) to red (2),
and setting all other cells in the sub-grid to white (0).
"""

import numpy as np

def get_gray_positions(grid):
    # return the positions of gray cells (5) in the grid
    return np.array(np.where(grid == 5)).T

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    gray_positions = get_gray_positions(input_grid)

    # Handle cases with no gray cells
    if len(gray_positions) == 0:
        return np.zeros((3, 3), dtype=int)

    # Sort by y coordinate to find the vertical middle
    gray_positions = gray_positions[gray_positions[:, 0].argsort()]
    middle_gray_y = gray_positions[len(gray_positions) // 2, 0]

    # Filter gray positions that share the middle y-coordinate
    middle_gray_positions = gray_positions[gray_positions[:, 0] == middle_gray_y]

     # Sort by x coordinate to find the horizontal middle among middle ys.
    middle_gray_positions = middle_gray_positions[middle_gray_positions[:, 1].argsort()]
    center_x = middle_gray_positions[len(middle_gray_positions) // 2, 1]
    center_y = middle_gray_y

    # Initialize output grid
    output_grid = np.zeros((3, 3), dtype=int)

    # Calculate output grid center indices (handle edge cases for smaller grids)
    out_center_y = min(1, center_y)
    out_center_x = min(1, center_x)


    # Set the center pixel to red (2)
    output_grid[out_center_y, out_center_x] = 2

    # Check for and set vertical neighbors to red (2) if they are gray and within bounds
    if center_y > 0 and input_grid[center_y - 1, center_x] == 5:
        output_grid[out_center_y - 1, out_center_x] = 2
    if center_y < input_grid.shape[0] - 1 and input_grid[center_y + 1, center_x] == 5:
        output_grid[out_center_y + 1, out_center_x] = 2

    return output_grid