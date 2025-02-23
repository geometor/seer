"""
1.  **Locate azure areas:** Identify all contiguous regions of color '8' (azure).
2.  **Locate red areas:** Identify regions of color '2'(red).
3.  **Locate white regions** Identify the regions of color '0'(white).
4.  **Conditional Replacement**: find the position of white '0' inside of the red '2' area, and keep the '0' at those positions in the final grid. All the other areas remain the same.
"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions of the specified color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col):
        """Depth-first search to find connected components."""
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                objects.append(dfs(row, col))
    return objects


def transform(input_grid):
    """Transforms the input grid based on the observed rules."""

    # initialize output_grid with copy of input grid
    output_grid = np.copy(input_grid)

    # Find objects of color 2 (red)
    red_objects = find_objects(input_grid, 2)
    # Find objects of color 0(white)
    # white_objects = find_objects(input_grid, 0)  # Not used, but kept for clarity

    # Iterate over each red object
    for red_object in red_objects:
        # get bounding box
        min_row = min(r for r, c in red_object)
        max_row = max(r for r, c in red_object)
        min_col = min(c for r, c in red_object)
        max_col = max(c for r, c in red_object)

        # Iterate over potential interior, check the color, if white, continue
        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if (r, c) in red_object:
                    continue #skip check for cells within red object
                if output_grid[r,c] == 0:
                    continue
                else:
                  output_grid[r,c] = input_grid[r,c]
    return output_grid