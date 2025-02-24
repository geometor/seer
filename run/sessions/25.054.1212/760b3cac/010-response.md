# 760b3cac • 010 • refine_coder

---
```python
"""
1. Identify Azure Regions: Find all contiguous regions of azure (8) pixels in the input grid. A contiguous region is a group of one or more azure pixels directly adjacent horizontally or vertically.

2. Constrained Horizontal Expansion for each region:
   For each continuous block of azure pixels
        a. Expand the azure region to the left, one pixel at a time, replacing white (0) pixels with azure (8), until a non-white pixel or the grid edge is encountered.
       b. Expand the azure region to the right, one pixel at a time, replacing white (0) pixels with azure (8), until a non-white pixel or the grid edge is encountered.

3. Preserve Other Colors: Do not modify any pixels that are not part of the identified azure regions. Specifically, the yellow regions remain unchanged.

4. Row Limited Expansion: Only rows containing original azure pixels will contain azure pixels in the output.
"""

import numpy as np

def get_azure_regions(grid):
    """
    Identifies contiguous azure (8) regions in the grid.
    Returns a list of lists, where each inner list contains (row, col) tuples
    for a single contiguous azure region.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    azure_regions = []

    def dfs(r, c, current_region):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or visited[r, c]
            or grid[r, c] != 8
        ):
            return
        visited[r, c] = True
        current_region.append((r, c))
        # Check adjacent cells (up, down, left, right)
        dfs(r + 1, c, current_region)
        dfs(r - 1, c, current_region)
        dfs(r, c + 1, current_region)
        dfs(r, c - 1, current_region)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8 and not visited[r, c]:
                current_region = []
                dfs(r, c, current_region)
                azure_regions.append(current_region)
    return azure_regions

def expand_region_horizontally(grid, region):
    """
    Expands a single contiguous azure region horizontally, filling white (0)
    pixels, until blocked by other colors or grid edges.
    """
    output_grid = np.copy(grid)
    # find min and max row
    min_row = min(r for r, c in region)
    max_row = max(r for r,c in region)
    if min_row != max_row:
      print("Error region spans multiple rows")
      return output_grid
    row = min_row # region is only in 1 row

    # Get the horizontal bounds for expansion
    min_col = min(c for r, c in region)
    max_col = max(c for r, c in region)

    # Expand left
    c = min_col - 1
    while c >= 0 and output_grid[row, c] == 0:
        output_grid[row, c] = 8
        c -= 1

    # Expand Right
    c = max_col + 1
    while c < output_grid.shape[1] and output_grid[row, c] == 0:
        output_grid[row, c] = 8
        c += 1

    return output_grid
  

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # get azure regions
    azure_regions = get_azure_regions(output_grid)

    # expand each region horizontally,
    for region in azure_regions:
        output_grid = expand_region_horizontally(output_grid, region)
    return output_grid
```
