# 0a938d79 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Key Pixels:** Locate the 'red' (2) pixel in the top row and the 'azure' (8) pixel in the bottom row of the input grid.

2.  **Alternating Column:** from left, create columns in the output with the detected red value. Skip a column.

3. **Alternating Azure:** from left, create columns in the previously skipped column positions using the detected azure value.

4.  **Fill Output:** Repeat the alternating pattern of color columns filling the output grid, ensuring it has the same dimensions as the input grid.
"""

import numpy as np

def find_pixel(grid, color):
    # Find the first occurrence of a specified color in the grid.
    rows, cols = np.where(grid == color)
    if len(rows) > 0:
        return rows[0], cols[0]  # return first occurance
    return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    
    # Initialize output grid with the same dimensions and default white color.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # find red (2)
    red_pos = find_pixel(input_grid, 2)
    # find azure (8)
    azure_pos = find_pixel(input_grid, 8)

    if red_pos is None or azure_pos is None:
      return output_grid # default empty
    
    # create columns of red and azure
    for col in range(cols):
      if (col % 2) == 0:
        output_grid[:, col] = 2
      else:
        output_grid[:,col] = 8

    return output_grid
```
