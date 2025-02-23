"""
1.  **Identify Center Column:** Find the vertical column in the input grid that contains a contiguous line of blue (1) pixels. This is the center column.
2.  **Examine Adjacent Pixels**: Inspect the pixels directly to the right of the blue (1) vertical line.
3.  **Build output**: Use the adjacent pixels to the right of the blue to
    determine a 5x3 region
    - The output is always 5x3
    - if the pixel to the right of the vertical blue line is 9, the output has an
      azure in that position
    - if the pixel to the right of the vertical blue line is 0, the output has a
      black in that position
    - Change all blue pixels to azure.

4.  **Output:** The resulting 5x3 region.
"""

import numpy as np

def find_blue_line_center_and_neighbors(grid):
    # Find the column indices where blue (1) forms a vertical line and the neighbors to its right.
    rows, cols = grid.shape
    neighbors = []
    center_col = -1
    for j in range(cols):
        for i in range(rows):
            if grid[i,j] == 1:
                if all(grid[k, j] == 1 for k in range(i, rows) if k < rows):
                    center_col = j
                    for row_index in range(rows) :
                      if j + 1 < cols:
                        neighbors.append((row_index, grid[row_index, j+1]))
                      else:
                        neighbors.append((row_index, 0)) # use background is out of bounds
                    return center_col, neighbors
    return center_col, neighbors

def transform(input_grid):
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)

    # Find the central feature (vertical blue line)
    center_col, neighbors = find_blue_line_center_and_neighbors(input_grid)
    
    # Create output grid initialized with zeros
    output_grid = np.zeros((5, 3), dtype=int)

    # if no blue, return all black
    if center_col == -1:
      return output_grid.tolist()

    # fill in the output grid, using relative position
    row_offset = 0
    for row_index, val in neighbors:
      if row_index < 5:
        if val == 9:  # rules show 9 maps to azure
          output_grid[row_index, 1] = 8 # center
        if center_col + 1 < input_grid.shape[1]: # only fill if valid
            if input_grid[row_index, center_col] == 1:
              output_grid[row_index, 1] = 8 # center gets azure

    return output_grid.tolist()