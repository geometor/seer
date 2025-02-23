"""
1.  **Copy Grid:** Create a copy of the input grid. This copy will be modified to become the output grid.
2.  **Iterative Expansion:** Repeat the following steps until no more changes occur:
    *   Iterate through each cell of the *output* grid.
    *   For each *white* (0) pixel:
        *   Examine its immediate neighbors (up, down, left, and right).
        *   If any neighbor is red (2), change the white pixel to yellow (4).
        *   If any neighbor is blue (1), change the white pixel to orange (7).
        *   If a neighbor is not 0, 1, 2, or 6, it will not propagate an expansion
        *   If all neighbors are 0 or the colors of the transformation, do not perform the expansion.
3.  **Output:** The modified copy of the grid is the final output. The key improvement is iterative expansion which continues until no more white pixels can be changed.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell (up, down, left, right)."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col, grid[row-1, col]))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col, grid[row+1, col]))  # Down
    if col > 0:
        neighbors.append((row, col - 1, grid[row, col-1]))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1, grid[row, col+1]))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the iterative expansion rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    changes_made = True

    while changes_made:
        changes_made = False
        next_grid = np.copy(output_grid)  # Work on a copy for each iteration

        for row in range(rows):
            for col in range(cols):
                if output_grid[row, col] == 0:
                    neighbors = get_neighbors(output_grid, row, col)
                    neighbor_colors = [color for _, _, color in neighbors]
                    
                    if any(c in neighbor_colors for c in [3,5,8,9,7,4]):
                        continue

                    if 2 in neighbor_colors:
                        next_grid[row, col] = 4
                        changes_made = True
                    elif 1 in neighbor_colors:
                        next_grid[row, col] = 7
                        changes_made = True

        output_grid = next_grid  # Update for the next iteration

    return output_grid