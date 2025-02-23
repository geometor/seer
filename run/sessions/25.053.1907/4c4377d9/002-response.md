# 4c4377d9 • 002 • example_1 - CODE

---
```python
"""
The input grid is duplicated and stacked vertically with a one-column rightward shift in the position of the colored pixels in the even rows.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with double the height of the input grid and the same width.
    output_grid = np.zeros((input_grid.shape[0] * 2, input_grid.shape[1]), dtype=int)

    # Iterate through the rows of the input grid.
    for i in range(input_grid.shape[0]):
        # Copy each row from the input grid to the output grid, to rows 2i and 2i+1.
        output_grid[i*2] = input_grid[i]
        output_grid[(i*2)+1] = input_grid[i]

        #shift values
        row = output_grid[(i*2)+1]
        shifted_row = np.array(row)  # Create a copy to modify

        # Find indices of values that are not 9 and 5 in the original row
        val_indices = np.where((row != 9) & (row !=5))[0]

        # set values to shift
        for val_index in val_indices:
            shifted_row[val_index] = row[val_index]


        # Find indices of 9s and 5s
        indices_9 = np.where(row == 9)[0]
        indices_5 = np.where(row == 5)[0]

        # Shift indices to right
        shifted_indices_9 = (indices_9 + 1) % row.shape[0]
        shifted_indices_5 = (indices_5 + 1) % row.shape[0]

        #reset original positions
        shifted_row[indices_9] = 0
        shifted_row[indices_5] = 0


        # Apply the shift by assigning values to the new positions
        shifted_row[shifted_indices_9] = 9
        shifted_row[shifted_indices_5] = 5


        output_grid[(i*2)+1] = shifted_row
        

    return output_grid
```
