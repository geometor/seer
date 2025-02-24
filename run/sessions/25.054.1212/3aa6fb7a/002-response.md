# 3aa6fb7a • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Azure Shapes:** Locate all contiguous shapes composed of azure (8) pixels within the input grid.
2.  **Select Hint Location:** For *each* azure shape, there might be multiple valid positions for placing the hint. Select locations in this order
    1.  to the left of the object
    2.  above the object
    3.  to the right of the object
    4.  below the object
3.  **Add Blue Pixel:** Place a single blue (1) pixel in the first valid selected location. Do this for all shapes.
4.  **Preserve Original:** All other pixels from the input grid remain unchanged in the output grid.
"""

import numpy as np

def find_objects(grid, color):
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Sort object pixels by row then column to prioritize top-left placement
        obj.sort(key=lambda x: (x[0], x[1]))
        placed = False

        # Try placing to the left
        for row, col in obj:
            if col > 0 and input_grid[row, col - 1] == 0:
                output_grid[row, col - 1] = 1
                placed = True
                break  # Only place one hint per object
        if placed:
            continue

        # Try placing above
        for row, col in obj:
            if row > 0 and input_grid[row - 1, col] == 0:
                output_grid[row - 1, col] = 1
                placed=True
                break
        if placed:
            continue
            
        # Try placing to the right
        for row, col in obj:
            if col < input_grid.shape[1] - 1 and input_grid[row, col + 1] == 0:
                output_grid[row, col + 1] = 1
                placed = True
                break  # Only place one hint per object
        if placed:
             continue
             
        # Try placing below
        for row, col in obj:
            if row < input_grid.shape[0] - 1 and input_grid[row + 1, col] == 0:
                output_grid[row + 1, col] = 1
                placed=True
                break
        if placed:
             continue

    return output_grid
```
