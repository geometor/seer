# 2dee498d • 014 • example_3 • investigate_coder

---
```python
"""
Extracts the smallest repeating horizontal sequence from the input grid to form the output grid.
"""

import numpy as np

def find_repeating_unit(grid):
    """Finds the smallest repeating unit in a grid along the horizontal axis."""
    height, width = grid.shape
    for unit_width in range(1, width + 1):
        if width % unit_width == 0:
            unit = grid[:, :unit_width]
            repeats = width // unit_width
            valid_unit = True
            for i in range(1, repeats):
                if not np.array_equal(unit, grid[:, i*unit_width:(i+1)*unit_width]):
                    valid_unit = False
                    break
            if valid_unit:
                return unit
    return grid  # If no repeating unit is found, return the original grid

def transform(input_grid):
    """
    Extracts the fundamental repeating unit from the input grid.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The output grid, which is the repeating unit.
    """
    # Find the repeating unit
    repeating_unit = find_repeating_unit(np.array(input_grid))

    # The repeating unit is the output grid
    output_grid = repeating_unit

    return output_grid.tolist()
```
