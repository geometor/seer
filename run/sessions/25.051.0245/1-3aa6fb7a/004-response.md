# 1-3aa6fb7a • 004 • example_2 - CODE

---
```yaml
task_context: "The task involves identifying connected components of color 8 (azure) within the input grid. For each component, the goal is to locate its 'end points'—cells within the component that have exactly one neighbor of the same color. Once the end points are identified, the 'top-most' and 'bottom-most' end points are determined based on their row and column indices. A color 1 (blue) cell is then placed to the right of the 'top-most' end point and to the left of the 'bottom-most' end point in the output grid. If no modifications are needed for a cell, it retains its original color from the input grid."
natural_language_program: |
  For each connected component of color 8 in the input grid:
  1. Identify all cells that comprise the connected component.
  2. Within each component, determine the "end points," which are cells having exactly one neighbor of the same color (8).
  3. From the identified end points, find the "top-most" end point (minimum row index, then minimum column index if tied).
  4. Also, find the "bottom-most" end point (maximum row index, then minimum column index if tied).
  5. In the output grid, modify the cell immediately to the right of the "top-most" end point to color 1 (blue).
  6. Similarly, modify the cell immediately to the left of the "bottom-most" end point to color 1 (blue).
  7. Any cell in the output grid not affected by steps 5 or 6 should retain its original color from the input grid.
```
```python
"""
For each connected component of color 8 in the input grid:
1. Identify all cells that comprise the connected component.
2. Within each component, determine the "end points," which are cells having exactly one neighbor of the same color (8).
3. From the identified end points, find the "top-most" end point (minimum row index, then minimum column index if tied).
4. Also, find the "bottom-most" end point (maximum row index, then minimum column index if tied).
5. In the output grid, modify the cell immediately to the right of the "top-most" end point to color 1 (blue).
6. Similarly, modify the cell immediately to the left of the "bottom-most" end point to color 1 (blue).
7. Any cell in the output grid not affected by steps 5 or 6 should retain its original color from the input grid.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """ Get valid neighbors of a cell. """
    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def find_connected_components(grid, color):
    """ Find all connected components of a given color. """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    components = []

    def dfs(r, c, current_component):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_component.append((r, c))
        for nr, nc in get_neighbors(grid, r, c):
            dfs(nr, nc, current_component)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_component = []
                dfs(r, c, current_component)
                components.append(current_component)
    return components

def find_end_points(grid, component):
    """ Find end points in a component. """
    end_points = []
    for r, c in component:
        neighbors = get_neighbors(grid, r, c)
        count = 0
        for nr, nc in neighbors:
            if (nr, nc) in component:
                count += 1
        if count == 1:
            end_points.append((r, c))
    return end_points

def find_top_most_end_point(end_points):
    """ Find the top-most end point. """
    return min(end_points, key=lambda x: (x[0], x[1]))

def find_bottom_most_end_point(end_points):
    """ Find the bottom-most end point. """
    return max(end_points, key=lambda x: (x[0], x[1]))

def transform(input_grid):
    """ Transform the input grid according to the specified rules. """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    components = find_connected_components(input_grid, 8)

    for component in components:
        end_points = find_end_points(input_grid, component)
        if end_points:
            top_most = find_top_most_end_point(end_points)
            bottom_most = find_bottom_most_end_point(end_points)

            # Place color 1 to the right of top-most
            if top_most[1] + 1 < output_grid.shape[1]:
                output_grid[top_most[0], top_most[1] + 1] = 1

            # Place color 1 to the left of bottom-most
            if bottom_most[1] - 1 >= 0:
                output_grid[bottom_most[0], bottom_most[1] - 1] = 1

    return output_grid
```

