"""
The transformation rule involves preserving the original single-cell objects and introducing new objects of different colors around them in specific patterns. Yellow cells surround the red cell in diagonal directions, and orange cells form a cross centered on blue cell. Gray cell is preserved.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Iterate through the input grid to find the single-cell objects
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            # Check for the red cell (color 2)
            if input_grid[i, j] == 2:
                # Place yellow cells (color 4) around the red cell
                if i > 0 and j > 0:
                    output_grid[i - 1, j - 1] = 4
                if i > 0 and j < input_grid.shape[1] - 1:
                    output_grid[i - 1, j + 1] = 4
                if i < input_grid.shape[0] - 1 and j > 0:
                    output_grid[i + 1, j - 1] = 4
                if i < input_grid.shape[0] - 1 and j < input_grid.shape[1] - 1:
                    output_grid[i + 1, j + 1] = 4

            # Check for the blue cell (color 1)
            if input_grid[i, j] == 1:
                # Place orange cells (color 7) in cross shape around blue
                if i > 0:
                    output_grid[i-1, j] = 7
                if j > 0:
                    output_grid[i, j-1] = 7
                if j < input_grid.shape[1] -1:
                    output_grid[i, j+1] = 7
                if i < input_grid.shape[0] -1:
                    output_grid[i+1, j] = 7

    return output_grid