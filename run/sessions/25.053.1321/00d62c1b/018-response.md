# 00d62c1b • 018 • example_3 - CODE

---
```python
"""
1.  **Identify the Input Object:** The input is a 10x10 grid of pixels, where each pixel has a color value (0 or 3 in the input, with 0, 3, and 4 in the output).

2.  **Locate the Region of Interest:** Find the largest contiguous region of green (3) pixels.

3. **Identify inner region**: Locate the set of pixels such that at least two pixels on opposite sides (vertical or horizontal) are the same color.

4.  **Transform the Region:** Change the color of the central pixels from green (3) to yellow (4). The central area are the green colored shapes that form an enclosed shape with a single open area of at least two green squares in horizontal and vertical directions.

5.  **Output:** Return the modified grid, now containing colors to 0, 3, and 4.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a specific color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col):
        """Depth-first search to explore a contiguous region."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return []

        visited[row, col] = True
        region = [(row, col)]

        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] == color:
                regions.append(dfs(row, col))

    return regions

def is_enclosed(grid, region, color):
    """
    Checks the identified region for a contiguous shape to change to color 4.
    """
    rows = [r for r, _ in region]
    cols = [c for _, c in region]
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    
    inner_region = []
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r,c) in region:
                # check up, down, left, right
                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                
                same_color_count = 0
                for nr, nc in neighbors:
                    if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and grid[nr, nc] == color:
                        same_color_count +=1

                if same_color_count >= 2:
                    inner_region.append((r,c))
    return inner_region

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # identify green regions
    green_regions = find_contiguous_regions(output_grid, 3)
    
    # identify largest green region (not necessary for example, helpful for generalization)
    # largest_green_region = max(green_regions, key=len, default=[])
    
    
    # check enclosure
    for region in green_regions:
        inner_region = is_enclosed(output_grid, region, 3)
        # paint inner region
        for row, col in inner_region:
            output_grid[row, col] = 4
    
    return output_grid
```
