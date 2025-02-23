"""
The transformation erodes non-blue (non-1) regions adjacent to white (0) regions in the input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by removing non-blue (non-1) pixels that are adjacent to white (0) pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is not blue (1)
            if input_grid[r, c] != 1:
                # Check for adjacent white (0) pixels
                is_adjacent_to_zero = False
                for i in range(max(0, r - 1), min(rows, r + 2)):
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        if input_grid[i, j] == 0:
                            is_adjacent_to_zero = True
                            break
                    if is_adjacent_to_zero:
                        break
                # If adjacent to zero, set the output pixel to blue(1)
                if is_adjacent_to_zero:
                    output_grid[r, c] = 1

    return output_grid