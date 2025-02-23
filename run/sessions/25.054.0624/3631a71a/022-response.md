# 3631a71a • 022 • refine_coder

---
```python
"""
1.  Iterate through the input grid.
2.  Identify all maroon (9) objects.
3.  Identify all 2x2 green (3) squares, and find the largest one by area.
4. Transform all colors in input grid that are not belongs to maroon objects and the largest 2x2 green squares to themself in output grid.
5.  Output the modified grid.
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

def find_2x2_square(grid, color):
    """
    Finds 2x2 squares of a specific color.
    """
    squares = []
    for r in range(grid.shape[0] - 1):
        for c in range(grid.shape[1] - 1):
            if (grid[r, c] == color and grid[r + 1, c] == color and
                    grid[r, c + 1] == color and grid[r + 1, c + 1] == color):
                squares.append([(r,c),(r+1,c),(r,c+1),(r+1,c+1)])
    return squares

def transform(input_grid):
    """
    Transforms the input grid according to the described rules.
    """
    output_grid = np.copy(input_grid)
    
    # Find all maroon objects
    maroon_objects = find_objects(input_grid, 9)
    
    # Find largest 2x2 Green square
    green_squares = find_2x2_square(input_grid, 3)
    largest_green_square = []
    if green_squares:
        largest_green_square = max(green_squares, key=len)
    
    # Create sets of pixels to preserve
    preserve_pixels = set()

    for obj in maroon_objects:
      for r, c in obj:
        preserve_pixels.add((r,c))
    
    for r, c in largest_green_square:
        preserve_pixels.add((r,c))

    # Iterate through the grid and apply transformation rule 4
    for row in range(input_grid.shape[0]):
        for col in range(input_grid.shape[1]):
          if (row, col) not in preserve_pixels:
            output_grid[row,col] = input_grid[row,col]


    return output_grid
```
