# 0a938d79 • 002 • example_1 - CODE

---
```python
"""
The transformation rule involves replicating the initial objects (single cells of color 2 and 8) across the grid in a specific pattern.

1.  **Identify Initial Objects**: Two single-cell objects are present in the input grid: one of color 2 and one of color 8.

2.  **Determine Replication Pattern**:
    *   The object with color 2, initially at position (0, 5), is replicated vertically down the entire column and then repeated every 5 columns to the right.
    *   The object with color 8, initially at position (9, 7), is replicated vertically down the entire column and then repeated every 5 columns to the right.
   
3. **Vertical Replication and Columns creation:** Each cell is the source of a new object, and each object replicates vertically down.

4. **Horizontal Replication and Columns creation:** Both initial single cells objects creates are replicated horizontally in a repeating pattern.

In summary, it is like stamping the single instances of the color vertically down, and repeat the result horizontally.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid, then modify it
    output_grid = np.zeros_like(input_grid)
    
    rows, cols = input_grid.shape

    # Find the positions and colors of the non-zero cells in the input grid.
    initial_objects = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                initial_objects.append(((r, c), input_grid[r, c]))

    # Replicate and place objects in output grid
    for obj in initial_objects:
        pos, color = obj
        _, initial_col = pos  # Corrected unpacking

        # Determine column start based on the initial color's column
        for j in range(5):  # There are 5 repetitions
          
          new_col = initial_col + (j*5)
          if new_col < cols:
            for i in range(rows):
               output_grid[i,new_col] = color
    
    return output_grid
```
