"""
1.  **Copy:** Create a copy of the input grid.  This copy will be the output grid.
2.  **Iterative Expansion:** Repeat the following steps until no more white pixels can be changed:
    *   Iterate through each cell of the *output* grid.
    *   For each *white* (0) pixel:
        *   Examine its immediate neighbors (up, down, left, and right).
        *   If a neighbor is not 0, 1, or 2, skip this pixel.
        *   If any neighbor is red (2), change the white pixel to yellow (4).
        *   If any neighbor is blue (1), change the white pixel to orange (7).
3. **Output**: The updated grid copy is the result.
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
    # initialize output_grid
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

                    # If a neighbor is not 0, 1, or 2, skip this pixel.
                    if any(c not in [0, 1, 2] for c in neighbor_colors):
                        continue
                    
                    # If any neighbor is red (2), change the white pixel to yellow (4).
                    if 2 in neighbor_colors:
                        next_grid[row, col] = 4
                        changes_made = True
                    # If any neighbor is blue (1), change the white pixel to orange (7).
                    elif 1 in neighbor_colors:
                        next_grid[row, col] = 7
                        changes_made = True

        output_grid = next_grid  # Update for the next iteration

    return output_grid