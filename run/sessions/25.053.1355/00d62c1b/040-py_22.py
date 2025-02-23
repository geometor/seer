"""
1.  **Identify Green Shapes:** Find all contiguous regions of green (3) pixels. These constitute the "green shapes."

2.  **Identify Boundaries:** For each green shape, find its boundary pixels. A boundary pixel is a green pixel that is directly adjacent (up, down, left, or right) to a non-green pixel (the background, color 0).

3. **Identify Interior:** For each green shape, identify the interior pixels. An interior pixel is any pixel that meets all these criteria:
    *   it is color 3 (green)
    *   it is not a boundary pixel
    *   it can be reached from another interior or boundary pixel by a path composed only of color 3 pixels

4.  **Fill Interior:** Change the color of all identified interior pixels to yellow (4).

5.  **Preserve Background:** All pixels that are not part of a green shape's interior (i.e., the background and any other non-green, non-interior pixels) remain unchanged.
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

def find_boundary_pixels(grid, region):
    """Finds boundary pixels of a region (adjacent to a different color)."""
    boundary = []
    for r, c in region:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < grid.shape[0]
                and 0 <= nc < grid.shape[1]
                and grid[nr, nc] != 3
            ):
                boundary.append((r, c))
                break  # Once a neighbor of a different color is found, it's a boundary
    return boundary

def find_interior_pixels(grid, region, boundary):
    """
    Finds interior pixels of region bounded by the boundary.
    Interior pixels are the green pixels that are not boundary pixels.
    """
    
    interior = []

    for r, c in region:
        if (r,c) not in boundary:
            interior.append((r,c))
    
    return interior

def transform(input_grid):
    """Transforms the input grid by filling the interior of green shapes with yellow."""
    output_grid = input_grid.copy()
    green_regions = find_contiguous_regions(input_grid, 3)  # Find green shapes

    for region in green_regions:
        boundary = find_boundary_pixels(input_grid, region) # identify boundary
        interior = find_interior_pixels(input_grid, region, boundary) # find interior

        for r, c in interior:
            output_grid[r,c] = 4

    return output_grid