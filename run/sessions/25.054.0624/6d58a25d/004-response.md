# 6d58a25d • 004 • refine_coder

---
```python
"""
1.  **Copy all Maroon Pixels**: Identify and copy all maroon (9) pixels from the input to the output grid, maintaining their relative positions.
2.  **Process Orange Pixels**: Locate all clusters of orange (7) pixels. For each cluster, copy it to the output grid. Additionally "extrude" or copy the orange color upwards by up to three pixels.
3. **Move red and green**: Red and green pixels appear to maintain position *relative* to orange, moving upwards along with the "extruded" orange pixels.
4.  **Process Azure Pixels:** For every azure (8) pixel in the input grid:
    *   Copy the azure pixel to the output grid in the same position.
    *   Add an azure pixel directly *above* the current azure pixel (row - 1). If the current pixel is in the top row (row 0), do not add a pixel above.
5. **Overwrite**: If any azure pixels are placed in the same position as a maroon, red, green or orange pixel in the output grid, the azure pixel overwrites (replaces) the other pixel's color. Other pixels are *not* overwritten.
"""

import numpy as np

def find_objects(grid, color):
    """Finds all objects of a given color in the grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(r, c, current_object):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.copy(input_grid)  # Initialize output_grid as a copy of input_grid
    rows, cols = input_grid.shape

    # 1. Copy all Maroon Pixels
    maroon_objects = find_objects(input_grid, 9)
    for obj in maroon_objects:
        for r, c in obj:
            output_grid[r, c] = 9

    # 2. Process Orange Pixels and neighbors (red and green)
    orange_objects = find_objects(input_grid, 7)
    for obj in orange_objects:
        for r, c in obj:
            output_grid[r, c] = 7  # Copy original orange
            # Extrude upwards
            for i in range(1, 4):
                if r - i >= 0:
                    output_grid[r - i, c] = 7

        # find and move red neighbors
        for r,c in obj:
             if r > 0 and input_grid[r-1,c] == 2:
                for i in range(1,4):
                    if r-i >=0:
                        output_grid[r-i-1,c] = 2
             if r+1 < rows and input_grid[r+1, c] == 2:
                for i in range(1,4):
                    if r-i >= 0:
                        output_grid[r-i+1,c] = 2

        # find and move green neighbors
        for r,c in obj:
            if r > 0 and input_grid[r-1,c] == 3:
                for i in range(1,4):
                    if r-i >=0:
                        output_grid[r-i-1,c] = 3
            if r+1 < rows and input_grid[r+1,c] == 3:
                for i in range(1,4):
                    if r-i >=0:
                        output_grid[r-i + 1,c] = 3
            if c > 0 and input_grid[r,c-1] == 3:
                for i in range(1,4):
                    if r-i >=0:
                        output_grid[r-i,c-1] = 3
            if c + 1 < cols and input_grid[r,c+1] ==3:
                for i in range(1,4):
                    if r-i >= 0:
                        output_grid[r-i,c+1] = 3


    # 3. Process Azure Pixels
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:
                output_grid[r, c] = 8  # Copy original
                if r > 0:
                    output_grid[r - 1, c] = 8  # Add above

    # 4. Overwrite (Azure over others) - handled implicitly because azure is processed last.

    return output_grid
```
