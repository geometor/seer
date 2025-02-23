# 00d62c1b • 022 • refine_coder

---
```python
"""
1.  **Find Green Regions:** Identify all contiguous regions of green (3) pixels in the input grid.  Contiguous pixels are connected horizontally or vertically (not diagonally).

2.  **Select Largest:** Determine the largest of these green regions based on the number of pixels it contains.

3.  **Define Interior (Bounding Box Method):**  Find the bounding box of the largest green region. This is the smallest rectangle (defined by min/max row and min/max column) that completely encloses the region.  A pixel is considered "interior" if:
    *   It is part of the largest green region.
    *   It is *not* on the edge of the bounding box.  That is, its row is not the minimum or maximum row *of the region*, AND its column is not the minimum or maximum column *of the region*.

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

def _find_interior_pixels(region):
    """Finds interior pixels using the bounding box method."""
    if not region:
        return []

    rows, cols = zip(*region)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    interior_pixels = []
    for row, col in region:
        if min_row < row < max_row and min_col < col < max_col:
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
    
    # 3. Define and Find Interior Pixels (Bounding Box)
    interior_pixels = _find_interior_pixels(largest_region)

    # 4. Recolor Interior
    for row, col in interior_pixels:
        output_grid[row, col] = 4
    
    return output_grid
```

