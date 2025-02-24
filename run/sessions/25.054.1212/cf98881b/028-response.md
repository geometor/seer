# cf98881b • 028 • refine_coder

---
```python
"""
Extracts a subgrid from the input grid. The subgrid is defined by the bounding box of the largest contiguous yellow region, iteratively expanded to include adjacent blue and yellow pixels.  Within this subgrid, all colors other than yellow and blue are changed to white.
"""

import numpy as np

def find_largest_object(grid, color):
    # implementation of depth first search
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    max_object_coords = []

    def dfs(row, col):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return 0, []

        visited[row, col] = True
        size = 1
        coords = [(row, col)]

        # Explore all 8 neighbors (including diagonals).
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_size, new_coords = dfs(row + dr, col + dc)
                size += new_size
                coords.extend(new_coords)

        return size, coords

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                size, coords = dfs(r, c)
                if size > max_size:
                    max_size = size
                    max_object_coords = coords
    return max_object_coords

def get_bounding_box(coords):
    min_row = min(c[0] for c in coords)
    max_row = max(c[0] for c in coords)
    min_col = min(c[1] for c in coords)
    max_col = max(c[1] for c in coords)
    return min_row, max_row, min_col, max_col

def expand_bounding_box(input_grid, bbox, colors):
    min_row, max_row, min_col, max_col = bbox
    expanded = True

    while expanded:
        expanded = False
        new_min_row, new_max_row, new_min_col, new_max_col = min_row, max_row, min_col, max_col

        # Check perimeter
        for r in range(max(0, min_row - 1), min(input_grid.shape[0], max_row + 2)):
            for c in [max(0, min_col - 1), min(input_grid.shape[1] - 1, max_col + 1)]:
                if 0 <= r < input_grid.shape[0] and 0 <= c < input_grid.shape[1] and input_grid[r,c] in colors:
                    new_min_row = min(new_min_row, r)
                    new_max_row = max(new_max_row, r)
                    new_min_col = min(new_min_col, c)
                    new_max_col = max(new_max_col, c)
                    expanded = True

        for c in range(max(0, min_col - 1), min(input_grid.shape[1], max_col + 2)):
             for r in [max(0, min_row - 1), min(input_grid.shape[0] - 1, max_row + 1)]:
                if 0 <= r < input_grid.shape[0] and 0 <= c < input_grid.shape[1] and input_grid[r,c] in colors:
                    new_min_row = min(new_min_row, r)
                    new_max_row = max(new_max_row, r)
                    new_min_col = min(new_min_col, c)
                    new_max_col = max(new_max_col, c)
                    expanded = True

        min_row, max_row, min_col, max_col = new_min_row, new_max_row, new_min_col, new_max_col

    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # Find the largest yellow object.
    yellow_coords = find_largest_object(input_grid, 4)

    # Get its bounding box.
    bbox = get_bounding_box(yellow_coords)

    # expand for adjacent blue and yellow iteratively
    bbox = expand_bounding_box(input_grid, bbox, [1, 4])
    min_row, max_row, min_col, max_col = bbox

    # Extract the subgrid.
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1].copy()

    # Replace colors other than yellow and blue with white within subgrid
    for r in range(output_grid.shape[0]):
      for c in range(output_grid.shape[1]):
        if output_grid[r,c] != 4 and output_grid[r,c] != 1:
          output_grid[r,c] = 0

    return output_grid
```
