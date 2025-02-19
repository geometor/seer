"""
The blue shape is duplicated and mirrored, based on the first green point. A new object is created by mirroring the blue object using the position of a green object as the axis of symmetry.
The yellow shapes are copied and some are mirrored. A copy of the yellow shape is mirrored relative to the red object on the bottom right.
The other yellow shapes are copied and translated.
The red single-cell objects and the green single cell are preserved without changes.
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
    # Find blue objects
    blue_objects = find_objects(input_grid, 1)
    # Find yellow objects
    yellow_objects = find_objects(input_grid, 4)

    #Mirror Blue object
    for green_object in green_objects:
        green_ref_row, green_ref_col = green_object[0]
        for blue_object in blue_objects:
            # Mirror the blue object
            mirrored_blue_object = mirror_object(blue_object, (green_ref_row, green_ref_col))
            # Place the mirrored object in the output grid
            for r, c in mirrored_blue_object:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                    output_grid[r, c] = 1
        break #Only first object

    #Mirror some Yellow object
    if len(red_objects) > 0:
        red_ref_row, red_ref_col = red_objects[-1][0] #Bottom-right

    for yellow_object in yellow_objects:
        # Mirror the yellow object
        mirrored_yellow_object = mirror_object(yellow_object, (red_ref_row, red_ref_col))
        # Place the mirrored object in the output grid
        for r, c in mirrored_yellow_object:
            if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1]:
                output_grid[r, c] = 4
    # Translate some yellow object
    if len(red_objects) >= 2:
        
      red_obj1 = red_objects[0][0]
      red_obj2 = red_objects[1][0]
      for yellow_object in yellow_objects:
          # Calculate translation based on the FIRST yellow object as reference
          yellow_ref_row, yellow_ref_col = yellow_object[0]
          #First
          row_translation = red_obj1[0] - yellow_ref_row
          col_translation = red_obj1[1] - yellow_ref_col
          translated_yellow = translate_object(yellow_object, row_translation, col_translation)

          for r,c in translated_yellow:
              output_grid[r,c] = 4

    return output_grid.tolist()