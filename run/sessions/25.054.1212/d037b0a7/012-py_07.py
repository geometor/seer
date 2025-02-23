"""
1.  **Downward Propagation:** Iterate through each cell of the grid. If a cell is white (0) and the cell directly above it has a different, non-zero color, set the current cell's color to the color of the cell above it. *Keep track of which cells are modified during this step.*

2.  **Conditional Rightward Fill:** Iterate through each cell of the grid again. If a cell was modified during the downward propagation step, examine the cells to its right. Fill any contiguous white (0) cells to the right with the modified cell's color. Stop filling when a non-white cell is encountered.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    modified_cells = set() # Keep track of modified cells

    # Iterate through each cell of the grid, applying the downward propagation rule.
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:  # If the current pixel is white
                if i > 0:  # Check if there's a row above
                    if output_grid[i - 1, j] != 0:  # If the pixel above is not white
                        output_grid[i, j] = output_grid[i - 1, j]  # Set color to the pixel above
                        modified_cells.add((i, j))  # Record the modification


    # Iterate through the grid again for conditional rightward fill
    for i in range(rows):
        for j in range(cols):
            if (i,j) in modified_cells:
                for k in range(j+1, cols):
                    if output_grid[i,k] == 0:
                        output_grid[i,k] = output_grid[i,j]
                    else:
                        break # stop when a non-white is encountered

    return output_grid