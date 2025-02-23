# 00d62c1b • 018 • example_3 - CODE

---
```python
"""
1. **Identify the Shape:** Locate the largest contiguous region of pixels with the value '3' (green) within the input grid. Contiguous means connected horizontally or vertically.
2. **Find Interior Pixels:** Within the identified shape, determine the "interior" pixels. A pixel is considered "interior" if it's part of the shape (value '3') and is surrounded on all four sides (up, down, left, right) by other pixels that are also part of the shape. It may be useful to think of this as the inverse flood-fill from the outer edge using the same color.
3. **Recolor Interior:** Change the color value of all identified interior pixels from '3' (green) to '4' (yellow).
4. **Output:** The resulting grid, with the interior of the shape recolored, is the output.
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
    """Finds the interior pixels of a given region."""
    interior_pixels = []
    for row, col in region:
        # Check if surrounded by same color on all 4 sides
        is_interior = True
        neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        for n_row, n_col in neighbors:
            if (n_row < 0 or n_row >= grid.shape[0] or
                n_col < 0 or n_col >= grid.shape[1] or
                grid[n_row, n_col] != grid[row, col]):
                is_interior = False
                break
        if is_interior:
            interior_pixels.append((row, col))
    return interior_pixels
    

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = input_grid.copy()
    
    # 1. Identify the Shape (largest contiguous region of color 3)
    regions = _find_contiguous_regions(input_grid, 3)
    if not regions:
      return output_grid
    
    largest_region = max(regions, key=len)

    # 2. Find Interior Pixels
    interior_pixels = _find_interior_pixels(input_grid, largest_region)

    # 3. Recolor Interior
    for row, col in interior_pixels:
        output_grid[row, col] = 4

    return output_grid
```
