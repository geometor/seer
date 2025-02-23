"""
1.  **Identify Original Colored Pixels:** Iterate through each cell of the input grid. Note the color and position of any non-white pixels.
2.  **Preserve Original Colors:** The output grid starts as a copy of the input grid.  This ensures all original non-white pixels are maintained.
3.  **Conditional Expansion:** For each *white* (0) pixel in the output grid:
    *   Check its immediate neighbors (up, down, left, and right, but *not* diagonally).
    *   If a neighbor is red (2), change the white pixel to yellow (4).
    *   If a neighbor is blue (1), change the white pixel to orange (7).
    *   If a neighbor is magenta(6) do nothing.
4. Output the final grid
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell (up, down, left, right)."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the expansion rules."""
    output_grid = np.copy(input_grid)  # Start with a copy to preserve original colors
    rows, cols = input_grid.shape

    # Iterate through each cell in the *output* grid
    for row in range(rows):
        for col in range(cols):
            # Only consider white pixels for expansion
            if output_grid[row, col] == 0:
                neighbors = get_neighbors(input_grid, row, col)
                for n_row, n_col in neighbors:
                    neighbor_color = input_grid[n_row, n_col]
                    # Conditional expansion based on neighbor's color
                    if neighbor_color == 2:  # Red neighbor
                        output_grid[row, col] = 4  # Change to yellow
                        break  # Stop after the first expansion color is applied
                    elif neighbor_color == 1:  # Blue neighbor
                        output_grid[row, col] = 7  # Change to orange
                        break  # Stop after the first expansion color is applied

    return output_grid