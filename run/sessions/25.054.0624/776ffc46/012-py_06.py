"""
1.  **Object Identification:** Identify all distinct objects in the grid. An object is a group of connected pixels of the same color (diagonal connections are allowed).

2.  **Key Colors:** Focus on objects colored gray (5), green (3), and blue (1).

3.  **Gray Containers:** Consider gray (5) objects as potential "containers."

4.  **Shape Matching:** For each blue (1) object:
    *   Compare its shape to the shape of *every* green (3) object *anywhere* in the grid.
    *   Two objects have the same shape if their pixel configurations are identical, regardless of their position within the grid. Only the relative positions of pixels within each object matter.

5.  **Transformation:** If a blue (1) object's shape matches a green (3) object's shape, change all pixels of the blue object to green (3).

6. **Preservation**: All objects, not blue, or all blue shapes that do *not* have a matching shape, are not changed.
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

def is_shape_match(target_obj, reference_obj):
    """
    Checks if two objects have the same shape configuration.
    """
    return get_shape_configuration(target_obj) == get_shape_configuration(reference_obj)


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # Identify  green, and blue objects
    green_objects = [obj for obj in objects if input_grid[obj[0]] == 3]
    blue_objects = [obj for obj in objects if input_grid[obj[0]] == 1]

    # Iterate through blue objects and check for shape matches with any green object
    for blue_obj in blue_objects:
        for green_obj in green_objects:
            if is_shape_match(blue_obj, green_obj):
                for r, c in blue_obj:
                    output_grid[r, c] = 3  # Change blue to green
                break  # Move to the next blue object after a match

    return output_grid