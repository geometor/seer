# 0520fde7 • 012 • refine_coder

---
```python
"""
1.  **Initialization:** Create a 3x3 output grid filled with white (0).
2.  **Grey Pixel Counter:** Initialize a counter `grey_count` to 0.
3.  **Row Iteration:** Iterate through each row of the input grid.
4.  **Grey Detection:** Within each row, iterate through the pixels.
    a. If the current input pixel is grey (5):
        i. Increment `grey_count`.
        ii. If `grey_count` is less than or equal to 3: Determine the output row index (from 0 to 2, it is just the order of rows that contained grey). Place a red pixel (2) in the output grid at the position `[row_index][grey_count - 1]`.
5. Stop processing after three grey pixels have been found, either within the row or across multiple rows.
6.  **Output:** Return the 3x3 output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros((3, 3), dtype=int)
    grey_count = 0
    output_row_index = 0

    # Iterate through rows of the input grid
    for row_index in range(input_grid.shape[0]):
        row = input_grid[row_index, :]

        # Check if the row contains grey (5)
        if 5 in row:
           # Iterate through input row, find gray
           for col_index in range(input_grid.shape[1]):
              if row[col_index] == 5:
                grey_count += 1

                if grey_count <= 3:
                  output_grid[output_row_index, grey_count-1] = 2

           output_row_index +=1 # update output_row for next row with gray
           if output_row_index >= 3:
              break

    return output_grid
```
