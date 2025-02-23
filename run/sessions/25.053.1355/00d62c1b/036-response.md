# 00d62c1b • 036 • refine_coder

---
```python
"""
1.  **Identify Green Shapes:** Locate all contiguous regions of green (3) pixels. These regions constitute the "green shapes."

2.  **Define Interior:** Within each green shape, define "interior" pixels as those green pixels that are completely surrounded by either other green pixels or yellow pixels that have already been filled. Consider that at the start all other green cells count as surrounding.

3.  **Iterative Interior Filling:** Iteratively fill the interior of each green shape with yellow (4). Start from the green pixels that do not have white neighbours and are fully surround by green. This process should be repeated until no more green pixels within a shape meet the "interior" criteria.

4.  **Preserve Background:**  All pixels that are not part of a green shape's interior should remain unchanged.
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

def is_interior(grid, row, col, filled):
    """Checks if a green pixel is an interior pixel."""
    if grid[row,col] != 3:
        return False

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if (
                0 <= nr < grid.shape[0]
                and 0 <= nc < grid.shape[1]
                and grid[nr, nc] != 3
                and (nr,nc) not in filled
                and grid[nr,nc] != 4
            ):
                return False  # Found a neighbor that is not green or yellow (filled)
    return True

def transform(input_grid):
    """Transforms the input grid by filling the interior of green shapes with yellow."""
    output_grid = input_grid.copy()
    green_regions = find_contiguous_regions(input_grid, 3)  # Find green shapes
    filled = set()

    for region in green_regions:
        changed = True
        while changed:  # Iterate until no more interior pixels are found
            changed = False
            pixels_to_fill = []

            for row, col in region:
                if (row, col) not in filled and is_interior(output_grid, row, col, filled):
                    pixels_to_fill.append((row, col))

            for row, col in pixels_to_fill:
                output_grid[row, col] = 4  # Fill with yellow
                filled.add((row,col))
                changed = True


    return output_grid
```
