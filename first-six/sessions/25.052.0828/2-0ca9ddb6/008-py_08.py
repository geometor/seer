"""
The transformation rule involves creating a yellow cross around each red cell and placing orange cells around each blue cell in the cardinal directions. The output grid starts filled with zeros.

1.  **Initialize:** Create an output grid filled with zeros (0) with the same dimensions as the input grid.
2.  **Locate:** Find all red (2) and blue (1) cells in the input grid.
3.  **Red Cell Transformation:** For each red cell:
    *   Place a yellow (4) cell one position above, below, to the left, and to the right of the red cell in the *output grid*.
4.  **Blue Cell Transformation:** For each blue cell:
    *   Place an orange (7) cell one position above, below, to the left, and to the right of the blue cell in the *output grid*.
5. **Copy remaining Input values:** Copy other values, such as 6 in this example, to the same position in the *output grid*.
"""

import numpy as np

def find_objects(grid, color):
    # Find the coordinates of all single-cell objects of the specified color.
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    # Initialize the output grid with zeros.
    output_grid = np.zeros_like(input_grid)

    # Find all red (2) and blue (1) cells.
    red_positions = find_objects(input_grid, 2)
    blue_positions = find_objects(input_grid, 1)

    # Create yellow crosses around each red cell.
    for y, x in red_positions:
        if y > 0:
            output_grid[y-1, x] = 4  # Above
        if y < output_grid.shape[0]-1:
            output_grid[y+1, x] = 4  # Below
        if x > 0:
            output_grid[y, x-1] = 4  # Left
        if x < output_grid.shape[1]-1:
            output_grid[y, x+1] = 4  # Right
        output_grid[y,x] = input_grid[y,x]

    # Create orange surrounds for each blue cell.
    for y, x in blue_positions:
        if y > 0:
            output_grid[y-1, x] = 7  # Above
        if y < output_grid.shape[0]-1:
            output_grid[y+1, x] = 7  # Below
        if x > 0:
            output_grid[y, x-1] = 7  # Left
        if x < output_grid.shape[1]-1:
            output_grid[y, x+1] = 7  # Right
        output_grid[y,x] = input_grid[y,x]

    #Copy any remaining cells
    for y in range(input_grid.shape[0]):
      for x in range(input_grid.shape[1]):
        if input_grid[y,x] not in [1,2]:
          output_grid[y,x] = input_grid[y,x]

    return output_grid