"""
1.  **Red Pixel Expansion:** The red pixel (color 2) expands horizontally by one pixel in both directions, creating new yellow pixels (color 4). This expansion is mirrored across the original red pixel's vertical axis.

2.  **Blue Pixel Expansion:** The blue pixel (color 1) expands by one pixel in all orthogonal directions (up, down, left, and right), creating new orange pixels (color 7).
"""

import numpy as np

def get_pixel_positions(grid, color):
    return np.argwhere(grid == color).tolist()

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find red pixel
    red_pixel_positions = get_pixel_positions(input_grid, 2)
    if red_pixel_positions:
      red_pixel = red_pixel_positions[0]
    
      # Horizontal expansion for red pixel
      for i in [-1, 1]:
        new_x = red_pixel[1] + i
        if 0 <= new_x < output_grid.shape[1]:
          output_grid[red_pixel[0], new_x] = 4
          

    # Find blue pixel
    blue_pixel_positions = get_pixel_positions(input_grid, 1)
    if blue_pixel_positions:
      blue_pixel = blue_pixel_positions[0]
    
      # Orthogonal expansion for blue pixel
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
          new_x = blue_pixel[1] + dx
          new_y = blue_pixel[0] + dy
          if 0 <= new_x < output_grid.shape[1] and 0 <= new_y < output_grid.shape[0]:
            output_grid[new_y, new_x] = 7

    return output_grid