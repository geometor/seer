"""
1.  **Identify the "seed":** Find the vertical line of orange (color 7) pixels. This is our primary object.
2.  **Create the alternating pattern:** Starting from the "seed" line, extend outwards, alternating between azure (8) and orange (7) pixels.
3.  **Extend to edges:** Continue the alternating pattern until the edges of the grid are reached, both horizontally and vertically. The orange pixels of the seed line are included as part of the alternating sequence. The result uses only the color of the "seed" (orange), and azure.
"""

import numpy as np

def find_orange_line(grid):
    """Finds the vertical line of orange (7) pixels."""
    rows, cols = grid.shape
    for j in range(cols):
        # Check if the entire column is orange (7)
        if np.all(grid[:, j] == 7):
            return j  # Return the column index
    return -1  # Return -1 if no orange line is found


def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the orange line
    orange_line_col = find_orange_line(input_grid)

    if orange_line_col == -1:
        return output_grid # if no seed, return all zeros.

    # Create the alternating pattern
    for i in range(rows):
        for j in range(cols):
            # Calculate the distance from the orange line
            distance = abs(j - orange_line_col)
            
            # Alternate between azure (8) and orange (7)
            if (distance % 2) == 0:
                output_grid[i, j] = 7  # Orange
            else:
                output_grid[i, j] = 8  # Azure
    return output_grid