# 1b2d62fb • 024 • refine_coder

---
```python
"""
1.  **Find Central Azure Column:** Scan the input grid to locate a column where *all* pixels are azure (8). This is the "central column."
2.  **Create Output Grid:** Create a new output grid with the same number of rows as the input, and exactly 3 columns. Initialize all cells in the output grid to white (0).
3.  **Conditional Copying:** For each row:
    *   If the central azure column exists, and in this row, there is *not* an azure pixel immediately to the *left* of the central column in the *input grid*, copy the azure (8) from the central column of the input to the second column of the output for this row.
    *   If the central azure column exists *and* in this row, *and* if there isn't an azure immediately to the *right* of the central column, copy that azure (8) to the *third* column of the output for that row.
    *    If the central azure column exists *and* there is no azure pixel immediately to the left of the central column, *and* if it is not at the extreme left (index > 0), copy the value from the input pixel immediately to the left, to column 1 of the output row.
    *    If there is *not* a vertical azure line found, return a grid of zeros with the same dimensions as the *input* grid.
"""

import numpy as np

def find_central_azure_column(grid):
    # Find the column index of the vertical line of azure (8) pixels.
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == 8 for i in range(rows)):
            return j
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the central azure column.
    center_col = find_central_azure_column(input_grid)

    # Initialize the output grid as all zeros (white).
    output_grid = np.zeros((rows, 3), dtype=int)

    if center_col != -1:
        # Iterate through each row and apply conditional copying rules.
        for i in range(rows):
            # Copy to center column if no azure to the left
            if center_col > 0 and input_grid[i,center_col-1] != 8:
                output_grid[i,1] = input_grid[i,center_col]
            elif center_col == 0:
                output_grid[i,1] = input_grid[i,center_col]


            # copy to right column if no azure to the right
            if center_col < cols -1 and input_grid[i, center_col + 1] != 8:
                output_grid[i,2] = input_grid[i, center_col]

            #Copy to left if no azure to left and left exists
            if center_col > 0 and input_grid[i, center_col-1] != 8:
                output_grid[i,0] = input_grid[i, center_col-1]

    else:
        # If no central azure column, return all-white grid of input size.
        return np.zeros((rows, cols), dtype=int).tolist()

    return output_grid.tolist()
```
