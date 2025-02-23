# 32597951 • 017 • refine_coder

---
```python
"""
1.  **Identify Azure Regions:** Locate all contiguous horizontal lines or blocks of azure (color 8).
2.  **Change Adjacent Blue Pixels:** Find all blue (color 1) pixels that are *directly adjacent* (horizontally, vertically, or diagonally) to the azure regions identified in step 1.
3.  **Recolor to Green:** Change the color of the identified blue pixels from step 2 to green (color 3).
4. **All other pixels remain the same:** Preserve all colors in all other locations
"""

import numpy as np

def find_azure_regions(grid):
    # Find contiguous horizontal lines or blocks of azure (color 8).
    azure_regions = []
    rows, cols = grid.shape
    for r in range(rows):
        start_c = None
        for c in range(cols):
            if grid[r, c] == 8:
                if start_c is None:
                    start_c = c
            elif start_c is not None:
                azure_regions.append((r, range(start_c, c)))
                start_c = None
        if start_c is not None:
            azure_regions.append((r, range(start_c, cols)))
    return azure_regions

def get_adjacent_pixels(grid, row, col):
    # helper to find neighbors
    rows, cols = grid.shape
    adjacent = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                adjacent.append((nr, nc))
    return adjacent

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = input_grid.copy()
    rows, cols = output_grid.shape

    # Find azure regions
    azure_regions = find_azure_regions(input_grid)

    # Find blue pixels adjacent to azure regions and change them to green
    for r, col_range in azure_regions:
        for c in col_range:
          # check neighbors of each azure pixel
          for nr, nc in get_adjacent_pixels(input_grid, r, c):
              if input_grid[nr, nc] == 1:
                  output_grid[nr, nc] = 3

    return output_grid.tolist()
```
