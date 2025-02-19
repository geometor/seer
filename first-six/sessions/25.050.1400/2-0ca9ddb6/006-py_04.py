"""
The transformation rule operates on each non-white cell in the input grid. If a cell is red (color 2), its immediate orthogonal neighbors (up, down, left, right) in the output grid are changed to yellow (color 4). If a cell is blue (color 1), its immediate orthogonal neighbors are changed to orange (color 7). Other cells, including magenta (color 6) and azure (color 8), and their neighbors remain unchanged. The original red and blue cells also remain unchanged.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels
    for i in range(rows):
        for j in range(cols):
            # Process only red and blue cells
            if input_grid[i, j] == 2:  # Red cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                        output_grid[r, c] = 4  # Set to yellow
            elif input_grid[i, j] == 1:  # Blue cell
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if 0 <= r < rows and 0 <= c < cols:  # Check boundaries
                        output_grid[r, c] = 7  # Set to orange

    return output_grid