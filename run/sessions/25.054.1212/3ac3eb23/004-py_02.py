"""
Copies the input grid and iteratively adds a pixel of the same color below each colored pixel until no new pixels are added.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    changed = True

    while changed:
        changed = False
        temp_grid = np.copy(output_grid)  # Work on a copy to avoid immediate self-replication
        for row in range(rows):
            for col in range(cols):
                # Check if the current pixel is not background and the space below is background and exists
                if temp_grid[row, col] != 0 and row + 1 < rows and output_grid[row + 1, col] == 0:
                    output_grid[row + 1, col] = temp_grid[row, col]
                    changed = True  # Mark that a change occurred

    return output_grid