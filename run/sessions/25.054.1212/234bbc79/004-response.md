# 234bbc79 • 004 • refine_coder

---
```python
"""
1.  **Column Removal:** Remove columns 3 and 6 (counting from 0) of the input grid to create a reduced grid.

2.  **Color Replacement for '5' (Gray) Pixels:**
    *   If a '5' pixel in the *input* grid is directly above or below a '1' (blue) pixel, change it to '1' (blue) in the corresponding position in the *output* grid.
    *   If a '5' pixel in the *input* grid is horizontally or vertically adjacent to a '2' (red) pixel, change to '2'(red)
    *   If a '5' pixel in the *input* grid is horizontally or vertically adjacent to a '8' (azure) pixel, change to '8'(azure)

3.  **Preservation of Other Colors:** All other pixels (not '5') retain their original color from the input grid to the output grid, maintaining their relative positions after the column removal.
4. All gray(5) will be replaced with a neighbor color if applicable. If multiple neighbors are candidates, preference should follow blue > red > azure
"""

import numpy as np

def get_neighbors(grid, row, col):
    neighbors = []
    rows, cols = grid.shape
    if row > 0:
        neighbors.append((grid[row-1, col], row-1, col))  # Up
    if row < rows - 1:
        neighbors.append((grid[row+1, col], row+1, col))  # Down
    if col > 0:
        neighbors.append((grid[row, col-1], row, col-1))  # Left
    if col < cols - 1:
        neighbors.append((grid[row, col+1], row, col+1))  # Right
    return neighbors

def transform(input_grid):
    # Initialize output_grid by removing columns 3 and 6
    output_grid = np.delete(input_grid, [3, 6], axis=1)

    rows, cols = output_grid.shape
    temp_output_grid = output_grid.copy()

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
                #prioritize the color
                neighbor_colors = [color for color, _,_ in neighbors]
                replace_color = 0 #default
                if 1 in neighbor_colors:
                    replace_color = 1
                elif 2 in neighbor_colors:
                    replace_color = 2
                elif 8 in neighbor_colors:
                    replace_color = 8

                temp_output_grid[row,col] = replace_color
    output_grid = temp_output_grid

    return output_grid
```
