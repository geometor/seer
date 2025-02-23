# f9012d9b • 016 • refine_coder

---
```python
"""
1. Determine Output Size: Identify the size of the largest square subgrid, at the top left corner of the input grid, that is made up of all the same color/number, excluding 5 (gray). This defines the dimension of the output grid.
2. Copy the Subgrid: Copy this subgrid to the output.
"""

import numpy as np

def get_largest_uniform_top_left_subgrid_size(grid):
    """
    Finds the size of the largest square subgrid at the top-left corner
    of the input grid that contains only one color (excluding gray, 5).
    """
    height, width = grid.shape
    max_size = min(height, width)

    for size in range(max_size, 0, -1):
        subgrid = grid[0:size, 0:size]
        unique_colors = np.unique(subgrid)
        if len(unique_colors) == 1 and unique_colors[0] != 5:
            return size
        elif len(unique_colors) == 2 and 5 in unique_colors:
            if unique_colors[0] == 5:
               if unique_colors[1] != 5:
                   return size
            elif unique_colors[1] == 5:
               if unique_colors[0] != 5:
                   return size

    return 0  # Should not happen in well-formed ARC tasks, but included for safety

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    # Determine output size.
    output_size = get_largest_uniform_top_left_subgrid_size(input_grid)

    # Initialize the output grid.
    output_grid = np.zeros((output_size, output_size), dtype=int)
    
    if output_size > 0:
        # Copy the subgrid.
        output_grid[:] = input_grid[0:output_size, 0:output_size]


    return output_grid
```
