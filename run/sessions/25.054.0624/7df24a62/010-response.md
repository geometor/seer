# 7df24a62 • 010 • refine_coder

---
```python
"""
Preserves all yellow pixels and mirrors any blue shape to the top of the output grid.
"""

import numpy as np

def find_blue_shapes(grid):
    """Finds all contiguous blue shapes in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    blue_shapes = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, shape):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != 1:
            return
        visited[r, c] = True
        shape.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, shape)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1 and not visited[r, c]:
                shape = []
                dfs(r, c, shape)
                if shape:
                    blue_shapes.append(shape)
    return blue_shapes
def get_shape_bounds(shape):
    """Calculates the bounding box of a shape."""
    min_row = min(p[0] for p in shape)
    max_row = max(p[0] for p in shape)
    min_col = min(p[1] for p in shape)
    max_col = max(p[1] for p in shape)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape
    # Preserve yellow pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 4:
                output_grid[r, c] = 4

    # Find blue shapes
    blue_shapes = find_blue_shapes(input_grid)

    # Mirror blue shapes to the top
    for shape in blue_shapes:
        min_row, max_row, min_col, max_col = get_shape_bounds(shape)
        shape_height = max_row - min_row + 1
        shape_width = max_col - min_col + 1

        # Find a suitable top position
        target_row = 0
        for r_offset in range(rows - shape_height + 1):
             target_col = min_col #start position
             collision = False

             # check rows from top to bottom to avoid overlap
             for r in range(shape_height):
                for c in range(shape_width):
                   if output_grid[target_row+ r, target_col+c ] != 0:
                       collision = True
                       break
                if collision:
                  break

             if not collision:
                break
             else:
                target_row += 1

        # Copy the shape to the target location
        for r in range(shape_height):
           for c in range(shape_width):
                if input_grid[min_row +r, min_col+c] == 1:
                    output_grid[target_row + r, target_col + c] = 1

    return output_grid
```
