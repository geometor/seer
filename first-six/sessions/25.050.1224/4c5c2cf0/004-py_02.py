"""
The transformation involves taking the azure structure, creating a vertically mirrored copy of it, and adding this copy to the output grid, positioning it according to the horizontal center of the green shape. The green objects remain invariant.
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

    # Get the positions of azure and green objects
    azure_objects = get_objects_by_color(input_grid, 8)
    green_objects = get_objects_by_color(input_grid, 3)

    # Green objects remain the same, so no action needed

    # Mirror the azure objects vertically and add to output grid
    if (len(azure_objects) > 0 and len(green_objects) > 0):

      # Calculate approximate center row of green shape
      green_center_row = int(np.mean([obj[0] for obj in green_objects]))

      # Find max and min row of azure shape
      max_y = max(obj[0] for obj in azure_objects)
      min_y = min(obj[0] for obj in azure_objects)

      # Calculate the height and middle of the original azure shape
      azure_height = max_y - min_y + 1
      azure_middle_row = (min_y + max_y) // 2
        
      # Calculate offset below the center of the green cells
      offset = (green_center_row - azure_middle_row) + azure_height

      for obj in azure_objects:
          new_y = obj[0] + 2*(offset -  obj[0] )
          if 0 <= new_y < input_grid.shape[0]: # Check bounds
            output_grid[new_y, obj[1]] = 8

      # Calculate the offset above the center of the green cells
      offset = (green_center_row - azure_middle_row) - azure_height

      for obj in azure_objects:
          new_y = obj[0] + 2*(offset - obj[0]) #obj[0] is row and obj[1] is column
          if 0 <= new_y < input_grid.shape[0]: # Check bounds
            output_grid[new_y, obj[1]] = 8


    return output_grid