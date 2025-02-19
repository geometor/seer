# 4c5c2cf0 • 002 • example_1 - CODE

---
```python
"""
The transformation involves making a horizontally mirrored copy of red structure, with an offset, and adding it to the output. The yellow structure remains invariant.
"""

import numpy as np

def get_objects_by_color(grid, color):
    """
    Finds the positions of all cells with a given color.
    """
    return np.array(np.where(grid == color)).T.tolist()

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Get the positions of red and yellow objects
    red_objects = get_objects_by_color(input_grid, 2)

    # Yellow objects remain the same, so no action needed

    # Mirror the red objects horizontally and add to output grid
    if (len(red_objects) > 0):
      max_x = max(obj[1] for obj in red_objects)
      min_x = min(obj[1] for obj in red_objects)

      for obj in red_objects:
         # Calculate offset to the right based on the shape
          new_x = obj[1] + 2 * (max_x - obj[1] + 1) # obj[1] is column (x) and obj[0] is row(y)
          output_grid[obj[0], new_x] = 2

      # Add a second mirrow, this time to the left
      for obj in red_objects:
          new_x = obj[1] - 2 * (obj[1] - min_x  + 1)
          if (new_x >= 0):
            output_grid[obj[0], new_x] = 2

    return output_grid
```

