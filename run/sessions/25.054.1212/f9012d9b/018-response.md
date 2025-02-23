# f9012d9b • 018 • refine_coder

---
```python
"""
1. Find Valid Subgrid Size: Examine the input grid starting from the top-left corner. Determine the largest possible square subgrid (1x1, 2x2, 3x3, etc.) that meets either of the following criteria:
    *   It contains only one color (any color).
    *   It contains only gray (5) and one other color.

2. Copy Subgrid: Once the largest valid subgrid size is found, copy that subgrid from the input to the output.

3. Return Result
"""

import numpy as np

def get_largest_valid_subgrid_size(grid):
    """
    Finds the size of the largest square subgrid at the top-left corner
    of the input grid that contains only one color or gray (5) and one other color.
    """
    height, width = grid.shape
    max_size = min(height, width)

    for size in range(max_size, 0, -1):
        subgrid = grid[0:size, 0:size]
        unique_colors = np.unique(subgrid)

        if len(unique_colors) == 1:
            return size  # Single color case
        elif len(unique_colors) == 2 and 5 in unique_colors:
            return size  # Gray and one other color case
        elif len(unique_colors) == 2:
            continue # two colors, but not gray
        elif len(unique_colors) > 2:
            continue # skip and check the smaller sub-grid

    return 0  # Should not happen in well-formed ARC tasks

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""

    # Determine output size.
    output_size = get_largest_valid_subgrid_size(input_grid)

    # Initialize the output grid.
    output_grid = np.zeros((output_size, output_size), dtype=int)

    if output_size > 0:
        # Copy the subgrid.
        output_grid[:] = input_grid[0:output_size, 0:output_size]

    return output_grid
```
