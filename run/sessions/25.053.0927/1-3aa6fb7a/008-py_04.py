"""
1.  **Identify '8's:** Locate all pixels with the value '8' (azure) in the input grid.
2.  **Group '8's:** Group contiguous '8' pixels. Two '8' pixels are considered contiguous if they are adjacent horizontally or vertically.  Diagonally adjacent '8' pixels will be in separate groups.
3.  **Place '1's:** For each group of '8's, going left to right of the westernmost 8s of each group, place a '1' (blue) pixel immediately to the west (left) of the westernmost '8' pixel in that group, if there is a 0. If no 0 to the west, no 1 is placed.
"""

import numpy as np

def find_groups(grid, value):
    """Finds groups of contiguous pixels with the given value."""
    groups = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(row, col):
        """Checks if a cell is within bounds and not visited."""
        return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

    def dfs(row, col, current_group):
        """Performs Depth-First Search to find contiguous pixels."""
        if not is_valid(row, col) or visited[row, col] or grid[row, col] != value:
            return

        visited[row, col] = True
        current_group.append((row, col))

        # Check adjacent cells (up, down, left, right)
        dfs(row + 1, col, current_group)
        dfs(row - 1, col, current_group)
        dfs(row, col + 1, current_group)
        dfs(row, col - 1, current_group)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == value and not visited[row, col]:
                current_group = []
                dfs(row, col, current_group)
                groups.append(current_group)

    return groups

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    groups_of_8 = find_groups(input_grid, 8)

    for group in groups_of_8:
        # Find the westernmost (leftmost) '8' in the group
        westernmost_8 = min(group, key=lambda x: x[1])

        # Place '1' to the west if there's a '0'
        west_col = westernmost_8[1] - 1
        if west_col >= 0 and input_grid[westernmost_8[0], west_col] == 0:
             output_grid[westernmost_8[0], west_col] = 1

    return output_grid