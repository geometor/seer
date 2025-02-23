# 1f0c79e5 • 006 • refine_coder

---
```python
"""
1.  **Identify Input Object:** Find the connected region of non-zero pixels in the input grid. This is the "input object."
2.  **Determine Dominant Color**: Identify the *inner* color in the input object, this will be the color that fills the majority of the output
3.  **Calculate Output Size:** Calculate the number of non-zero pixels within the input object (its "area"). Determine the output grid's dimensions.  The area will not always directly map, but will be used to determine the output size. The output grid size appears to follow the pattern where one of the output dimension equals `ceil(input_area / 2 + 1)`.
4. **Determine Output Dimensions:** The examples all use one dimension of the output to be consistent with ceil(input_area / 2) + 1.
5.  **Spiral Fill:** Starting from the top-left corner (0, 0) of the output grid, fill the grid in a clockwise spiral pattern using the dominant color.  The filling doesn't involve placing the entire *input object* repeatedly. Instead, it places individual pixels of the dominant color. The key is to correctly implement the spiral traversal:
    *   Start at (0, 0).
    *   Move right as far as possible, placing the dominant color.
    *   Move down as far as possible, placing the dominant color.
    *   Move left as far as possible, placing the dominant color.
    *   Move up as far as possible, placing the dominant color.
    *   Repeat, reducing the length of each movement by one each time a corner is turned, until the entire output grid is filled.
"""

import numpy as np
from math import ceil

def get_object(grid):
    # Find non-zero pixels
    non_zero_pixels = np.argwhere(grid != 0)

    # if no object return none
    if len(non_zero_pixels) == 0:
      return None, None

    # Find top-left and bottom-right corners
    min_row, min_col = non_zero_pixels.min(axis=0)
    max_row, max_col = non_zero_pixels.max(axis=0)

    # Create object mask
    object_mask = (grid[min_row:max_row+1, min_col:max_col+1] != 0)

    # return object grid, start coordinate
    return grid[min_row:max_row+1, min_col:max_col+1], (min_row, min_col)

def get_dominant_color(obj):
    # get the counts of each color
    unique_colors, counts = np.unique(obj, return_counts=True)
    # get the counts, ignoring zeros
    color_counts = {color: count for color, count in zip(unique_colors, counts) if color != 0}
    # get dominant
    if not color_counts:  # handle empty
        return 0
    dominant_color = max(color_counts, key=color_counts.get)
    return dominant_color

def calculate_output_dimensions(input_area):
    # determine one dimension of the output matrix
    dim = ceil(input_area / 2) + 1
    return (dim, 9) # hard coded to 9 for now

def spiral_fill(output_grid, dominant_color):
    # Spiral fill logic
    rows, cols = output_grid.shape
    top, left = 0, 0
    bottom, right = rows - 1, cols - 1
    dr, dc = 0, 1  # Initial direction: right

    while top <= bottom and left <= right:
        if dr == 0 and dc == 1:  # Move right
            for i in range(left, right + 1):
                output_grid[top, i] = dominant_color
            top += 1
        elif dr == 1 and dc == 0:  # Move down
            for i in range(top, bottom + 1):
                output_grid[i, right] = dominant_color
            right -= 1
        elif dr == 0 and dc == -1:  # Move left
            for i in range(right, left - 1, -1):
                output_grid[bottom, i] = dominant_color
            bottom -= 1
        elif dr == -1 and dc == 0:  # Move up
            for i in range(bottom, top - 1, -1):
                output_grid[i, left] = dominant_color
            left += 1

        # Change direction
        dr, dc = dc, -dr

def transform(input_grid):
    # Find the object
    obj, _ = get_object(input_grid)

    # if not object found, return the original
    if obj is None:
        return np.zeros((9,9), dtype=int)

    # get dominant color
    dominant_color = get_dominant_color(obj)

    # calculate input area
    input_area = np.sum(obj != 0)

    # determine output_grid dimensions
    output_dimensions = calculate_output_dimensions(input_area)
    output_grid = np.zeros(output_dimensions, dtype=int)

    # perform spiral fill of output grid
    spiral_fill(output_grid, dominant_color)

    return output_grid
```
