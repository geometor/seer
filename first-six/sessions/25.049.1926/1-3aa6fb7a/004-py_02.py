"""
The transformation rule can be summarized as: Find every separated figure colored in azure. Find the top-right pixel of this object. Convert this pixel to blue.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds connected components of a specific color in the grid.
    Returns a list of lists, where each inner list contains the coordinates of an object's pixels.
    """
    visited = set()
    objects = []

    def dfs(row, col, current_object):
        """Depth-First Search helper function."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.append((row, col))
        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def find_top_right(object_pixels):
    """
    Finds the top-right pixel of a set of pixels representing an object.
    """
    # Sort by column (ascending) and then by row (descending)
    sorted_pixels = sorted(object_pixels, key=lambda p: (-p[0], p[1]))
    return sorted_pixels[-1]
    

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Find every separated figure colored in azure. Find the top-right pixel of this object. Convert this pixel to blue.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find all azure (color 8) objects
    azure_objects = find_objects(output_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Find the top-right pixel of the object
        top_right_pixel = find_top_right(obj)

        # Change the color of the top-right pixel to blue (color 1)
        output_grid[top_right_pixel[0], top_right_pixel[1]] = 1
        
    return output_grid