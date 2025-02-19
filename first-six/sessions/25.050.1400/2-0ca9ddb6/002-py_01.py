"""
The transformation process operates on each non-white cell in the input grid independently. For every non-white cell, we identify its color. If the cell is red (color 2), its orthogonal neighbors (up, down, left, right) in the output grid are turned yellow (color 4). If the cell is blue (color 1), its orthogonal neighbors in the output grid are turned orange (color 7).  The original non-white cells and any white cells that are not neighbors of these colored cells remain unchanged in the output grid. Essentially, each colored cell in the input grid "emanates" a specific color to its immediate surroundings in the output grid, based on its own color.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    - Red (2) cells cause their orthogonal neighbors to become yellow (4).
    - Blue (1) cells cause their orthogonal neighbors to become orange (7).
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the input grid
    for i in range(rows):
        for j in range(cols):
            # Process only non-white cells
            if input_grid[i, j] != 0:
                # Define orthogonal neighbors
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

                # Change neighbor colors based on the current cell's color
                if input_grid[i, j] == 2:  # Red cell
                    for r, c in neighbors:
                        if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                            output_grid[r, c] = 4  # Set to yellow
                elif input_grid[i, j] == 1:  # Blue cell
                    for r, c in neighbors:
                        if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                            output_grid[r, c] = 7  # Set to orange

    return output_grid