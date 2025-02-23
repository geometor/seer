# 5-150deff5 • 008 • refine_coder

---
```python
"""
1.  **Find Shapes:** Identify all distinct, contiguous regions (shapes) of gray (5) pixels in the input grid.

2.  **Outline Shapes:** For each identified gray shape:
    *   Iterate through all pixels of the shape.
    *   If a gray pixel is adjacent (up, down, left, or right) to a pixel that is *not* part of the *same* shape (either a different color or out of bounds), replace it with azure (8). This creates an outline around each shape.

3.  **Fill Shapes:** For each outlined shape:
    *   find seed points, defined as gray points that are adjacent to the boundary.
    *   Use a flood-fill algorithm, starting from any internal points, to replace all interior, connected, gray (5) pixels with red (2).
    *   *Crucially*, the flood fill must *stop* when it encounters an azure (8) pixel (the outline) or the boundary of the grid. The outline acts as a strict boundary for the fill operation.

4.  **Preserve Background:** Ensure all pixels that were originally white (0) remain unchanged throughout the entire process.
"""

import numpy as np
from collections import deque

def find_shapes(grid, shape_color):
    """Finds all contiguous regions of the specified color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    shapes = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_shape):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != shape_color:
            return
        visited[r, c] = True
        current_shape.append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, current_shape)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == shape_color and not visited[row, col]:
                current_shape = []
                dfs(row, col, current_shape)
                shapes.append(current_shape)
    return shapes

def outline_shape(grid, shape, outline_color):
    """Outlines a single shape with the specified color."""
    outlined_grid = np.copy(grid)
    for r, c in shape:
        is_outline = False
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]) or (nr, nc) not in shape:
                is_outline = True
                break
        if is_outline:
            outlined_grid[r, c] = outline_color
    return outlined_grid

def flood_fill(grid, shape, fill_color, outline_color):
    """
    Flood fills the interior of a shape, respecting the outline.
    """
    rows, cols = grid.shape
    filled_grid = np.copy(grid)
    visited = set()
    q = deque()

    # Find seed points (gray pixels adjacent to non-gray pixels)
    for r, c in shape:
        if filled_grid[r,c] == outline_color:
            continue # skip outline
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols and (nr,nc) in shape ):
                #seed if adjacent to the boundary
                q.append((r,c))
                visited.add((r,c))
                break

    while q:
        r, c = q.popleft()
        filled_grid[r,c] = fill_color #always fill

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            #stay in bounds, is not visited, and must be gray
            if (0 <= nr < rows and 0 <= nc < cols and
                (nr, nc) not in visited and filled_grid[nr,nc] != outline_color and (nr,nc) in shape):
                q.append((nr, nc))
                visited.add((nr, nc))
    return filled_grid

def transform(input_grid):
    # Initialize output_grid with the same dimensions and background as input_grid.
    output_grid = np.copy(input_grid)
    shape_color = 5
    outline_color = 8
    fill_color = 2

    # Find all distinct shapes.
    shapes = find_shapes(input_grid, shape_color)

    # Outline and then fill each shape
    for shape in shapes:
        output_grid = outline_shape(output_grid, shape, outline_color)
    
    for shape in shapes:
        output_grid = flood_fill(output_grid,shape, fill_color, outline_color)
        

    return output_grid
```
