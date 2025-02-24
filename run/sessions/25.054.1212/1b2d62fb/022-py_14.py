"""
1.  **Find the Central Column:** Scan the input grid to find a column where *all* pixels are azure (8). This is the "central column." If no such column is found, return an all white grid that matches the dimensions of the input grid.
2.  **Create Output Grid:** Create a new grid with the same number of rows as the input grid and 3 columns. Fill this new grid with white (0) pixels.
3.  **Copy Central Column:** If the central column was found, copy the entire central column from the input grid to the second (middle) column of the output grid.
4.  **Copy Adjacent Azure Pixels:** Iterate through all rows of the input grid:
      *   If the found "central column" is not at index 0, check the pixel to the *left* of the central column in the input grid. If it's azure (8), copy it to the corresponding position in the *first* column of the output grid.
      *    If the found "central column" is not at the last index, check the pixel to the *right* of the central column in the input grid. If it's azure (8), copy it to the corresponding position in the *third* column of the output grid.
5. **Return Output Grid** return the output grid.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find the column index of the vertical line of the specified color.
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1  # Return -1 if no such line is found.

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the column with the vertical line of 8s.
    center_col = find_vertical_line(input_grid, 8)

    # Initialize the output grid as all zeros (white).
    output_grid = np.zeros((rows, 3), dtype=int)

    if center_col != -1:
        # copy central column
        for i in range(rows):
            output_grid[i,1] = input_grid[i,center_col]

        # copy horizontally adjancent cells
        for i in range(rows):
            if center_col > 0 and input_grid[i,center_col-1] == 8:
                output_grid[i,0] = 8
            if center_col < cols-1 and input_grid[i, center_col+1] == 8:
                output_grid[i,2] = 8
    else:
      return np.zeros((rows,cols), dtype=int).tolist()


    return output_grid.tolist()