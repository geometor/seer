"""
1.  **Extract Subgrid:** Find the central vertical column of the input grid (index = `width // 2`). Extract a 3-column-wide subgrid centered on this column. This includes the central column, one column to its left, and one to its right. All rows are included.
2.  **Recolor Center Column:** Iterate through each row of the extracted subgrid. If the pixel in the center column is blue (1), change its color to azure (8).
3.  **Recolor Side Columns:** Iterate through each row. If a pixel in the left or right column of the subgrid has is not black (0), change it to black(0).
4.  **Output:** The modified 3xN subgrid is the output.
"""

import numpy as np

def get_central_column_index(grid):
    """Helper function to find the index of the central column."""
    return grid.shape[1] // 2

def extract_subgrid(grid, center_col_index, width):
    """Helper function to extract a subgrid of specified width centered on a column."""
    start_col = max(0, center_col_index - width // 2)
    end_col = min(grid.shape[1], center_col_index + width // 2 + 1)
    return grid[:, start_col:end_col]


def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # 1. Locate Center and Extract Subgrid
    center_col_index = get_central_column_index(input_grid)
    subgrid = extract_subgrid(input_grid, center_col_index, 3)
    output_grid = subgrid.copy()

    # 2. Recolor Center Column
    center_sub = subgrid.shape[1] // 2
    for i in range(subgrid.shape[0]):
        if subgrid[i, center_sub] == 1:
            output_grid[i, center_sub] = 8

    # 3. Recolor Side Columns
    for i in range(subgrid.shape[0]):
        for j in [0, subgrid.shape[1]-1]:
          if subgrid[i, j] != 0:
            output_grid[i,j] = 0

    # 4. Output
    return output_grid.tolist()