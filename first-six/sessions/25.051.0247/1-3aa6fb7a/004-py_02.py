"""
The transformation rule is as follows:
1. Identify all azure (color 8) objects in the input grid.
2. Preserve these objects in the output grid without any changes.
3. For each azure object:
    a. If the object is on the left side of the grid (x coordinate of top-left corner < grid width / 2),
       add a blue (color 1) cell immediately to its right, at the vertical midpoint of the object.
    b. If the object is on the right side of the grid (x coordinate of top-left corner >= grid width / 2),
       add a blue (color 1) cell immediately to its left, at the vertical midpoint of the object.
4. The rest of the grid (background color 0) remains unchanged.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, obj):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        obj.append((r, c))
        dfs(r + 1, c, obj)
        dfs(r - 1, c, obj)
        dfs(r, c + 1, obj)
        dfs(r, c - 1, obj)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                obj = []
                dfs(r, c, obj)
                objects.append(obj)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find the azure (color 8) objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Sort the object coordinates to find the top-left position.
        obj.sort()
        # calculate object height.
        height = obj[-1][0] - obj[0][0] + 1

        if obj[0][1] < input_grid.shape[1] / 2: # Left side object
            
            # find x coordinate to put the new blue pixel.
            x = obj[0][0] + height // 2

            # find y coordinate.
            y = obj[0][1] + 1
            
            #check the coordinate
            if 0 <= x < output_grid.shape[0] and 0 <= y < output_grid.shape[1]:
                # Add a blue (color 1) cell to the immediate right
                output_grid[x, y] = 1

        else:  # Right side object

            # find x coordinate to put the new blue pixel.
            x = obj[0][0] + height // 2
            
            # find y coordinate.
            y = obj[0][1] -1

            if 0 <= x < output_grid.shape[0] and 0 <= y < output_grid.shape[1]:          
                # Add a blue (color 1) cell to the immediate left
                output_grid[x,y] = 1

    return output_grid