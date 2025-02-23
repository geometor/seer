# db93a21d • 012 • refine_coder

---
```python
"""
1.  **Identify Maroon Objects:** Find all contiguous regions of maroon (color 9) pixels. These are the "maroon objects."

2.  **Identify Leftmost and Rightmost Objects:** Determine the bounding box for each maroon object. The object with the smallest minimum column index is the "leftmost" object. The object with the largest maximum column index is the "rightmost" object.

3.  **Flood Fill Green (Left):** Starting from the white (0) cells adjacent to the *leftmost* maroon object, flood-fill the connected white area with green (3). Stop the fill when encountering any non-white cell or the edge of the grid. The flood fill extends both above *and* below the object, and is not limited to be 'above and to the left'.

4.  **Flood Fill Blue (Right):** Starting from the white (0) cells adjacent to the *rightmost* maroon object, flood-fill the connected white region with blue (1). Stop the fill when you reach another color, *or* when you reach an area that has already been filled with green due to a leftmost object. The flood fill extends in all directions around the *rightmost* maroon object.

5.  **All Other Pixels:** Leave all other pixels unchanged.
"""

import numpy as np
from collections import deque

def find_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return

        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                if current_object:
                    objects.append(current_object)
    return objects

def get_bounding_box(obj):
    min_row = min(p[0] for p in obj)
    max_row = max(p[0] for p in obj)
    min_col = min(p[1] for p in obj)
    max_col = max(p[1] for p in obj)
    return min_row, max_row, min_col, max_col

def flood_fill(grid, start_row, start_col, fill_color, boundary_color=None):
    rows, cols = grid.shape
    queue = deque([(start_row, start_col)])
    visited = np.zeros_like(grid, dtype=bool)

    if grid[start_row, start_col] != 0:  # Ensure starting point is white
        return

    while queue:
        row, col = queue.popleft()

        if (row < 0 or row >= rows or col < 0 or col >= cols or
                visited[row, col] or grid[row, col] != 0):
            continue

        visited[row, col] = True
        grid[row, col] = fill_color

        queue.append((row + 1, col))
        queue.append((row - 1, col))
        queue.append((row, col + 1))
        queue.append((row, col - 1))


def get_adjacent_white_cells(grid, obj):
    adjacent_whites = set()
    rows, cols = grid.shape
    for r, c in obj:
        # Check adjacent cells
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 0:
                adjacent_whites.add((nr, nc))
    return list(adjacent_whites)

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    maroon_objects = find_objects(input_grid, 9)

    # Find leftmost and rightmost maroon objects
    if maroon_objects:
        leftmost_object = min(maroon_objects, key=lambda obj: get_bounding_box(obj)[2])
        rightmost_object = max(maroon_objects, key=lambda obj: get_bounding_box(obj)[3])

        # Flood fill green from adjacent white cells of leftmost object
        left_adjacent_whites = get_adjacent_white_cells(output_grid, leftmost_object)
        for r, c in left_adjacent_whites:
            flood_fill(output_grid, r, c, 3)

        # Flood fill blue from adjacent white cells of rightmost object
        right_adjacent_whites = get_adjacent_white_cells(output_grid, rightmost_object)
        for r, c in right_adjacent_whites:
            flood_fill(output_grid, r, c, 1)

    return output_grid
```
