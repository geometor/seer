# 3-1e0a9b12 • 002 • example_1 - CODE

---
```python
"""
1. Collect all non-zero values from the input grid.
2. Sort the non-zero values in ascending order.
3. Place the sorted values in the bottom row of the output grid, starting from the leftmost column.
4. Maintain the original row order relationship of duplicate values in the input to the output. For instance, a value in a higher row in the input should be positioned above other instances of that same number in the output.
5. Fill the remaining cells of the output grid with zeros.
"""

import numpy as np

def get_nonzero_elements(grid):
    """Extracts non-zero elements and their original row indices."""
    elements = []
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value != 0:
                elements.append((value, row_idx, col_idx))
    return elements

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Initialize output grid with zeros
    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    # Get non-zero elements with their original row indices
    nonzero_elements = get_nonzero_elements(input_grid)

    # Sort elements primarily by value, secondarily by original row index
    sorted_elements = sorted(nonzero_elements, key=lambda x: (x[0], x[1]))

    # Place sorted elements in the last row
    col_idx = 0
    for value, original_row, original_col in sorted_elements:
        if len(set([x[0] for x in sorted_elements])) == len(sorted_elements):          
            output_grid[rows - 1, col_idx] = value
        else:
            # find row for the element
            output_row = rows -1
            for r in range(rows):
                if input_grid[r, original_col] == value:
                    output_row = r
                    if output_grid[r,col_idx] == 0 and output_grid[rows-1,col_idx] != value :
                        output_row = r
                        break;                    
                    elif (original_col == col_idx):
                        for rr in range(rows-1):
                            if (output_grid[rr,original_col] == 0):
                                output_row=rr
                                break
                        
            output_grid[output_row, col_idx] = value
                        
        col_idx += 1


    return output_grid
```
