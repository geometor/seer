# a85d4709 • 011 • refine_coder

---
```python
"""
Iterate through each pixel of the input grid. If the input pixel is gray (5), 
the output color depends on the column: column 0 -> red (2), column 1 -> yellow (4), 
column 2 -> green (3).  If the input pixel is black (0), the output is a color 
determined by a gray (5) pixel. Return the output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as the input_grid
    output_grid = np.zeros_like(input_grid)
    
    # Get the column mapping color for any gray pixel.
    gray_column_colors = {}
    for col in range(input_grid.shape[1]):
        for row in range(input_grid.shape[0]):
          if input_grid[row, col] == 5:
              if col == 0:
                  gray_column_colors[col] = 2
              elif col == 1:
                  gray_column_colors[col] = 4
              elif col == 2:
                  gray_column_colors[col] = 3
    
    # Determine a default color for black pixels.
    default_color = list(gray_column_colors.values())[0] if gray_column_colors else 0  # Default to black if no gray pixels

    # Iterate through each pixel of the input grid
    for row in range(input_grid.shape[0]):
        for col in range(input_grid.shape[1]):
            # If the input pixel is gray (5)
            if input_grid[row, col] == 5:
                # Determine output color based on column
                if col == 0:
                    output_grid[row, col] = 2  # Red
                elif col == 1:
                    output_grid[row, col] = 4  # Yellow
                elif col == 2:
                    output_grid[row, col] = 3  # Green
            # Else (input pixel is black/0)
            else:
                output_grid[row,col] = default_color

    return output_grid
```
