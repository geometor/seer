# 2dee498d • 017 • refine_coder

---
```python
"""
The input grid consists of a smaller rectangular pattern that repeats horizontally. The width of the repeating pattern is a divisor of the input grid's width. Extract one instance of this repeating pattern from the beginning of the input grid. The output is this extracted repeating pattern.
"""

import numpy as np

def find_repeating_pattern(grid):
    rows, cols = grid.shape
    for c in range(1, cols + 1):
        # Check if c is a divisor of cols
        if cols % c == 0:
            pattern = grid[:, 0:c]
            # Check if the pattern repeats throughout the entire grid
            repeats = True
            for i in range(c, cols, c):
                if not np.array_equal(pattern, grid[:, i:i + c]):
                    repeats = False
                    break
            if repeats:
                return pattern

    return None


def transform(input_grid):
    """
    Transforms the input grid by identifying and extracting a repeating subgrid.
    The width of the repeating subgrid is a divisor of the original grid width
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the repeating sub-grid.
    pattern = find_repeating_pattern(input_grid)
    if pattern is not None:
        output_grid = pattern
    else:
        output_grid = input_grid

    return output_grid.tolist()
```
