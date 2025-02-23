"""
The transformation identifies the two azure L-shaped objects and changes their interior corner pixel to blue. All other pixels remain unchanged.
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of sets, where each set contains the coordinates of an object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = set()
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_l_corner(object_coords):
    """
    Finds the interior corner of an L-shaped object.
    Returns the coordinates of the corner pixel.
    """
    # Convert the set of coordinates to a numpy array for easier manipulation.
    coords = np.array(list(object_coords))

    # Iterate to check for pixels sorrounded by 2 neighbors
    for r,c in object_coords:
        neighbors = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (r + dr, c + dc) in object_coords:
                neighbors +=1
        if neighbors == 2:
          return (r,c)

    return None  # Should not happen if the object is truly L-shaped

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Find azure (color 8) L-shaped objects and change their interior corner pixel to blue (color 1).
    """
    # Initialize output_grid as a copy of input_grid
    output_grid = input_grid.copy()

    # Find all azure objects
    azure_objects = find_objects(input_grid, 8)

    # Iterate through each azure object
    for obj in azure_objects:
        # Find the corner of the L-shape
        corner = find_l_corner(obj)

        # If a corner is found, change its color to blue
        if corner:
            output_grid[corner] = 1

    return output_grid