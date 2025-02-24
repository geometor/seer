"""
Transforms an input grid, changing some red pixels (2) to yellow (4) based on adjacency. A red pixel changes to yellow if it has at least one orthogonally adjacent white pixel (0) and at least one orthogonally adjacent red pixel (2). The transformation happens iteratively until no more changes occur.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the adjacency rules, iteratively.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    def is_valid(r, c):
        """Checks if the given row and column are within grid bounds."""
        return 0 <= r < rows and 0 <= c < cols

    def get_adjacent_colors(r, c, grid):
        """Gets the colors of orthogonally adjacent cells."""
        adjacent_colors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Right, Left, Down, Up
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                adjacent_colors.append(grid[nr, nc])
        return adjacent_colors

    while True:
        changed = False  # Flag to track if any changes were made in this iteration
        temp_grid = np.copy(output_grid) # Work on a copy to avoid immediate cascading during iteration

        for r in range(rows):
            for c in range(cols):
                if temp_grid[r, c] == 2:  # Check if the cell is red in temp_grid
                    adjacent_colors = get_adjacent_colors(r, c, temp_grid)
                    has_white_neighbor = 0 in adjacent_colors
                    has_red_neighbor = 2 in adjacent_colors

                    if has_white_neighbor and has_red_neighbor:
                        output_grid[r, c] = 4  # Change to yellow in the output_grid
                        changed = True

        if not changed:  # If no changes were made, break the loop
            break

    return output_grid