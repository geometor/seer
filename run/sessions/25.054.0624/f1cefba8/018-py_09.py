"""
The transformation involves identifying an outer rectangle and a smaller, inner rectangle of a different color.
The inner rectangle's color expands to fill the outer rectangle completely within a combined bounding box, 
replacing the outer object's color. Background pixels that were adjacent (side or corner) to the inner are also filled by the inner color.
"""

import numpy as np

def find_objects(grid):
    """Finds the inner and outer objects based on color and size."""
    # Get unique colors, excluding black (background)
    unique_colors = np.unique(grid)
    unique_colors = unique_colors[unique_colors != 0]

    objects = []
    for color in unique_colors:
        rows, cols = np.where(grid == color)
        if len(rows) > 0:
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)
            objects.append({
                'color': color,
                'top_left': (min_row, min_col),
                'bottom_right': (max_row, max_col)
            })

    if len(objects) < 2:
      return None, None

    # Sort objects by area (assuming the largest is the outer object)
    objects.sort(key=lambda obj: (obj['bottom_right'][0] - obj['top_left'][0]) * (obj['bottom_right'][1] - obj['top_left'][1]), reverse=True)
    
    outer_object = objects[0]
    inner_object = objects[1]

    # check that the objects form rectangles
    outer_pixels = (outer_object['bottom_right'][0] - outer_object['top_left'][0] + 1) * (outer_object['bottom_right'][1] - outer_object['top_left'][1] + 1)
    inner_pixels = (inner_object['bottom_right'][0] - inner_object['top_left'][0] + 1) * (inner_object['bottom_right'][1] - inner_object['top_left'][1] + 1)
    if np.sum(grid == outer_object['color']) != outer_pixels or np.sum(grid == inner_object['color']) != inner_pixels:
      return None, None

    return outer_object, inner_object

def combined_bounding_box(outer_object, inner_object):
    """Calculates the combined bounding box of two objects."""
    min_row = min(outer_object['top_left'][0], inner_object['top_left'][0])
    min_col = min(outer_object['top_left'][1], inner_object['top_left'][1])
    max_row = max(outer_object['bottom_right'][0], inner_object['bottom_right'][0])
    max_col = max(outer_object['bottom_right'][1], inner_object['bottom_right'][1])
    return (min_row, min_col), (max_row, max_col)

def is_adjacent_to_inner(grid, row, col, inner_object):
    """Checks if a pixel is adjacent (horizontally, vertically, or diagonally) to the inner object."""
    inner_color = inner_object['color']
    rows, cols = np.where(grid == inner_color)
    if len(rows) == 0:  # if for some reason the color isn't found
       return False

    for r, c in zip(rows,cols):
       if abs(row - r) <= 1 and abs(col - c) <= 1:
          return True

    return False
    

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the outer and inner objects
    outer_object, inner_object = find_objects(input_grid)

    if outer_object is None or inner_object is None:
        return output_grid

    # Determine the combined bounding box
    top_left, bottom_right = combined_bounding_box(outer_object, inner_object)

    # Perform color replacement within the combined bounding box
    for row in range(top_left[0], bottom_right[0] + 1):
        for col in range(top_left[1], bottom_right[1] + 1):
            if output_grid[row, col] == outer_object['color']:
                output_grid[row, col] = inner_object['color']
            elif output_grid[row,col] == 0 and is_adjacent_to_inner(input_grid, row, col, inner_object):
                output_grid[row,col] = inner_object['color']
    return output_grid