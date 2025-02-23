# f1cefba8 • 016 • refine_coder

---
```python
"""
The transformation involves identifying an outer rectangle and a smaller, inner rectangle of a different color.
The inner rectangle's color "creeps" vertically, replacing the color of the outer rectangle, until the inner shape
fills the available space within the outer rectangle's boundaries, or reaches the edge of the grid.
"""

import numpy as np

def find_object(grid, colors):
    """Finds the bounding box of an object with a specific color."""
    for color in colors:
        rows, cols = np.where(grid == color)
        if len(rows) > 0:
            min_row, max_row = np.min(rows), np.max(rows)
            min_col, max_col = np.min(cols), np.max(cols)
            return (min_row, min_col), (max_row, max_col), color  # Return color too
    return None, None, None

def get_central_column(top_left, bottom_right):
    """Calculates the central column index."""
    _, min_col = top_left
    _, max_col = bottom_right
    central_col = (min_col + max_col) // 2
    return central_col

def creeping(grid, inner_top_left, inner_bottom_right, outer_top_left, outer_bottom_right, inner_color):
    """Expands the inner object vertically within the outer object's bounds."""
    output_grid = np.copy(grid)
    inner_min_row, inner_min_col = inner_top_left
    inner_max_row, inner_max_col = inner_bottom_right
    outer_min_row, outer_min_col = outer_top_left
    outer_max_row, outer_max_col = outer_bottom_right

    # iterate over each column in the inner rectangle
    for col in range(inner_min_col, inner_max_col + 1):
       # creep up
       for row in range(inner_min_row - 1, -1, -1):
           if row >= outer_min_row:
               if output_grid[row,col] != 0:
                 output_grid[row, col] = inner_color
           else:
              break
       # creep down
       for row in range(inner_max_row + 1, grid.shape[0]):
            if row <= outer_max_row:
               if output_grid[row,col] != 0:
                   output_grid[row,col] = inner_color
            else:
               break
    return output_grid

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Define potential outer and inner colors
    outer_colors = [2, 1]  # Red, Blue
    inner_colors = [3, 4]  # Green, Yellow

    # Find the outer and inner rectangles
    outer_top_left, outer_bottom_right, outer_color = find_object(input_grid, outer_colors)
    inner_top_left, inner_bottom_right, inner_color = find_object(input_grid, inner_colors)
    if outer_color is None or inner_color is None:
        return output_grid

    
    # Perform creeping
    output_grid = creeping(output_grid, inner_top_left, inner_bottom_right, outer_top_left, outer_bottom_right, inner_color)

    return output_grid
```
