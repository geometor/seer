"""
1. Identify Azure Objects: Find all contiguous regions (objects) of the color azure (8).

2. Iterate through Pixels: For *each* azure pixel within each azure object:

    *   Check for Vertical Adjacency: If any other azure pixel is *directly above or below* the azure pixel, add a blue pixel *immediately to the right* of the current azure.

    *   Check for horizontal Adjacency: If any other azure pixel is *directly to the left or right* of the current azure, add a blue pixel *immediately to the left* of the current azure.

    * If an azure object is not adjacent to any other azure pixel, do not add any pixel.
"""

import numpy as np

def find_objects(grid, color):
    # Find all objects of a specific color in the grid.
    objects = []
    visited = set()

    def is_valid(x, y):
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_object):
        if (x, y) in visited or not is_valid(x, y) or grid[x, y] != color:
            return
        visited.add((x, y))
        current_object.append((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(x + dx, y + dy, current_object)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and (x, y) not in visited:
                current_object = []
                dfs(x, y, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    # Find all objects with color 8 (azure)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Iterate through each pixel in the object
        for x, y in obj:
            has_vertical_neighbor = False
            has_horizontal_neighbor = False

            # Check for neighbors
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < input_grid.shape[0] and 0 <= ny < input_grid.shape[1] and input_grid[nx, ny] == 8:
                    if dx == 0:  # Horizontal neighbor
                        has_horizontal_neighbor = True
                    if dy == 0:  # Vertical neighbor
                        has_vertical_neighbor = True
            # Add blue pixel based on the presence of neighbors
            if has_vertical_neighbor:
                new_x, new_y = x , y + 1 #to the right
                if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
                    output_grid[new_x,new_y] = 1
            if has_horizontal_neighbor:
                new_x, new_y = x , y - 1 #to the left
                if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
                    output_grid[new_x,new_y] = 1
    return output_grid