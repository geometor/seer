# 00d62c1b • 016 • refine_coder

---
```python
"""
Identifies contiguous regions of green (3) pixels within the input grid.
Changes the color of interior green pixels to yellow (4). An interior
pixel is defined as a green pixel that has 8 green neighbors (8-connectivity).
All other pixels remain unchanged.
"""

import numpy as np

def get_contiguous_regions(grid, color):
    """
    Finds all contiguous regions of a given color in the grid.
    Uses a depth-first search (DFS) approach.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = []

    def dfs(r, c, current_region):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != color:
            return
        visited.add((r, c))
        current_region.append((r, c))
        # Explore all 8 neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == color and (r, c) not in visited:
                current_region = []
                dfs(r, c, current_region)
                regions.append(current_region)
    return regions

def is_interior(grid, r, c, color):
    """
    Checks if a pixel at (r, c) is an interior pixel of a given color.
    An interior pixel has 8 neighbors of the same color (8-connectivity).
    """
    rows, cols = len(grid), len(grid[0])
    neighbor_count = 0
    # Check all 8 neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == color:
                neighbor_count += 1

    return neighbor_count == 8  # 8-connectivity

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = len(output_grid), len(output_grid[0])

    # Identify green regions
    green_regions = get_contiguous_regions(output_grid, 3)

    # Find interior pixels and change their color
    for region in green_regions:
        for r, c in region:
            if is_interior(output_grid, r, c, 3):
                output_grid[r][c] = 4

    return output_grid
```
