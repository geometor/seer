# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
Identifies azure (8) colored L-shaped objects and recolors the corner cell of each object that is furthest away from other objects to blue (1).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color.

    Args:
        grid: The input grid.
        color: The color to search for.

    Returns:
        A list of objects, where each object is a set of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or grid[row, col] != color
        ):
            return
        visited.add((row, col))
        current_object.add((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = set()
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def calculate_centroid(object_coords):
    """Calculates the centroid of a set of coordinates."""
    if not object_coords:
        return None
    sum_row = sum(coord[0] for coord in object_coords)
    sum_col = sum(coord[1] for coord in object_coords)
    return (sum_row / len(object_coords), sum_col / len(object_coords))

def find_furthest_corner(object_coords, other_objects_coords):
    """
    Finds the corner cell within an object that is furthest from the centroids of other objects.
    
    Args:
        object_coords: Coordinates of the object.
        other_objects_coords: list of coordinates of other objects

    Returns:
        Coordinates of the furthest corner.
    """
    
    #if there are no other objects, return the centroid of current object
    if not other_objects_coords:
        return calculate_centroid(object_coords)

    # Calculate the centroid of all the other objects together
    all_other_coords = set()
    for other_obj in other_objects_coords:
        all_other_coords.update(other_obj)
    
    other_centroid = calculate_centroid(all_other_coords)

    #find the corner cells
    corner_cells = []
    for cell in object_coords:
        neighbors = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = cell[0] + dx, cell[1] + dy
            if (new_row, new_col) in object_coords:
                neighbors +=1
        if neighbors == 2:
            corner_cells.append(cell)

    #find the furthest corner from other objects centroid
    furthest_corner = None
    max_distance = -1

    for corner in corner_cells:
        distance = (corner[0] - other_centroid[0]) ** 2 + (corner[1] - other_centroid[1]) ** 2
        if distance > max_distance:
            max_distance = distance
            furthest_corner = corner
            
    return furthest_corner

def transform(input_grid):
    """
    Transforms the input grid by recoloring specific cells of azure objects to blue.
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)

    # Find all azure objects
    azure_objects = find_objects(output_grid, 8)
    
    #create list to store coordinates of all objects other than current
    other_objects_coords = []

    # Iterate through each azure object
    for i, azure_object in enumerate(azure_objects):
        #get coordinates of all other objects
        other_objects_coords = azure_objects[:i] + azure_objects[i+1:]
        
        # Find the corner cell furthest away from other objects
        furthest_cell = find_furthest_corner(azure_object, other_objects_coords)
        
        if furthest_cell:
            # Recolor the furthest cell to blue (1)
            output_grid[furthest_cell[0], furthest_cell[1]] = 1

    return output_grid
```
