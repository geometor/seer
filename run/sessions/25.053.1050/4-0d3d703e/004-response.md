# 4-0d3d703e • 004 • refine_coder

---
```python
"""
The program performs a direct substitution of each pixel's value based on a mapping specific to each example. The mapping isn't consistent across all examples; it must be determined separately for each input/output pair.

1.  **Determine the Example-Specific Mapping:** For each example, create a mapping by comparing corresponding pixel values in the input and output grids.
2.  **Apply the Mapping:** For every pixel in the input grid, find its corresponding replacement value in the example-specific mapping and replace it in the output grid.
3.  Output is the resulting grid.
"""

import numpy as np

def get_substitution_map(input_grid, output_grid):
    """Determines the example-specific substitution mapping."""
    substitution_map = {}
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            substitution_map[input_grid[i, j]] = output_grid[i, j]
    return substitution_map

def transform(input_grid, output_grid):  # Added output_grid as input
    # Initialize output_grid (in this case, it's provided, so we don't create a copy)

    # Determine the example-specific mapping.
    substitution_map = get_substitution_map(input_grid, output_grid)

    # Apply the Mapping
    transformed_grid = np.copy(input_grid) # make a copy of the input to modify
    for row_index, row in enumerate(input_grid):
        for col_index, value in enumerate(row):
            if value in substitution_map:
                transformed_grid[row_index, col_index] = substitution_map[value]

    return transformed_grid
```

