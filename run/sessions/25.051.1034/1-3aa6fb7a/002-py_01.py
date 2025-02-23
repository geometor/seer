"""
The transformation rule is to identify azure (color 8) objects and add a blue (color 1) pixel adjacent to each of them. 
The blue pixel is added to the right of the bottom pixel of the vertical azure line.
The blue pixel is added to the left of the top pixel of the horizontal azure line.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    
    # Find objects of color 8 (azure)
    azure_objects = find_objects(input_grid, 8)
    
    # Iterate through each azure object
    for obj in azure_objects:
        # Sort the object coordinates to determine shape (vertical or horizontal line)
        obj.sort()
        
        if obj[1][0] > obj[0][0]: #obj[0][0] is row, obj[0][1] is column
            # Vertical line: Add blue pixel to the right of the bottom pixel
            row = obj[-1][0] 
            col = obj[-1][1] + 1
            if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:
              output_grid[row, col] = 1
        elif obj[1][1] > obj[0][1]:
             #horizontal line
            row = obj[0][0]
            col = obj[0][1] - 1
            if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:
              output_grid[row,col] = 1
    
    return output_grid