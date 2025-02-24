# 662c240a • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify the bottom-most section of the input grid.** This section is defined as contiguous rows, up to the point where the next upper row contains different colors.
2.  **Output this section.** The output grid has the same dimensions as the bottom area.

In simpler terms, extract the last "unique colored block" of rows from the bottom.
"""

import numpy as np

def get_bottom_unique_block(grid):
    """
    Identifies the bottom-most section of the grid consisting of
    contiguous rows with the same color composition, up to the point
    where the next upper row contains different colors.
    """
    rows, cols = grid.shape
    bottom_block_start = rows - 1

    # Start from the bottom and move up
    while bottom_block_start > 0:
        current_row_colors = set(grid[bottom_block_start])
        prev_row_colors = set(grid[bottom_block_start - 1])

        if current_row_colors != prev_row_colors:
            #check to make sure that they are not completely different colors
            if len(current_row_colors.intersection(prev_row_colors)) == 0:
                break  # Found a row with diff colors
            else:
                bottom_block_start -=1 #the rows contain some of the same colors
        else:
            bottom_block_start -= 1


    return grid[bottom_block_start:]

def transform(input_grid):
    """
    Transforms the input grid by extracting the bottom-most uniquely colored block.
    """
    # Convert input grid to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # Get the bottom unique block
    output_grid = get_bottom_unique_block(input_grid)

    return output_grid.tolist()
```
