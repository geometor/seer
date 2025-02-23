"""
The transformation aligns colored objects (red, blue, yellow) vertically while maintaining their relative horizontal positions. Objects move down by one row, unless this would cause them to overlap with an object of a different color.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    objects = []

    def dfs(r, c, color, obj_coords):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        obj_coords.append((r, c))
        dfs(r + 1, c, color, obj_coords)
        dfs(r - 1, c, color, obj_coords)
        dfs(r, c + 1, color, obj_coords)
        dfs(r, c - 1, color, obj_coords)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                obj_coords = []
                dfs(r, c, color, obj_coords)
                # Find top-left and dimensions
                min_r = min(coord[0] for coord in obj_coords)
                min_c = min(coord[1] for coord in obj_coords)
                max_r = max(coord[0] for coord in obj_coords)
                max_c = max(coord[1] for coord in obj_coords)
                objects.append({
                    'color': color,
                    'position': (min_r, min_c),
                    'shape': (max_r - min_r + 1, max_c - min_c + 1),
                    'pixels': obj_coords
                })
    return objects

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find objects
    objects = find_objects(input_grid)

    # Group by color for easier processing
    color_groups = {}
    for obj in objects:
        if obj['color'] not in color_groups:
            color_groups[obj['color']] = []
        color_groups[obj['color']].append(obj)


    # Apply transformation rules
    for color, objs in color_groups.items():
      for obj in objs:
            r, c = obj['position']
            height, width = obj['shape']
            new_r = r + 1

            # Check for overlap
            can_move = True
            for pixel_r, pixel_c in obj['pixels']:
                new_pixel_r = pixel_r + 1
                if new_pixel_r >= input_grid.shape[0]:
                    can_move = False #prevent it from going off the board
                    break
                if output_grid[new_pixel_r, pixel_c] != 0 and output_grid[new_pixel_r,pixel_c] != color:
                    can_move = False #check if occupied by a different color.
                    break

            if can_move:
                for pixel_r, pixel_c in obj['pixels']:
                    output_grid[pixel_r + 1, pixel_c] = color

            else: #it can't move, so keep it where it is.
                for pixel_r, pixel_c in obj['pixels']:
                    output_grid[pixel_r, pixel_c] = color

    return output_grid