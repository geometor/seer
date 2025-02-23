"""
1.  **Identify the blue line:** Locate the vertical line of blue (1) pixels in the input grid. In this instance there is a single complete vertical line.
2.  **Crop the grid:** Extract a section of the input grid. The cropped section consists of three columns: The column to the left of the blue line and the two columns to the right. The height of the cropped section should be the height of the original section.
3.  **Change Colors**: Transform the pixels that were blue (1) to be azure(8). Leave all other pixel in the cropped section as color 0.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find columns where all elements are of the specified color.
    rows, cols = grid.shape
    line_cols = []
    for j in range(cols):
        if all(grid[:, j] == color):
            line_cols.append(j)
    return line_cols

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the blue (1) vertical line
    blue_line_cols = find_vertical_line(input_grid, 1)

    # Handle case where no blue line is found or multiple
    if not blue_line_cols:
        return np.zeros((rows, 3), dtype=int).tolist()
        
    blue_line_col = blue_line_cols[0]

    # Crop the grid
    start_col = max(0, blue_line_col - 1)
    end_col = min(cols, blue_line_col + 2)
    cropped_grid = input_grid[:, start_col:end_col]
    
    output_grid = np.zeros_like(cropped_grid)

    # change output pixels
    cropped_rows, cropped_cols = cropped_grid.shape
    for r in range (cropped_rows):
        for c in range(cropped_cols):
            if cropped_grid[r,c] == 1:
                output_grid[r,c] = 8

    return output_grid.tolist()