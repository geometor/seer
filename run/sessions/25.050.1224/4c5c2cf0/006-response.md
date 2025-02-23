# 4c5c2cf0 • 006 • example_3 - CODE

---
```python
"""
The transformation involves creating a horizontally mirrored copy of the blue structure and adding this copy to the output, centering it horizontally with respect to the azure shape. The positions of azure objects remain invariant.
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

    # Get the positions of azure and blue objects
    azure_objects = get_objects_by_color(input_grid, 8)
    blue_objects = get_objects_by_color(input_grid, 1)

    # Azure objects remain the same, so no action needed

    # Mirror the blue objects horizontally and add to output grid
    if (len(blue_objects) > 0 and len(azure_objects) > 0) :

      # Calculate approximate center column of azure structure
      azure_center_col = int(np.mean([obj[1] for obj in azure_objects]))

      # Find the minimum and maximum columns occupied by blue pixels
      min_x = min(obj[1] for obj in blue_objects)
      max_x = max(obj[1] for obj in blue_objects)
    
      # Calculate offset based on center of azure shape
      blue_width = max_x - min_x + 1
      blue_middle_col = (min_x + max_x) // 2
    
      offset = (azure_center_col - blue_middle_col)
    
      for obj in blue_objects:
          new_x = obj[1] + 2 * (offset - obj[1] // 2)

          # If the mirrored position is within bounds, set the pixel to blue
          if 0 <= new_x < input_grid.shape[1]: # Check bounds
            output_grid[obj[0]][new_x] = 1

      # Calculate offset based on center of azure shape
      offset = (azure_center_col - blue_middle_col) - blue_width
    
      for obj in blue_objects:
          new_x = obj[1] + 2 * (offset - (obj[1] - min_x) / 2 )

          # If the mirrored position is within bounds, set the pixel to blue
          if 0 <= new_x < input_grid.shape[1]: # Check bounds
            output_grid[obj[0]][new_x] = 1


    return output_grid
```

