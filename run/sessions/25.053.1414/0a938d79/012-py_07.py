"""
Transforms an input grid by first identifying rows that start with non-zero values and propagating those values across the row.
Then, it takes those changed rows, and duplicates them, effectively repeating the modified pattern to create an output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    copied_grid = np.copy(input_grid)
    rows, cols = copied_grid.shape

    # Row Propagation: Iterate through rows of the copied grid.
    changed_rows = []
    for r in range(rows):
        # Leading Non-Zero: If a row starts with a non-zero, replace all elements.
        if copied_grid[r, 0] != 0:
            copied_grid[r, :] = copied_grid[r, 0]
            changed_rows.append(copied_grid[r,:].tolist())


    output_grid = np.copy(input_grid)
    # add the changed rows
    for r in range(rows):
        # Leading Non-Zero: If a row starts with a non-zero, replace all elements.
        if output_grid[r, 0] != 0:
            output_grid[r, :] = output_grid[r, 0]
    
    # append changed rows
    for row in changed_rows:
        output_grid = np.append(output_grid, [row], axis=0)
    
    return output_grid