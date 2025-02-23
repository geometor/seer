"""
The rule identifies separated clusters of color 8 (azure), then calculates the new coordinates for a color 1 (blue)
object using the minimum x-coordinate and maximum y-coordinate of the azure object, decrementing the y-coordinate by one.
The original azure clusters remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specific color in the grid.
    Returns a list of coordinates where the object's cells are located.
    """
    coords = []
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return []

        visited[r, c] = True
        coords = [(r, c)]

        coords.extend(dfs(r + 1, c))
        coords.extend(dfs(r - 1, c))
        coords.extend(dfs(r, c + 1))
        coords.extend(dfs(r, c - 1))
        return coords

    objects_coords = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                objects_coords.append(dfs(r, c))
    return objects_coords

def transform(input_grid):
    """
    Transforms the input grid according to the identified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj_coords in azure_objects:
        #find x and y coordinates
        x_coords = [coord[0] for coord in obj_coords]
        y_coords = [coord[1] for coord in obj_coords]

        #find min and max of x and y coordinate
        min_x = min(x_coords)
        max_y = max(y_coords)

        # calculate new object position , min_x, max_y - 1
        new_x = min_x
        new_y = max_y - 1
        if 0 <= new_x < output_grid.shape[0] and 0 <= new_y < output_grid.shape[1]:
                output_grid[new_x, new_y] = 1

    return output_grid