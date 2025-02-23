# 6d58a25d • 006 • refine_coder

---
```python
"""
1.  **Copy Maroon Pixels**: Copy all maroon (9) pixels from the input to the output, maintaining position.
2.  **Process Orange Pixels**: Find orange (7) pixel clusters.  For each cluster, copy it to the output. Then, for each orange pixel, extend the orange color upwards by up to three pixels *if* there isn't already an orange pixel there.
3.  **Propagate Red and Green**: After placing orange, find red (2) and green (3) pixels that are *directly* adjacent (up, down, left, or right, but *not* diagonally) to the *original* orange pixels (before extrusion) in the input grid.  For each such red/green pixel, shift it upwards by the same amount the orange pixel directly adjacent to it was extruded.
4.  **Place Azure Pixels:** Place azure (8) pixels in the output grid.  For every azure pixel in the input, copy it to the output, and also place one azure pixel directly above it (if not in the top row). Azure pixels overwrite any other colors.
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

def get_neighbors(grid, r, c):
    """Gets the valid neighbors (up, down, left, right) of a cell."""
    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r + 1 < rows:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c + 1 < cols:
        neighbors.append((r, c + 1))
    return neighbors


def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    output_grid = np.zeros_like(input_grid)  # Initialize output_grid as all black
    rows, cols = input_grid.shape

    # 1. Copy Maroon Pixels
    maroon_pixels = np.where(input_grid == 9)
    for r, c in zip(maroon_pixels[0], maroon_pixels[1]):
        output_grid[r, c] = 9

    # 2. Process Orange Pixels
    orange_objects = find_objects(input_grid, 7)
    orange_positions = []  # Store original orange positions
    for obj in orange_objects:
        for r, c in obj:
            orange_positions.append((r,c))
            output_grid[r, c] = 7
            # Conditional Extrusion
            for i in range(1, 4):
                if r - i >= 0 and output_grid[r - i, c] != 7:
                    output_grid[r - i, c] = 7
                else:
                    break # Stop extruding if we hit another orange pixel


    # 3. Propagate Red and Green
    for r_orig, c_orig in orange_positions:  # Iterate through *original* orange positions
        neighbors = get_neighbors(input_grid, r_orig, c_orig)

        for r_neighbor, c_neighbor in neighbors:
            if input_grid[r_neighbor,c_neighbor] in (2,3):
                color = input_grid[r_neighbor, c_neighbor]
                # find extrusion amount
                extrusion_amount = 0
                for i in range(1,4):
                    if r_orig - i < 0 or input_grid[r_orig -i, c_orig] != 7 :
                        break
                    else:
                        extrusion_amount +=1

                new_r = r_neighbor - extrusion_amount
                if new_r >= 0:

                  output_grid[new_r, c_neighbor] = color


    # 4. Place Azure Pixels (with overwriting)
    azure_pixels = np.where(input_grid == 8)
    for r, c in zip(azure_pixels[0], azure_pixels[1]):
        output_grid[r, c] = 8  # Copy original
        if r > 0:
            output_grid[r - 1, c] = 8  # Add above

    return output_grid
```
