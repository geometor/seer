"""
The yellow cross is duplicated and moved around based on the green points. The green object are not impacted.
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

def translate_object(object_coords, row_translation, col_translation):
    translated_coords = []
    for r,c in object_coords:
        new_r = r + row_translation
        new_c = c + col_translation
        if 0<= new_r < 13 and 0<= new_c < 13:
             translated_coords.append((new_r, new_c))
    return translated_coords

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)

    # Find green objects
    green_objects = find_objects(input_grid, 3)

    # Find yellow objects
    yellow_objects = find_objects(input_grid, 4)

    for green_object in green_objects:
        gr, gc = green_object[0] #Consider only the position

        for yellow_object in yellow_objects:
                # Calculate translation based on the FIRST yellow object as reference
                yellow_ref_row, yellow_ref_col = yellow_object[0]
                row_translation = gr - yellow_ref_row
                col_translation = gc - yellow_ref_col
                translated_yellow = translate_object(yellow_object, row_translation, col_translation)

                for r,c in translated_yellow:
                    output_grid[r,c] = 4

    return output_grid.tolist()