# 3-1e0a9b12 • 012 • refine_coder

---
```python
"""
1. Identify all contiguous blocks of non-zero (colored) pixels. These are our "objects."
2. For each column, starting from the bottom row and moving upwards, iterate through the identified objects.
3. Move each object downwards as far as possible within its original column, stopping when it hits the bottom of the grid or another object. If multiple instances of an object of the same color exist, stack vertically, merging from top down.
4. Empty/white (0) cells remain empty.
"""

import numpy as np

def find_objects(grid):
    # Find contiguous blocks of non-zero pixels
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] != 0 and (row, col) not in visited:
                obj = []
                dfs(row, col, grid[row, col], obj)
                objects.append(obj)
    return objects

def move_object_down(grid, obj):
    # Move an object down to its lowest possible position in the grid
    
    # Sort object pixels by row (descending) to move the bottom pixels first.
    obj.sort(key=lambda x: x[0], reverse=True)
    
    new_obj = []
    for row, col in obj:
        new_row = row
        while new_row + 1 < grid.shape[0] and grid[new_row + 1, col] == 0:
            new_row += 1
        new_obj.append((new_row,col))    
    return new_obj

def transform(input_grid):
    # Initialize output_grid as a copy of the input
    output_grid = np.zeros_like(input_grid)

    # Find all objects
    objects = find_objects(input_grid)
    
    # Create a dictionary to store objects by column
    objects_by_column = {}
    for obj in objects:
        for row, col in obj:
            if col not in objects_by_column:
                objects_by_column[col] = []
            objects_by_column[col].append((row,col))

    # Iterate through each column
    for col in sorted(objects_by_column.keys()):
        column_objects = objects_by_column[col]

        # consolidate by color, put consolidated back in objects_by_column
        consolidated = {}
        for r,c in column_objects:
            color = input_grid[r,c]
            if color not in consolidated:
                consolidated[color] = []
            consolidated[color].append((r,c))

        # for each color group
        for color, pixels in consolidated.items():
            # sort by row descending
            pixels.sort(key=lambda x:x[0], reverse=True)

            # find lowest possible row
            lowest_row = input_grid.shape[0] - 1
            for r, _ in reversed(pixels):
                while lowest_row > 0 and (output_grid[lowest_row,col] != 0 and output_grid[lowest_row, col] != color):
                    lowest_row -=1
                output_grid[lowest_row, col] = color
                lowest_row -= 1


    return output_grid
```
