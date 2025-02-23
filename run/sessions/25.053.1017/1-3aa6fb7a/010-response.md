# 1-3aa6fb7a • 010 • example_2 - CODE

---
```python
"""
1.  **Identify Azure Objects:** Locate all contiguous blocks of azure (8) pixels within the input grid.
2.  **Insert Blue Pixels Diagonally**: For some azure pixels, place a blue (1) pixel diagonally adjacent to the azure pixel, specifically, either directly above or directly below *and* left one position or right one position.
3. **Selective transformation**: Not all azure pixels get a blue neighbor, only those that are at the diagonal edges of an azure shape.
4.  **Preserve Other Pixels:** All other pixels, including the existing azure pixels, remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """Find contiguous objects of a specific color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        """Depth-first search to find contiguous pixels."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
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
                objects.append(current_object)
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    
    # change output pixels
    for obj in azure_objects:
        for r, c in obj:
            # Check for diagonal placement above and to the left
            if r > 0 and c > 0 and input_grid[r-1,c-1] == 0:
                if (r-1, c) not in obj and (r,c-1) not in obj:
                    output_grid[r - 1, c - 1] = 1
                    continue #only do one
            # Check for diagonal placement above and to the right
            if r > 0 and c < input_grid.shape[1] - 1 and input_grid[r - 1, c + 1] == 0:
                if (r-1,c) not in obj and (r,c+1) not in obj:
                    output_grid[r - 1, c + 1] = 1
                    continue
            # Check for diagonal placement below and to the left
            if r < input_grid.shape[0] - 1 and c > 0 and input_grid[r + 1, c - 1] == 0:
                if (r + 1, c) not in obj and (r,c-1) not in obj:
                    output_grid[r + 1, c - 1] = 1
                    continue
            # Check for diagonal placement below and to the right
            if r < input_grid.shape[0] - 1 and c < input_grid.shape[1] - 1 and input_grid[r+1,c+1] == 0:
                if (r+1,c) not in obj and (r, c+1) not in obj:
                    output_grid[r + 1, c + 1] = 1
                    continue

    return output_grid
```
