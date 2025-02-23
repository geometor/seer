# 9af7a82c • 006 • refine_coder

---
```python
"""
1.  **Count Non-Zero Elements:** Count the total number of non-zero elements across all columns of the input grid. This count determines the height of the output grid. The output width is the same as the input width.

2.  **Column-wise Transformation:** For each column in the input grid:
    a.  **Extract:** Extract all values from the current input column.
    b.  **Filter:** Separate the non-zero values from the zero values.
    c.  **Sort:** Sort the non-zero values in *descending* order.
    d. **Assemble Column:** Create output column. Place the sorted non-zero values at the *top* of the output column.
    e.  **Pad:** Fill the remaining cells of the output column (if any) with zeros (representing the color white).

3.  **Assemble Output Grid:** Combine the transformed columns to form the final output grid.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    
    # Count non-zero elements to determine output height.
    non_zero_count = np.count_nonzero(input_grid)
    output_height = non_zero_count
    output_width = input_grid.shape[1]
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # change output pixels 
    output_row_index = 0
    for j in range(input_grid.shape[1]):
        # Get the values from the input column
        input_column_values = input_grid[:, j]

        # Get non-zero values.
        non_zero_values = input_column_values[input_column_values != 0]
        
        #sort in descending order
        sorted_non_zero = np.sort(non_zero_values)[::-1]

        # how many non-zeros in this col
        num_non_zero_this_col = len(sorted_non_zero)
        
        # write to output
        output_grid[output_row_index:output_row_index + num_non_zero_this_col, j] = sorted_non_zero
        
        # update the output_row_index so next col writes to next available row
        output_row_index += num_non_zero_this_col

    return output_grid.tolist()
```

