# 3-1e0a9b12 • 006 • Response

---

*text:*

*text:*
```python
"""
The program finds all non-white and non-uniform colors and moves these values to the bottom row, preserving their original order.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid, then fill with white
    output_grid = np.full_like(input_grid, 0)

    # Find rows with all elements of the same color (excluding white)
    uniform_rows = []
    for row_index, row in enumerate(input_grid):
        unique_colors = np.unique(row)
        if len(unique_colors) == 1 and unique_colors[0] != 0:
            uniform_rows.append(row_index)
        elif len(unique_colors) == 2 and 0 in unique_colors:
            if len(np.where(row==unique_colors[1])[0])==1:
                uniform_rows.append(row_index)

    # Copy uniform rows to the output grid
    for row_index in uniform_rows:
        output_grid[row_index] = input_grid[row_index]

    # Find non-white pixels that are NOT in uniform rows
    non_white_pixels = []
    for row_index, row in enumerate(input_grid):
        if row_index not in uniform_rows:
            for col_index, pixel in enumerate(row):
                if pixel != 0:
                    non_white_pixels.append((pixel, col_index))

    # Sort the non-white pixels by their original column index
    non_white_pixels.sort(key=lambda x: x[1])

    # Place the non-white pixels in the last row of the output grid
    last_row_index = output_grid.shape[0] - 1
    
    for i, (pixel, _) in enumerate(non_white_pixels):
        output_grid[last_row_index][i] = pixel
        
    #fill the remaining non-white pixels in the appropriate row
    rows_non_white = []
    for r in range(len(input_grid)):
        colors = []
        for cor in range(len(input_grid)):
            colors.append(input_grid[r][cor])
        colors = np.unique(colors)
        if 0 in colors and len(colors)>2:
          for i in colors:
            if i != 0:
                rows_non_white.append(r)
                break

    for row_non_white in rows_non_white:
        col_index=0    
        for c in range(len(input_grid)):
          if input_grid[row_non_white][c] != 0:
            output_grid[row_non_white][col_index]=input_grid[row_non_white][c]
            col_index += 1
        
    return output_grid
```

