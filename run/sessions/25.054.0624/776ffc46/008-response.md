# 776ffc46 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation identifies disconnected shapes of blue (color 1) pixels.
If a blue shape has a shape of the same configuration and color directly above it,
AND that same shape is green (color 3) and within a larger gray (color 5) shape,
then the blue shape's color is changed to green. Other objects and the background
remain unchanged.
"""

import numpy as np

def find_objects(grid):
    """
    Identifies distinct, contiguous regions of non-background (non-zero) pixels.
    Returns a list of objects, where each object is a list of (row, col) tuples.
    """
    visited = set()
    objects = []

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, color, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            dfs(r + dr, c + dc, color, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0 and (r, c) not in visited:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append(current_object)
    return objects

def get_shape_configuration(obj):
    """
    Returns a simplified representation of the object's shape as a set of
    relative (row, col) offsets from the top-left corner of its bounding box.
    """
    min_row = min(r for r, _ in obj)
    min_col = min(c for _, c in obj)
    return {(r - min_row, c - min_col) for r, c in obj}

def object_at_location(objects, location):
    """
    Checks if any object in the list of objects occupies the given location.

    Args:
    objects: A list of objects where each object is a list of (row, col) tuples.
    location: A (row, col) tuple representing the location to check.

    Returns:
        The object at the given location if exists, otherwise None
    """
    row, col = location
    for obj in objects:
        if (row,col) in obj:
            return obj
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # Find the green shape inside the gray shape
    gray_object = None
    green_object = None
    for obj in objects:
        color = input_grid[obj[0]]  # Get color from a pixel in the object
        if color == 5:
            gray_object = obj
        elif color == 3:
            green_object = obj
    
    # Find the relative configuration of the green interior
    if gray_object and green_object:
        
        gray_min_row = min(r for r, _ in gray_object)
        gray_min_col = min(c for _, c in gray_object)
        
        green_relative_config = get_shape_configuration(green_object)


        # Iterate through blue objects
        for obj in objects:
            if input_grid[obj[0]] == 1:  # if its blue
                obj_config = get_shape_configuration(obj)  # calculate its relative configuration
                
                #Find object directly above
                first_pixel_row, first_pixel_col = obj[0]
                
                #look up, assuming the configuration is the same size, find offset from first pixel
                offset_r = 0
                offset_c = 0
                
                if len(obj_config) == len(green_relative_config):  # quick size check for optimization
                    for r, c in obj_config:
                        if (r,c) in green_relative_config:
                            offset_r += r
                            offset_c += c
                    # Check if there is a '3' colored shape above it
                    potential_match_loc = (first_pixel_row - offset_r -1, first_pixel_col-offset_c) # -1 to go "above"
                    
                    obj_above = object_at_location(objects, potential_match_loc) #find pixel at location
                
                    if obj_above: #if something is there
                        if input_grid[obj_above[0]] == 3: # check color
                            if get_shape_configuration(obj_above) == green_relative_config:  # Correct Configuration Above

                                #check if the shape above is inside a gray object
                                obj_row, obj_col = obj_above[0]
                                gray_check_loc = (obj_row - (gray_min_row - green_object[0][0]), obj_col - (gray_min_col - green_object[0][1]))

                                if object_at_location(objects,gray_check_loc) == gray_object:

                                    for r, c in obj:  # change all instances of this object
                                        output_grid[r, c] = 3
    return output_grid
```
