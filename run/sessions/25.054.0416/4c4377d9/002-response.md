# 4c4377d9 • 002 • example_1 • investigate_coder

---
```python
"""
The transformation rule is as follows:
1.  **Identify Repeating Pattern:** Observe the input grid and notice a repeating row pattern of "9 9 5 9", then "5 5 9 9", and then '9 5 9 9'.
2.  **Double all rows that do not start with gray:**. Duplicate these rows, taking the whole 3 x 4 grid, doubling all of the rows, to arrive at 6 x 4 grid.
3. **Rearrange rows**. Take the original 2nd row and move to the final row, so insert a copy of row 2 after row 6. Take the original 3rd row and insert a copy between rows 3 and 4.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = []

    # Duplicate each row and add to output_grid list
    for row in input_grid:
        output_grid.append(row)
        output_grid.append(row)

    output_grid = np.array(output_grid)

    #insert row 2 after original row
    row_2 = input_grid[1].copy()
    output_grid = np.insert(output_grid, 6, row_2, axis=0)
        
    #insert row 3 after original row
    row_3 = input_grid[2].copy()    
    output_grid = np.insert(output_grid, 3, row_3, axis=0)


    return output_grid.tolist()
```
