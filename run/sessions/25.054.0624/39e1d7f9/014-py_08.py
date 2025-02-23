"""
The transformation preserves the azure lines and fills specific white regions bounded by these lines with yellow, leaving all other colored regions.
"""

import numpy as np

def get_objects_by_color(grid, color):
    """Find contiguous regions of the specified color."""
    mask = (grid == color)
    labeled_array, num_features = ndimage.label(mask)
    objects = []
    for i in range(1, num_features + 1):
        objects.append(np.where(labeled_array == i))
    return objects
    

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify azure lines (horizontal and vertical)
    azure_lines = get_objects_by_color(input_grid, 8)

    # Find white regions and process the grid
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 0: # if pixel is white
          # Check if in top or left section bounded by azure(8) lines
            is_top = False
            is_left = False

            #check top
            for ar, ac in zip(*azure_lines[0]):
                if ac == c and ar < r :
                  is_top = True
                  break
                if ar > r:
                   break

            #check left
            for ar, ac in zip(*azure_lines[0]):
                if ar == r and ac < c:
                    is_left = True
                    break
                if ac > c:
                    break


            if is_top or is_left:
                output_grid[r,c] = 4 # color it yellow

    return output_grid