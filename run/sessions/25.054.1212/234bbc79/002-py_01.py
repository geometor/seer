"""
1. **Column Reduction:** The output grid has 7 columns while the input has 9. Columns 3 and 6 (counting from 0) of the input are removed.

2. **Color Replacement (5s):** All pixels with a value of '5' (gray) in the input grid are changed.

3. **Replacement Logic:**
   - Input '5' pixels directly above or below a '1' (blue) become '1' (blue).
   - Input '5' pixels adjacent to a '2' (red) become '2'(red) if the '5' is at the edge and a '2' exist.

4. **Other Pixels:** Pixels that are not '5' in the input grid retain their original values in the output grid, maintaining relative position after column removal.
"""

import numpy as np

def get_neighbors(grid, row, col):
    neighbors = []
    rows, cols = grid.shape
    if row > 0:
        neighbors.append(grid[row-1, col])  # Up
    if row < rows - 1:
        neighbors.append(grid[row+1, col])  # Down
    if col > 0:
        neighbors.append(grid[row, col-1])  # Left
    if col < cols - 1:
        neighbors.append(grid[row, col+1])  # Right
    return neighbors

def transform(input_grid):
    # Initialize output_grid by removing columns 3 and 6
    output_grid = np.delete(input_grid, [3, 6], axis=1)

    rows, cols = output_grid.shape

    # Iterate through the output_grid and apply transformation rules
    for row in range(rows):
        for col in range(cols):
            # Map the output grid indices back to the input grid
            input_col = col
            if col >= 3:
                input_col += 1
            if col >= 5:
                input_col += 1

            # Color Replacement Logic
            if input_grid[row, input_col] == 5:
                neighbors = get_neighbors(input_grid, row, input_col)
                if 1 in neighbors:
                    output_grid[row, col] = 1
                #check if at first or last colum
                elif (input_col == 0 or input_col == 8) and 2 in neighbors:
                  output_grid[row,col] = 2
                else: #added condition
                  output_grid[row,col] = 0

    return output_grid