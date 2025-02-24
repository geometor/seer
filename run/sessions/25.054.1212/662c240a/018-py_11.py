"""
1.  **Iterate downwards:** Start examining rows from the bottom of the input grid, moving upwards.
2. **Identify Blocks**: Consider a block to be the contiguous groups of rows *above* the current row being evaluated.
3.  **Check for complete row differences**: For each row being examined (starting from the second-to-last row and going up), compare it to the row *immediately below it*. A "complete row difference" means that *all* corresponding pixel colors in the two rows are different.
4.  **Extract Block:** If a complete row difference is found, select all rows *above* and including the current row for the output grid.
5.  **Output**: Return the selected block as output. If no complete difference is found after examining all rows, the output is an empty grid, or alternatively, the original grid. (This edge case needs clarification with more examples; for now, we assume if no differences exist, no transformation happens). The current examples show that the entire grid should be returned, although this could change with more complex cases.
"""

import numpy as np

def _rows_all_different(row1, row2):
    """Helper function to check if all elements in two rows are different."""
    return not np.any(row1 == row2)

def transform(input_grid):
    """
    Transforms the input grid based on the natural language program description.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape

    if rows <= 1:  # Handle edge case with a single-row input, or empty grid
        return grid.tolist()

    for i in range(rows - 1, 0, -1):
        # Compare the current row with the row immediately below it.
        if _rows_all_different(grid[i], grid[i-1]):
            # If all colors are different, extract the block *above* and including the current row.
            output_grid = grid[:i+1]
            return output_grid.tolist()

    # If no complete row difference is found, return the entire original grid.
    return grid.tolist()