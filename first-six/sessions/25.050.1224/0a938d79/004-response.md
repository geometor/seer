# 0a938d79 • 004 • example_2 - CODE

---
```python
"""
The transformation rule involves replicating the initial objects (single cells of color 1 and 3) across the grid in a specific pattern.

1.  **Identify Initial Objects**: There are two single-cell objects in the input grid, one with color 1 and another with color 3.

2.  **Determine Replication Pattern**:
    *   The object with color 1 (initially at position (0, 5)) is replicated vertically down and then repeated every 5 columns.
    *   The object with color 3 (initially at position (6, 8)) is replicated vertically down and then repeated every 5 columns.

3. **Vertical Replication and Columns creation:** Each cell is the source of a new object, and each object replicates vertically down.

4. **Horizontal Replication and Columns creation:** Both initial single cells objects creates are replicated horizontally in a repeating pattern.

In summary, the same "stamping" rule is applied: single instances of colors are stamped vertically, and the results are repeated horizontally every 5 columns.
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
        for j in range((cols // 5) + 1):  # Iterate enough times to cover the whole grid
          
          new_col = initial_col + (j*5)
          if new_col < cols:
            for i in range(rows):
               output_grid[i,new_col] = color
    
    return output_grid
```

