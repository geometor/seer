# eb5a1d5d • 002 • example_1 • investigate_coder

---
```python
"""
The transformation extracts the innermost colored rectangle from the input and reduces the colored region to one pixel. The border of the output is the outermost color of the input.
"""

import numpy as np

def find_innermost_rectangle(grid):
    """Finds the innermost rectangle's color and its surrounding rectangle's color."""
    rows, cols = grid.shape
    outermost_color = grid[0, 0]
    innermost_color = None
    surrounding_color = None

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != outermost_color:
                surrounding_color = grid[r,c]
                break
        if surrounding_color is not None:
             break

    for r in range(rows):
      for c in range(cols):
        if grid[r,c] != outermost_color and grid[r,c] != surrounding_color:
          innermost_color = grid[r,c]
          return innermost_color, surrounding_color, outermost_color

    return innermost_color, surrounding_color, outermost_color
    

def transform(input_grid):
    """Transforms the input grid to the output grid based on the nested rectangles."""

    # Find the innermost and surrounding rectangle colors
    innermost_color, surrounding_color, outermost_color = find_innermost_rectangle(np.array(input_grid))

    # Initialize the output grid (5x5) with the outermost color
    output_grid = np.full((5, 5), outermost_color)

    # Set the center pixel to the innermost color
    if innermost_color != None:
      output_grid[2, 2] = innermost_color

    # set the other pixels to the surrounding color
    if surrounding_color != None:
      for i in range(1,4):
        for j in range(1,4):
          if output_grid[i,j] == outermost_color:
            output_grid[i,j] = surrounding_color

    return output_grid.tolist()
```
