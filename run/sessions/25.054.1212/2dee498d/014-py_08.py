"""
The input grid is compressed by identifying a repeating 2x1 sub-grid pattern and extracting the first occurance.
The output grid represents this pattern.
"""

import numpy as np

def find_repeating_pattern(grid):
    rows, cols = grid.shape
    for c in range(1, cols + 1):
        pattern = grid[:, 0:c]
        # Check if the pattern repeats throughout the entire grid
        repeats = True
        for i in range(c, cols, c):
            if i + c > cols:
                if not np.array_equal(pattern[:, :cols-i], grid[:, i:cols]):
                   repeats = False
                   break

            elif not np.array_equal(pattern, grid[:, i:i + c]):
                repeats = False
                break
        if repeats:
            return pattern

    return None


def transform(input_grid):
    """
    Transforms the input grid by identifying and extracting a repeating 2x1 subgrid.
    """
    # Convert to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Find the smallest repeating sub-grid.
    pattern = find_repeating_pattern(input_grid)
    if pattern is not None:
        output_grid = pattern
    else:
        output_grid = input_grid

    return output_grid.tolist()