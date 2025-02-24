"""
1. Identify Target Color: Examine the input grid and determine color that makes up the output 2x2.
2. Create Output Grid: Create a 2x2 grid.
3. Fill the grid with solid target color: All cells of the grid must be filled with the color found in step 1.
4. Return the new grid.
"""

import numpy as np

def find_target_color(grid):
    # Iterate through the grid to find a 2x2 block of the same color
    grid = np.array(grid)
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Check if a 2x2 block has the same color
            if (grid[i, j] == grid[i + 1, j] ==
                grid[i, j + 1] == grid[i + 1, j + 1]):
                return grid[i, j]
    return None  # No 2x2 block found


def transform(input_grid):
    # Find the target color which forms solid 2x2 block
    target_color = find_target_color(input_grid)

    # Handle the case where no target color is found
    if target_color is None:
        return [[]] # or return input_grid ?

    # Create a 2x2 grid filled with the target color
    output_grid = np.full((2, 2), target_color, dtype=int)

    return output_grid.tolist()