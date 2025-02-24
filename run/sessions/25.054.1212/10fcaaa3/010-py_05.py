"""
1.  **Expansion:** Create a new grid with double the height and width of the original grid.
2.  **Copy and Mirror Horizontally:** Copy every colored pixel (not black or white) from the input grid to the corresponding location in the new grid, and then mirror the pixel horizontally to the right side.
3.  **Azure Vertical Highlight:** In the top half of the expanded grid, add a vertical azure line on each side of *every* colored (non-black) column.
4.  **Azure Horizontal Separation:** Add a horizontal line of azure pixels across the entire width of the grid, dividing it exactly in half.
5.  **Mirror Vertically:** Mirror the top half of the grid (above the horizontal azure line) to the bottom half (below the azure line). The azure line should be at the last row index for the bottom half.
"""

import numpy as np

def get_colored_columns(grid):
    """Finds the indices of columns containing colored (non-black, non-white) pixels."""
    height, width = grid.shape
    colored_cols = []
    for j in range(width):
        for i in range(height):
            if grid[i, j] != 0 and grid[i,j] != 8:  # Not black, and not azure
                colored_cols.append(j)
                break  # Move to the next column
    return colored_cols

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Copy and Mirror Horizontally
    for i in range(input_height):
        for j in range(input_width):
            if input_grid[i, j] != 0:  # Copy all colors except background
                output_grid[i, j] = input_grid[i, j]
                output_grid[i, output_width - 1 - j] = input_grid[i, j]

    # Azure Vertical Highlight
    colored_cols = get_colored_columns(output_grid[:input_height,:])

    for col in colored_cols:
        if col > 0 :
          for i in range(input_height):
            output_grid[i, col - 1] = 8
        if col < output_width-1:
          for i in range(input_height):
            output_grid[i, col + 1] = 8

    # Azure Horizontal Separation
    output_grid[input_height, :] = 8

    # Mirror Vertically
    for i in range(input_height):
        for j in range(output_width):
            output_grid[output_height - 1 - i, j] = output_grid[i, j]

    return output_grid