"""
1.  **Identify the Green Shape:** Locate the contiguous region of pixels with the value '3' (green). This forms the primary object.

2.  **Fill Interior with Yellow:** change to the colour yellow (4) all green pixels adjacent to white background pixels.

3  **Leave Background Unchanged:** Maintain all the white pixels.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds all contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, current_region):
        """Depth-first search to find contiguous pixels."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        current_region.append((row, col))
        dfs(row + 1, col, current_region)
        dfs(row - 1, col, current_region)
        dfs(row, col + 1, current_region)
        dfs(row, col - 1, current_region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)
    return regions

def is_adjacent_to_color(grid, row, col, color):
    """Checks if a cell is adjacent to a cell of a specified color."""
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if (
                0 <= nr < grid.shape[0]
                and 0 <= nc < grid.shape[1]
                and grid[nr, nc] == color
            ):
                return True
    return False

def transform(input_grid):
    """Transforms the input grid by filling the interior of green shapes with yellow."""
    output_grid = input_grid.copy()
    green_regions = find_contiguous_regions(input_grid, 3) #find green regions

    for region in green_regions:
        for row, col in region:
            if is_adjacent_to_color(input_grid, row, col, 0): # Check for adjacency to white (0)
              output_grid[row, col] = 4

    return output_grid