"""
1.  **Double Dimensions:** Create a new grid (output_grid) with twice the height and width of the original grid (input_grid).
2.  **Copy and Mirror Horizontally:** Copy every colored pixel (not black or azure) from the input grid to the corresponding location in the *top half* of the new grid, and then mirror the pixel horizontally to the right side *within the top half*.
3.  **Vertical Azure Highlight:** Add a vertical azure line on each side of the copied colored pixels in the *top half* of the output grid.
4.  **Horizontal Azure Separation:** Add a horizontal azure line across the entire width of the output grid, positioned at the row index equal to the original input grid's height.
5.  **Vertical Mirroring:** Mirror the top half of the grid (above the horizontal azure line) to the bottom half of the grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Copy and Mirror Horizontally (top half only)
    for i in range(input_height):
        for j in range(input_width):
            if input_grid[i, j] != 0 and input_grid[i,j] != 8:  # Not black or azure
                output_grid[i, j] = input_grid[i, j]
                output_grid[i, output_width - 1 - j] = input_grid[i, j]

    # Vertical Azure Highlight (top half only)
    for i in range(input_height):
        for j in range(output_width):
            if output_grid[i,j] != 0 and output_grid[i,j] != 8:
                if j > 0 and output_grid[i,j-1] == 0:
                    output_grid[i, j - 1] = 8
                if j < output_width - 1 and output_grid[i,j+1] == 0:
                    output_grid[i, j + 1] = 8

    # Horizontal Azure Separation
    output_grid[input_height, :] = 8

    # Vertical Mirroring (top half to bottom half)
    for i in range(input_height):
        for j in range(output_width):
            output_grid[output_height - 1 - i, j] = output_grid[i, j]

    return output_grid