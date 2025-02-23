# 3631a71a • 024 • refine_coder

---
```python
"""
1.  Identify all green (3) objects in the input grid.
2.  For each green object, check if it forms a 2x2 square.
3.  If a green object is a 2x2 square, keep it unchanged in the output grid.
4.  If a green object is NOT a 2x2 square, transform it to the background color (0) in the output grid.
5.  All other colors in input grid transform to themselves in output grid.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous objects of a specific color in the grid.
    """
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
        dfs(row + 1, col + 1, current_object)  # Check diagonals
        dfs(row + 1, col - 1, current_object)
        dfs(row - 1, col + 1, current_object)
        dfs(row - 1, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_2x2_square(object_pixels, grid):
    """
    Checks if an object is a 2x2 square.
    """
    if len(object_pixels) != 4:
        return False

    rows = [r for r, c in object_pixels]
    cols = [c for r, c in object_pixels]

    if max(rows) - min(rows) != 1 or max(cols) - min(cols) != 1:
        return False
        
    min_row, min_col = min(rows), min(cols)

    # Check if the 4 pixels form a filled 2x2 square
    expected_pixels = {(min_row, min_col), (min_row + 1, min_col), (min_row, min_col + 1), (min_row + 1, min_col + 1)}
    return set(object_pixels) == expected_pixels



def transform(input_grid):
    """
    Transforms the input grid based on 2x2 green squares.
    """
    output_grid = np.copy(input_grid)
    green_objects = find_objects(input_grid, 3)

    for obj in green_objects:
        if not is_2x2_square(obj, input_grid):
            for r, c in obj:
                output_grid[r, c] = 0  # Change to background color

    return output_grid
```
