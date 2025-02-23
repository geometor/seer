"""
1.  **Identify** the location of the red pixel (2) and the blue pixel (1) in the input grid.
2.  **For the red pixel:** Create a cross-shaped pattern of yellow pixels (4) centered on the red pixel's location. This cross extends one pixel horizontally and one pixel vertically from the red pixel.
3.  **For the blue pixel:** Create a cross-shaped pattern of orange pixels (7) centered on the blue pixel's location. This cross extends one pixel horizontally and one pixel vertically from the blue pixel.
4.  **Maintain** all other pixels (background, represented by 0) as they are. The output grid has the same dimensions as the input grid.
"""

import numpy as np

def find_pixel(grid, color):
    # Find the coordinates of a specific color pixel.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return first occurrence
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the red and blue pixels
    red_pixel_coords = find_pixel(input_grid, 2)
    blue_pixel_coords = find_pixel(input_grid, 1)

    # Create yellow cross around red pixel
    if red_pixel_coords:
        row, col = red_pixel_coords
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Adjacent cells
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 4

    # Create orange cross around blue pixel
    if blue_pixel_coords:
        row, col = blue_pixel_coords
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Adjacent cells
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
                output_grid[new_row, new_col] = 7

    return output_grid