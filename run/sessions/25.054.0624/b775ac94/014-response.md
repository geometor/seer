# b775ac94 • 014 • example_3 • investigate_coder

---
```python
"""
Duplicates and expands colored objects in a grid, with exceptions of shifting for yellow and azure objects.
"""

import numpy as np

def find_objects(grid):
    """
    Finds all contiguous colored regions (objects) in the grid.
    Returns a dictionary where keys are colors and values are lists of (row, col) coordinates.
    """
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, obj_coords):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        obj_coords.append((row, col))
        dfs(row + 1, col, color, obj_coords)
        dfs(row - 1, col, color, obj_coords)
        dfs(row, col + 1, color, obj_coords)
        dfs(row, col - 1, color, obj_coords)

    for row in range(rows):
        for col in range(cols):
            color = grid[row, col]
            if color != 0 and (row, col) not in visited:
                obj_coords = []
                dfs(row, col, color, obj_coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(obj_coords)
    return objects


def transform(input_grid):
    # Initialize output grid with the same dimensions and background color
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

   # Find all objects in the input grid
    objects = find_objects(input_grid)

    # Process each object based on its color
    for color, obj_list in objects.items():
        for obj_coords in obj_list:
            if color == 4:  # Yellow object
                #shift yellow right
                for r, c in obj_coords:
                    output_grid[r,min(cols-1,c+1)] = 4

                # check if 1-cell or L-shape to see if expand
                if len(obj_coords) == 4:
                    coords = np.array(obj_coords)
                    min_row, min_col = np.min(coords, axis=0)
                    max_row, max_col = np.max(coords, axis=0)
                    
                    #check if L
                    is_l_shape = (max_row - min_row == 1) and (max_col - min_col == 1)

                    if is_l_shape:
                        for r, c in obj_coords:
                            if r == min_row or c == max_col:
                                output_grid[r,min(cols-1,c+2)] = 4

            elif color == 8: #azure object
                #shift azure right
                for r, c in obj_coords:
                    output_grid[r,min(cols-1,c+1)] = 8

            else: #other objects
                # Duplicate and expand other colored objects
                for r, c in obj_coords:
                    output_grid[r, c] = color
                    output_grid[r, min(cols-1,c + (c - min([c_ for _, c_ in obj_coords]) + 1))] = color #expand

    return output_grid
```
