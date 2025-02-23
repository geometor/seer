# 264363fd • 006 • refine_coder

---
```python
"""
The transformation identifies a target object within the input grid, traces (fully or partially) its outline with a specified color, highlights points on the outline with another color, copies other objects, and then mirrors the output vertically.
"""

import numpy as np

def find_objects(grid):
    # Find all objects in a grid.  Returns a dictionary mapping color to a list of coordinates.
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, coords):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        coords.append((row, col))
        dfs(row + 1, col, color, coords)
        dfs(row - 1, col, color, coords)
        dfs(row, col + 1, color, coords)
        dfs(row, col - 1, color, coords)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                color = grid[row, col]
                coords = []
                dfs(row, col, color, coords)
                if color not in objects:
                    objects[color] = []
                objects[color].append(coords)
    return objects

def outline_object(grid, object_coords, outline_color):
    # Create an outline of the traced object.
    output_grid = np.copy(grid)

    for r, c in object_coords:
        #check neighbors
        neighbors = []
        for i in range(-1,2):
            for j in range(-1,2):
                if (i != 0 or j != 0):
                    neighbor_row = r + i
                    neighbor_col = c + j
                    if (0 <= neighbor_row < grid.shape[0] and 0 <= neighbor_col < grid.shape[1]):
                          neighbors.append(grid[neighbor_row,neighbor_col])
        #if a neighbor is a different color than the object, we have an outline
        if any(neighbor != grid[r, c] for neighbor in neighbors):
            output_grid[r,c] = outline_color

    return output_grid

def highlight_object(grid, object_coords, highlight_color):
    # Highlights inside object
    output_grid = np.copy(grid)
    for r, c in object_coords:
        output_grid[r,c] = highlight_color
    return output_grid


def mirror_vertical(grid):
    # Mirror the grid vertically.
    return np.fliplr(grid)

def transform(input_grid):
    # Initialize output grid
    output_grid = np.copy(input_grid)


    # Determine target color and outline color, and highlight color based on input
    target_color = None
    outline_color = None
    highlight_color = None
    copy_color = None

    if (np.any(input_grid == 1) and len(set(np.unique(input_grid))) > 2): #blue
        target_color = 1
        outline_color = 2
        highlight_color = 3
    elif (np.any(input_grid == 2) and len(set(np.unique(input_grid))) > 2): #red
        target_color = 2
        outline_color = 1
        highlight_color = 3
    elif (np.any(input_grid == 3) and len(set(np.unique(input_grid))) > 2): #green
        target_color = 3
        outline_color = 8
        highlight_color = 5
        copy_color = 5



    objects = find_objects(input_grid)

     # Outline target objects, if a target color exists
    if target_color in objects:
        for obj_coords in objects[target_color]:
            output_grid = outline_object(output_grid, obj_coords, outline_color)

    #copy other objects
    if copy_color in objects:
       for obj_coords in objects[copy_color]:
           for r, c in obj_coords:
              output_grid[r,c] = copy_color

    #highlight object
    if highlight_color is not None:
        if target_color in objects:
            for obj_coords in objects[target_color]:
                 output_grid = highlight_object(output_grid, obj_coords, input_grid[obj_coords[0][0], obj_coords[0][1]]) #reset to original


    if target_color in objects:
        for obj_coords in objects[target_color]:
           if (highlight_color in [input_grid[r,c] for r, c in obj_coords] ):
                output_grid = highlight_object(output_grid, obj_coords, highlight_color)


    # Mirror the output
    output_grid = mirror_vertical(output_grid)

    return output_grid
```
