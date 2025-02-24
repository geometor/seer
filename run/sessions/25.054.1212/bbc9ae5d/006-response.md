# bbc9ae5d • 006 • refine_coder

---
```python
"""
1.  Identify Expanding Color: Find the single color in the input grid that is *not* white (0). This is the "expanding color".
2.  Count Expanding Pixels: Count the number of pixels of the expanding color in the input grid.
3.  Determine Output Dimensions:
    *   The output grid has the *same number of columns* as the input grid.
    *   The output grid has a number of rows equal to the *number of rows in the input grid (which is always 1) plus the count of expanding color pixels*.
4.  Create Expanding Shape:
    *   Starting from the top-left corner of the output grid (0,0), fill cells with the expanding color.
    *   The expanding color fills a triangular area.
    *   Row 1 of output = row 1 of input
    *   Each subsequent row duplicates the previous row, and adds a single pixel of the expanding color to the end.
5.  Fill Background: Fill all remaining cells in the output grid with white (0).
"""

import numpy as np

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the expanding color (non-zero color)
    expanding_color = None
    for color in np.unique(input_grid):
        if color != 0:
            expanding_color = color
            break

    # Count the number of pixels of the expanding color
    expanding_color_count = np.count_nonzero(input_grid == expanding_color)

    # Determine output dimensions
    output_rows = rows + expanding_color_count
    output_cols = cols
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # Copy the first row from input to output
    output_grid[0, :] = input_grid[0, :]

    # Create the expanding shape
    for i in range(1, output_rows):
        # Copy the previous row
        output_grid[i, :] = output_grid[i-1, :]
        # Find the last non-zero index in the previous row
        last_non_zero = -1
        for j in range(output_cols):
            if output_grid[i-1, j] != 0:
                last_non_zero = j
        
        #add expanding color to the end
        if last_non_zero + 1 < output_cols:
             output_grid[i, last_non_zero+1] = expanding_color

    return output_grid.tolist()
```
