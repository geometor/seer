# 3-1e0a9b12 • 006 • example_3 - CODE

---
```python
"""
The non-zero pixels represent objects. Each object, identified by its color (value), shifts down by a specific number of rows.
Objects with value 3 and 2 shift down by two rows. Objects with values 6 and 1 shift down by one row.
Objects of value 1 also shift one column to the right.
Object of value 2 also shifts one column to the right.
The white pixels (value 0) remain unchanged.
"""

import numpy as np

def get_objects(grid):
    # Find positions of non-zero pixels
    objects = []
    for value in np.unique(grid):
        if value != 0:
            positions = np.argwhere(grid == value)
            objects.append((value, positions))
    return objects

def shift_object(grid_shape, object_positions, row_shift, col_shift):
    # Apply shifts to object positions, ensuring they stay within grid bounds
    shifted_positions = []
    for pos in object_positions:
        new_row = min(pos[0] + row_shift, grid_shape[0] - 1)
        new_col = min(pos[1] + col_shift, grid_shape[1] - 1)
        new_col = max(0,new_col) # additional fix to prevent going to -1
        shifted_positions.append((new_row, new_col))
    return shifted_positions

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.zeros_like(input_grid)
    
    # Get objects and their positions
    objects = get_objects(input_grid)
    
    # Apply shifts based on object value
    for value, positions in objects:
        if value == 3:
            shifted_positions = shift_object(input_grid.shape, positions, 2, 0)
        elif value == 6:
            shifted_positions = shift_object(input_grid.shape, positions, 1, 0)
        elif value == 1:
            shifted_positions = shift_object(input_grid.shape, positions, 1, 1)
        elif value == 2:
            shifted_positions = shift_object(input_grid.shape, positions, 2, 1)
        else:
            shifted_positions = positions # should not happen, since we only operate on non-zero objects.

        # Place shifted objects in the output grid
        for pos in shifted_positions:
            output_grid[pos] = value

    return output_grid
```
