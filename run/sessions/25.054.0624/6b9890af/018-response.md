# 6b9890af • 018 • refine_coder

---
```python
"""
Combines a large red rectangular outline and a smaller filled rectangle of another color into a new grid. The transformation preserves the large rectangle's outline and places the smaller, resized filled rectangle just inside the top border of the large shape. The smaller shape is stretched horizontally to fit inside red outline, and the height is distance between the top of the original shape and bottom of outer shape.
"""

import numpy as np

def find_bounding_box(grid, color):
    """Finds the bounding box of an object with the specified color."""
    coords = np.argwhere(grid == color)
    if coords.size == 0:
        return None
    min_y, min_x = np.min(coords, axis=0)
    max_y, max_x = np.max(coords, axis=0)
    return (min_y, min_x), (max_y, max_x)

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    # 1. Find the Red Rectangle Outline:
    red_bbox = find_bounding_box(input_grid, 2)
    if red_bbox is None:
        return input_grid  # Return original if no red outline
    (red_min_y, red_min_x), (red_max_y, red_max_x) = red_bbox

    # 2. Find the Inner Filled Rectangle:
    inner_color = None
    for color in range(10):  # check for all non-red colors
        if color != 2:
          inner_bbox = find_bounding_box(input_grid,color)
          if inner_bbox is not None:
            inner_color = color
            break
    if inner_color is None:
        return input_grid

    (inner_min_y, inner_min_x), (inner_max_y, inner_max_x) = inner_bbox

    # 3. Determine output grid size based on red outline:
    output_height = red_max_y - red_min_y + 1
    output_width = red_max_x - red_min_x + 1
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # 4. Draw Red Outline:
    for x in range(output_width):
        output_grid[0, x] = 2  # Top border
        output_grid[output_height - 1, x] = 2  # Bottom border
    for y in range(output_height):
        output_grid[y, 0] = 2  # Left border
        output_grid[y, output_width - 1] = 2  # Right border


    # 5. Calculate Inner Rectangle Dimensions and Position:
    start_y = 1  # One pixel below top
    start_x = 1  # One pixel from left

    inner_width = output_width - 2
    inner_height = red_max_y - inner_min_y + 1


    # 6. Draw Inner Rectangle:
    for y in range(inner_height):
      for x in range(inner_width):
        if start_y + y < output_height and start_x + x < output_width:
            output_grid[start_y + y, start_x + x] = inner_color

    return output_grid
```
