# c8f0f002 • 002 • example_1 • investigate_coder

---
```python
"""
Replace all orange (7) pixels with gray (5) pixels, preserving the grid structure and all other colors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replacing all instances of orange (7) with gray (5).

    Args:
        input_grid (list of lists): A 2D array representing the input grid.

    Returns:
        list of lists: A 2D array representing the transformed grid.
    """
    # Initialize the output grid as a copy of the input grid.  This ensures
    # that the dimensions and any unchanged values are preserved.
    output_grid = [row[:] for row in input_grid]  # faster than deepcopy

    # Iterate through each cell of the grid using nested loops.
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            # Check if the current cell's value is 7 (orange).
            if output_grid[i][j] == 7:
                # Replace the orange pixel with gray (5).
                output_grid[i][j] = 5

    # Return the modified grid.
    return output_grid
```
