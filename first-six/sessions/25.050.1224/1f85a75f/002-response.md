# 1f85a75f • 002 • example_1 - CODE

---
```python
"""
This program extracts the largest contiguous object from the input grid,
determines its bounding box, and creates a new grid based on the bounding box
dimensions. The new grid is filled with the color of the extracted object.
Finally, the top-right and bottom-left corners of the resized grid with 0.
"""

import numpy as np

def find_largest_object(grid):
    """
    Finds the largest contiguous object in the grid.
    Contiguous is defined as sharing an edge or a corner.
    """
    visited = set()
    max_size = 0
    max_color = -1
    object_coords = []

    rows, cols = grid.shape
    
    def dfs(row, col, color, current_coords):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return 0
        visited.add((row, col))
        current_coords.append((row,col))
        size = 1
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                size += dfs(r, c, color, current_coords)
        return size


    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                current_coords = []
                color = grid[r, c]
                object_size = dfs(r, c, color, current_coords)
                if object_size > max_size:
                    max_size = object_size
                    max_color = color
                    object_coords = current_coords
    return max_color, object_coords

def bounding_box(coords):
    """
    Calculates the bounding box of a set of coordinates.
    Returns (min_row, min_col, max_row, max_col).
    """
    min_row = min(coords, key=lambda x: x[0])[0]
    min_col = min(coords, key=lambda x: x[1])[1]
    max_row = max(coords, key=lambda x: x[0])[0]
    max_col = max(coords, key=lambda x: x[1])[1]
    return min_row, min_col, max_row, max_col

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)

    # 1. Find the largest object and its color.
    object_color, object_coords = find_largest_object(input_grid)

    # 2. Determine the bounding box.
    min_row, min_col, max_row, max_col = bounding_box(object_coords)

    # 3. Calculate output grid dimensions. We add two additional rows
    rows = (max_row - min_row + 1) + 2
    cols = (max_col - min_col + 1)
    
    # 4. Create the new grid and fill it with the object's color.
    output_grid = np.full((rows, cols), object_color)

    # 5. Place zeros in the corners.
    output_grid[0, -1] = 0  # Top-right corner
    output_grid[-1, 0] = 0  # Bottom-left corner

    return output_grid.tolist()
```

