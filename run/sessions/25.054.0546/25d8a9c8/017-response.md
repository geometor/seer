# 25d8a9c8 • 017 • refine_coder

---
```python
"""
1.  **Identify Unique Colors in the Top Row:** Examine the first row of the input grid and determine the unique colors present.
2.  **Map to Output Colors:** Observe that in all examples there are two distinct colors in each grid. There are also two distinct colors in the top row of each grid. The transformation changes all pixels of color A in the input to color B, where A and B are a unique combination per row.
3. **Apply color changes:** Using the color change mapping from the first row, apply these transformations to the entire grid.
"""

import numpy as np

def get_color_map_for_row(input_row, output_row):
    """
    Creates a color mapping dictionary for a single row.

    Args:
      input_row: list
      output_row: list

    Returns:
      A dictionary for converting colors
    """
    color_map = {}
    for i in range(len(input_row)):
        color_map[input_row[i]] = output_row[i]
    return color_map

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows = input_grid.shape[0]
    
    # Iterate through each row to generate color maps.
    for row in range(rows):
      input_row = input_grid[row,:]
      if row == 0:
        #find output row and set colors
        unique_input_colors = sorted(list(set(input_row)))
        if len(unique_input_colors) == 1:
          output_row = [5 if unique_input_colors[0] != 5 else 0] * len(input_row)
        else:
          output_row = [0] * len(input_row)
      else:
        # find output row by checking the color changes in input
        unique_input_colors = sorted(list(set(input_grid.flatten())))
        if len(unique_input_colors) <= 2:
          output_color = [c for c in [0,5] if c not in output_grid[0,:]]
          if len(output_color)>0:
            output_row = [output_color[0]] * len(input_row)
          else:
            output_row = output_grid[0,:]
        
        else:
          output_row = output_grid[0,:]

      color_map = get_color_map_for_row(input_row, output_row)
          
      # Apply the color mapping to the entire row in output
      for col in range(output_grid.shape[1]):
          output_grid[row, col] = color_map[input_grid[row, col]]

    return output_grid
```
