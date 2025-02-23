"""
1.  **Identify initial objects:** Locate the single red (2) pixel and the single blue (1) pixel in the input grid. Note their positions.
2.  **Red Pixel Expansion:**  Create two yellow (4) pixels horizontally adjacent to the red pixel, one to its left and one to its right. If there are no positions to its left and right (i.e., it's on the edge of the board, mirror the position, placing another yellow on the same side.
3. **Red Pixel Expansion, phase 2:** Create two yellow (4) pixels vertically adjacent to the red pixel, one above and one below.
4.  **Blue Pixel Expansion:** Create two orange (7) pixels horizontally adjacent to the blue pixel, on to its left and one to its right.
5. **Blue Pixel Expansion, phase 2:** Create two orange (7) pixels vertically adjacent to the blue pixel, one above and one below.
6. **Preserve**: Keep the original red and blue pixels in their original locations.
"""

import numpy as np

def get_object_coordinates(grid, color):
    coords = np.argwhere(grid == color)
    return coords.tolist()

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # find red and blue pixels
    red_coords = get_object_coordinates(input_grid, 2)
    blue_coords = get_object_coordinates(input_grid, 1)

    # Red pixel expansion
    if red_coords:
        row, col = red_coords[0]
        # Horizontal expansion
        if col > 0:
            output_grid[row, col - 1] = 4
        if col < output_grid.shape[1] - 1:
            output_grid[row, col + 1] = 4
        # Vertical expansion
        if row > 0:
            output_grid[row-1,col]=4
        if row < output_grid.shape[0] -1:
          output_grid[row+1, col] = 4

    # Blue pixel expansion
    if blue_coords:
        row, col = blue_coords[0]
        #Horizontal expansion
        if col > 0:
          output_grid[row, col -1] = 7
        if col < output_grid.shape[1] - 1:
          output_grid[row, col + 1] = 7

        #vertical expansion
        if row > 0:
          output_grid[row - 1, col] = 7
        if row < output_grid.shape[0] - 1:
          output_grid[row + 1, col] = 7
    

    return output_grid