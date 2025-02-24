"""
The transformation identifies connected shapes in the input grid and expands each shape by a factor of 3. Each identified shape is replicated with the original shape in the center of the expanded area. Pixels in the input that are not part of these identified objects are not included in the output. The output grid dimensions are 3x the input grid.
"""

import numpy as np
from scipy.ndimage import label

def get_objects(input_grid):
    """
    Identifies connected components (objects) in the input grid, excluding the background (0).
    Returns a list of coordinates and color for each object.
    """
    labeled_grid, num_objects = label(input_grid != 0)
    objects = []
    for i in range(1, num_objects + 1):  # Iterate through object labels (1, 2, ...)
        # create mask for current object
        object_mask = (labeled_grid == i)
        # extract color of this object
        object_color = np.unique(input_grid[object_mask])[0]

        # only process if object is not background color
        if object_color != 0:
            # find where object is in input_grid
            coords = np.where(object_mask)
            objects.append((coords, object_color))
    return objects

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows, output_cols = input_rows * 3, input_cols * 3
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Find the objects
    objects = get_objects(input_grid)

    # Expand each object's shape by factor of 3
    for coords, color in objects:
        for row, col in zip(coords[0], coords[1]):
            # center the expanded shape
            for r in range(row * 3 -1, row * 3 + 2):
                for c in range(col * 3 - 1, col * 3 + 2):
                  # check output grid boundaries, and add pixel
                  if 0 <= r < output_rows and 0 <= c < output_cols:
                      output_grid[r, c] = color

    return output_grid