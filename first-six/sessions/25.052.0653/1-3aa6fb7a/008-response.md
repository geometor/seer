# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
The input consists of azure (color 8) L-shaped objects.  The output preserves these objects and adds two blue (color 1) cells. One blue cell is placed immediately to the right of the corner of any L-shape that has a "Top-Left Corner" orientation. The other blue cell is placed immediately to the left of the corner of any L-shape that has a "Bottom-Right Corner" orientation.
"""

import numpy as np

def find_objects(grid, color):
    """Finds all L-shaped objects (3 contiguous cells) of a given color."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                if len(current_object) == 3:  # Check if it's an L-shape (3 cells)
                    objects.append(current_object)
    return objects

def get_corner(obj):
    """Identifies the corner cell of an L-shaped object."""
    rows, cols = zip(*obj)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)

    for r, c in obj:
        neighbors = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in obj:
                neighbors += 1
        if neighbors == 2:  # Corner cell has exactly two neighbors within the object
            return (r, c)
    return None  # Should not happen, but for safety

def get_orientation(obj, corner):
    """Determines the orientation of the L-shape."""
    r, c = corner
    rows, cols = zip(*obj)
    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    
    if r == min_row and c == min_col:
      return "Top-Left"
    if r == min_row and c == max_col:
      return "Top-Right"
    if r == max_row and c == min_col:
      return "Bottom-Left"
    if r == max_row and c == max_col:
      return "Bottom-Right"
      

def transform(input_grid):
    """Transforms the input grid according to the L-shape rule."""
    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    azure_objects = find_objects(input_grid, 8) # Find azure L-shaped objects

    for obj in azure_objects: # Iterate over each found object
        corner = get_corner(obj)  # Determine the corner cell
        if corner is None:
            continue  # Skip if no corner found (shouldn't happen)
        orientation = get_orientation(obj, corner) # Determine the orientation

        r, c = corner   # Get corner coordinates
        if orientation == "Top-Left":  # If Top-Left, add blue to the right
            if c + 1 < output_grid.shape[1]:
                output_grid[r, c + 1] = 1
        elif orientation == "Bottom-Right":  # If Bottom-Right, add blue to the left
            if c - 1 >= 0:
                output_grid[r, c - 1] = 1
    return output_grid
```
