# 1e0a9b12 • 006 • refine_coder

---
```python
"""
1.  **Identify Non-zero Pixels:** Find all pixels in the input grid that are not zero. Note their color, original row, and original column.
2.  **Process Input Rows Sequentially:** Iterate through each row of the *input* grid, starting from the top row (row 0) and going down.
3.  **Preserve Intra-Row Order:** For each input row, process the non-zero pixels found in that row from left to right (original column order).
4.  **Place at lowest available position:** For each non-zero pixel:
    -   start at the *bottom* row of the output grid in the pixel's original column.
    -   If the cell at that location in the output grid is empty (value 0), place the pixel there.
    -   If the cell is occupied, move up one row at a time in the *same column* until you find an empty cell.  Place the pixel in that empty cell.
5.  **Implicit Zero Filling:** The output grid is implicitly filled with zeros as any remaining empty spaces will naturally contain zeros.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero pixels to the bottom,
    preserving their original row-wise order.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through input rows (top to bottom)
    for r in range(rows):
        # Process non-zero pixels in the current row (left to right)
        for c in range(cols):
            pixel_value = input_grid[r, c]
            if pixel_value != 0:
                # Find the lowest available position in the output grid
                output_row = rows - 1
                while output_row >= 0 and output_grid[output_row, c] != 0:
                    output_row -= 1

                # Place the pixel in the found position
                if output_row >= 0:
                    output_grid[output_row, c] = pixel_value

    return output_grid
```

