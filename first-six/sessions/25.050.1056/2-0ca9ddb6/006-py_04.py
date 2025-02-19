"""
Transformation Rule: For each red (2) or blue (1) cell in the input grid, create a cross-shaped object of a corresponding color (yellow for red, orange for blue) centered on the original cell. The original red and blue cells are preserved. Other colored cells do not generate crosses and are kept unchanged. The size of the cross is one cell extending in each cardinal direction.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)  # Start with a copy of the input grid
    rows, cols = input_grid.shape

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the cell is red or blue
            if input_grid[r, c] == 2:  # Red cell
                cross_color = 4  # Yellow
            elif input_grid[r, c] == 1:  # Blue cell
                cross_color = 7  # Orange
            else:
                continue  # Skip if not red or blue

            # Create the cross by changing the neighboring cells
            if r > 0:
                output_grid[r - 1, c] = cross_color  # Up
            if r < rows - 1:
                output_grid[r + 1, c] = cross_color  # Down
            if c > 0:
                output_grid[r, c - 1] = cross_color  # Left
            if c < cols - 1:
                output_grid[r, c + 1] = cross_color  # Right

    return output_grid