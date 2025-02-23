"""
1. **Identify Objects:** The input is a grid. Define an "object" as a group of one or more contiguous pixels of the same color.  Contiguous includes adjacent pixels horizontally, vertically, *and diagonally*.
2. **Target Color:** Focus on pixels with the color white (value 0).
3. **Count Distinct Objects:** Count the number of distinct white objects in the input grid.
4. **Output:** Create a 1x1 output grid. The single cell's value is the total count of distinct white objects found in the input grid.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds distinct objects of a specified color in a grid.
    An object is a group of contiguous cells of the same color, including diagonals.
    """
    visited = set()
    objects = []

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        # Explore all 8 adjacent cells (up, down, left, right, and diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, current_object)
        

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid to count the distinct white objects
    """
    # Find distinct white objects, including diagonals
    white_objects = find_objects(np.array(input_grid), 0)

    # Count the number of distinct white objects
    count = len(white_objects)
    
    # the output grid will be 1 x 1 with value of the 'count'
    output_grid = np.array([[count]])
    
    return output_grid