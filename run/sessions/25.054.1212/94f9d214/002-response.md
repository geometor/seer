# 94f9d214 • 002 • example_1 • investigate_coder

---
```python
"""
The input grid is analyzed to identify the locations of regions bound by green and blue. The green color in the top left corner of those regions is converted to red in the output grid, which has different sizes that the input. All other pixels in output are white.
"""

import numpy as np

def find_regions(input_grid):
    """Find regions bounded by green (3) and blue (1)."""
    regions = []
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_region):
        if not is_valid(r, c) or visited[r, c] or (input_grid[r, c] != 3 and input_grid[r,c] != 1):
            return

        visited[r, c] = True
        current_region.append((r, c))

        # Explore adjacent cells
        dfs(r + 1, c, current_region)
        dfs(r - 1, c, current_region)
        dfs(r, c + 1, current_region)
        dfs(r, c - 1, current_region)


    for r in range(rows):
        for c in range(cols):
            if (input_grid[r,c] == 3 or input_grid[r,c] == 1) and not visited[r,c]:
                current_region = []
                dfs(r,c, current_region)
                if len(current_region) > 0:
                    greens = [pos for pos in current_region if input_grid[pos] == 3]
                    blues = [pos for pos in current_region if input_grid[pos] == 1]

                    if len(greens) >= 1 and len(blues) >=1:

                      # find top_left of green cluster
                      min_row = min(pos[0] for pos in greens)
                      min_col_at_min_row = min(pos[1] for pos in greens if pos[0] == min_row)

                      regions.append((min_row, min_col_at_min_row))

    return regions

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    regions = find_regions(input_grid)
    
    # determine output grid size - max x and y of any identified region
    max_r = 0
    max_c = 0
    for r, c in regions:
        if r > max_r:
          max_r = r
        if c > max_c:
          max_c = c;

    output_grid = np.zeros((max_r+1, max_c+1), dtype=int)

    # Place red (2) pixels at the top-left corner of each identified green cluster
    for r, c in regions:
        output_grid[r, c] = 2

    return output_grid.tolist()
```
