# 1-3aa6fb7a • 010 • refine_code - CODE

---
```python
"""
1.  **Identify 2x1 Azure Rectangles:** Find all 2x1 vertical rectangles where both cells are azure (8).

2.  **Conditional Blue Placement - Right:**
    a. Check the right side of each azure rectangle.
    b. If the cell to the immediate right of the top cell of the 2x1 azure rectangle *and* the cell to the immediate right of the bottom cell of the 2x1 azure rectangle contains an azure cell (8), then place a blue cell(1) to the immediate left of the top cell of the 2x1 azure rectangle.

3. **Conditional Blue Placement - Left:**
    a. Check the left side of each azure rectangle.
    b. If the cell to the immediate left of the bottom cell of the 2x1 azure rectangle contains an azure cell (8), then place a blue cell(1) to the immediate right of the bottom cell of the 2x1 azure rectangle.
"""

import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    for top_coord, bottom_coord in azure_rectangles:
        #Conditional Blue Placement - Right
        r_top, c_top = top_coord
        r_bot, c_bot = bottom_coord
        if (c_top + 1 < output_grid.shape[1] and
            c_bot + 1 < output_grid.shape[1] and
            output_grid[r_top, c_top + 1] == 8 and
            output_grid[r_bot, c_bot + 1] == 8):
                if c_top -1 >= 0:
                    output_grid[r_top,c_top-1] = 1

        #Conditional Blue Placement - Left
        if (c_bot - 1 >= 0 and
            output_grid[r_bot,c_bot-1] == 8):
             if c_bot + 1 < output_grid.shape[1]:
                output_grid[r_bot,c_bot+1] = 1
    return output_grid
```

