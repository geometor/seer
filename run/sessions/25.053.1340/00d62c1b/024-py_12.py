"""
1.  **Find Green Regions:** Identify all contiguous regions of green (3) pixels in the input grid.  Contiguous pixels are connected horizontally or vertically (not diagonally).

2.  **Select Largest:** Determine the largest of these green regions based on the number of pixels it contains.

3.  **Define Interior (4-Neighbor Rule):** A pixel is considered "interior" if:
    *   It is part of the largest green region.
    *   All four of its immediate neighbors (up, down, left, and right) are also pixels *within the same largest green region*.

4.  **Recolor Interior:** Change the color of the identified interior pixels within the largest green region from green (3) to yellow (4).

5.  **Output:** The resulting grid is the output.  Pixels outside the largest green region remain unchanged.
"""

import numpy as np

def _find_contiguous_regions(grid, color):
    """Finds all contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def _dfs(row, col, region):
        """Depth-first search to explore a contiguous region."""
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
        region.append((row, col))
        _dfs(row + 1, col, region)
        _dfs(row - 1, col, region)
        _dfs(row, col + 1, region)
        _dfs(row, col - 1, region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                region = []
                _dfs(row, col, region)
                regions.append(region)
    return regions

def _find_interior_pixels(grid, region):
    """Finds interior pixels using the 4-neighbor rule."""
    interior_pixels = []
    region_set = set(region)  # Convert to set for efficient lookup

    for row, col in region:
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]
        is_interior = True
        for neighbor_row, neighbor_col in neighbors:
            if (neighbor_row, neighbor_col) not in region_set:
                is_interior = False
                break
        if is_interior:
            interior_pixels.append((row, col))
    return interior_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    
    # 1. Find Green Regions
    regions = _find_contiguous_regions(input_grid, 3)
    if not regions:
      return output_grid
    
    # 2. Select Largest
    largest_region = max(regions, key=len)
    
    # 3. Define and Find Interior Pixels (4-Neighbor Rule)
    interior_pixels = _find_interior_pixels(input_grid, largest_region)

    # 4. Recolor Interior
    for row, col in interior_pixels:
        output_grid[row, col] = 4
    
    return output_grid