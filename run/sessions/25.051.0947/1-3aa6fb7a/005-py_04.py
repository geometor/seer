"""
The transformation rule is similar to the previous example but with adjustments for multiple azure objects and blue cell placement and some object identification strategy:

1.  **Identify Azure Objects:** Locate all azure (color 8) objects in the input grid. There are three separate azure objects.

2.  **Preserve Azure Objects:** Copy all azure colored areas to the output grid, in their respective locations.

3. **Introduce Blue Pixel, Top:** Identify the azure object with the upper-leftmost coordinate. Add a blue (color 1) pixel to the left of its upper-rightmost coordinate.

4.  **Introduce Blue Pixel, Middle:** Identify the object whose upper-leftmost coordinate has the lowest row value among the remaining objects. Add a blue (color 1) to the left of its upper-rightmost coordinate.

5.  **Introduce Blue Pixel, Bottom:** Out of the remaining objects, find the one whose bottom-leftmost coordinate have the lowest row value. Add one blue pixel (color 1) to the left of this object's bottom-rightmost cell.

In summary, the transformation preserves all azure objects, introducing three strategically placed blue pixels in direct relation to existing azure objects positions.
"""

import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
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
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find azure objects
    azure_objects = find_objects(input_grid, 8)

    # Sort objects by upper-leftmost coordinate, then by bottom-leftmost
    azure_objects.sort(key=lambda obj: (min(y for x, y in obj), min(x for x,y in obj)))

    # Add blue pixel for the top object
    if len(azure_objects) >= 1:
        top_object = azure_objects[0]
        #find upper-rightmost coordinate in the first object
        top_rightmost = max(top_object, key=lambda x: (x[1], -x[0]))

        # Add blue pixel to its left, ensuring not exceed boundary
        if(top_rightmost[1] - 1 >= 0):
            output_grid[top_rightmost[0], top_rightmost[1] - 1] = 1
    
    azure_objects_remaining = azure_objects[1:]

    # Sort remaining objects by uppermost coordinate, then leftmost.
    azure_objects_remaining.sort(key=lambda obj: (min(x for x,y in obj), min(y for x, y in obj)))

    if len(azure_objects_remaining) >= 1:
        middle_object = azure_objects_remaining[0]

        #find upper-rightmost coordinate
        middle_rightmost = max(middle_object, key = lambda x: (x[1],-x[0]))

        if(middle_rightmost[1] -1 >= 0):
            output_grid[middle_rightmost[0], middle_rightmost[1] - 1] = 1
    
    azure_objects_remaining = azure_objects_remaining[1:]
    # Sort remaining objects by lowermost coordinate, then leftmost.
    azure_objects_remaining.sort(key=lambda obj: (max(x for x,y in obj), min(y for x, y in obj)))

    #add blue pixel for the second object
    if len(azure_objects_remaining) >= 1:
        bottom_object = azure_objects_remaining[0]

        # Find the bottom-rightmost coordinate in second object
        bottom_rightmost = max(bottom_object, key=lambda x: (x[1],x[0]))

        #add blue pixel to the left of its downmost coordinate, ensuring not exceed boundary
        if(bottom_rightmost[1] -1 >= 0):
            output_grid[bottom_rightmost[0] , bottom_rightmost[1]-1] = 1

    return output_grid