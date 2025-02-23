"""
The azure and yellow objects are mirrored based on the position of the green and red, respectively. The single-cell red and green objects do not change.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        """Depth-first search to find contiguous regions."""
        if (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1] and
                grid[r, c] == color and (r, c) not in visited):
            visited.add((r, c))
            current_object.append((r, c))
            dfs(r + 1, c, current_object)
            dfs(r - 1, c, current_object)
            dfs(r, c + 1, current_object)
            dfs(r, c - 1, current_object)
        return current_object

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c, []))
    return objects

def mirror_object(object_coords, ref_coords):
    """Mirrors the object coordinates with respect to the ref object coordinates."""
    mirrored_coords = []
    r_ref, c_ref = ref_coords
    for r, c in object_coords:
        mirrored_coords.append((r + 2 * (r_ref - r), c + 2 * (c_ref - c)))
    return mirrored_coords
def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find red objects
    red_objects = find_objects(input_grid, 2)
    # Find green objects
    green_objects = find_objects(input_grid, 3)
    # Find azure objects
    azure_objects = find_objects(input_grid, 8)
    # Find yellow objects
    yellow_objects = find_objects(input_grid, 4)
    #Mirror Yellow object
    for red_object in red_objects:
        red_ref_row, red_ref_col = red_object[0]
        for yellow_object in yellow_objects:
            # Mirror the yellow object
            mirrored_yellow_object = mirror_object(yellow_object, (red_ref_row, red_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_yellow_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 4
    #Mirror Azure Object
    for green_object in green_objects:
        green_ref_row, green_ref_col = green_object[0]
        for azure_object in azure_objects:
            # Mirror the yellow object
            mirrored_azure_object = mirror_object(azure_object, (green_ref_row, green_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_azure_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 8
    return output_grid.tolist()