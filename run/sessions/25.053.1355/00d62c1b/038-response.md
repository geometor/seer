# 00d62c1b • 038 • refine_coder

---
```python
"""
1.  **Identify Green Shapes:** Find all contiguous regions of green (3) pixels. These are the "green shapes."

2.  **Identify Starting "Seeds":** The first "seed" will be pixels that are only surrounded by green pixels.

3.  **Iterative Interior Filling:**
    *   Seed Growth: Starting with the seed, expand outwards, filling adjacent green pixels. Consider the 'white' background to be a boundary.

4.  **Preserve Background:** All pixels that are not part of a green shape's interior remain unchanged.
"""

import numpy as np
from collections import deque

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

def find_seed_pixels(grid, region):
    """Finds initial seed pixels within a green region."""
    seeds = []
    for r, c in region:
        surrounded = True
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                if grid[nr, nc] != 3:
                    surrounded = False
                    break
            else:
                # Consider out-of-bounds as not surrounded
                surrounded = False
                break
        if surrounded:
            seeds.append((r,c))
    return seeds
            

def transform(input_grid):
    """Transforms the input grid by filling the interior of green shapes with yellow."""
    output_grid = input_grid.copy()
    green_regions = find_contiguous_regions(input_grid, 3)  # Find green shapes

    for region in green_regions:
        seeds = find_seed_pixels(input_grid, region)
        
        # use a queue for breadth first search style filling
        q = deque(seeds)

        filled = set(seeds)
        
        while q:
            r, c = q.popleft()
            output_grid[r,c] = 4 # fill with yellow

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < output_grid.shape[0] and 0 <= nc < output_grid.shape[1] and
                    output_grid[nr, nc] == 3 and (nr, nc) not in filled):
                    q.append((nr,nc))
                    filled.add((nr,nc))


    return output_grid
```
