# 2dee498d • 018 • refine_coder

---
```python
"""
The input grid is compressed by identifying the smallest repeating vertical sub-grid pattern.
The output grid represents this smallest repeating pattern.
"""

import numpy as np

def find_smallest_repeating_pattern(grid):
    """
    Finds the smallest repeating vertical sub-grid pattern in a grid.
    """
    rows, cols = grid.shape
    for width in range(1, cols + 1):
        if cols % width == 0:  # Check if width is a divisor of total columns
            pattern = grid[:, :width]
            repeats = True
            for i in range(width, cols, width):
                if not np.array_equal(pattern, grid[:, i:i + width]):
                    repeats = False
                    break
            if repeats:
                return pattern
        else: #handle cases where the width is not a divisor
            pattern = grid[:,:width]
            repeats = True
            for i in range(width, cols - width + 1, width):
                if not np.array_equal(pattern, grid[:, i:i+width]):
                    repeats = False
                    break
            if repeats:
                return pattern

    return None

def transform(input_grid):
    """
    Transforms the input grid by identifying and extracting the smallest repeating vertical subgrid.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the smallest repeating sub-grid.
    pattern = find_smallest_repeating_pattern(input_grid)

    # If a repeating pattern is found, return it as the output.
    if pattern is not None:
        output_grid = pattern
    else:
        output_grid = input_grid  # Default to input if no pattern is found.

    return output_grid.tolist()
```
