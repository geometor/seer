# cf98881b • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Target Columns:** Select columns from the input grid that contain *either* the digit '9' *or* the digit '4', *or* the digit '1'. Do *not* select all columns, only the select columns identified by the rule.

2.  **Extract Sub-grid:** From the selected columns, create a new grid, discarding all others.

3. **Reduce Further:** Consider only the first instance of a contiguous vertical sequence of a single color. Discard any subsequent, matching color that is contiguous vertically.

4. **Result:** the output grid contains only 4x4
"""

import numpy as np

def get_target_columns(input_grid):
    """
    Identifies columns containing 9, 4, or 1.
    """
    target_columns = []
    for j in range(input_grid.shape[1]):
        if 9 in input_grid[:, j] or 4 in input_grid[:, j] or 1 in input_grid[:,j]:
            target_columns.append(j)
    return target_columns

def extract_subgrid(input_grid, target_columns):
    """
    Extracts a subgrid based on the target columns.
    """
    subgrid = input_grid[:, target_columns]
    return subgrid

def reduce_vertically(input_grid):
    """
    Keeps only the first instance of a contiguous vertical sequence of a single color.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape
    
    for j in range(cols):
        first_instance_found = {} # dictionary to store is a color in a column had its "first instance"
        
        for i in range(rows):            
            current_color = input_grid[i,j]
            
            if current_color not in first_instance_found:
                output_grid[i, j] = current_color
                first_instance_found[current_color] = True
            else:
                output_grid[i, j] = 0 # set the other ones to white
        
    return output_grid

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)

    # get target columns
    target_cols = get_target_columns(input_grid)
    
    # extract the subgrid using only target columns
    subgrid = extract_subgrid(input_grid, target_cols)

    # perform vertical reduction to take first instances of each color contiguously
    reduced_grid = reduce_vertically(subgrid)

    # select only 4 columns at most
    output_grid = reduced_grid[:, :4]

    
    return output_grid.tolist()
```
