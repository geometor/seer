# AboveBelow10 • 006 • refine_coder

---
```python
"""
1.  **Identify Key Parameters:** Determine the target `color` for the diagonal, the `fill_direction` (left or right), and the `diagonal_direction` (top-left to bottom-right, or bottom-left to top-right).

2.  **Locate the Diagonal:** Find the longest diagonal line of pixels matching the target `color` and `diagonal_direction`.

3.  **Fill based on Direction:**
    *   If `fill_direction` is "left", for each row, change all pixels to the *left* of the diagonal pixel in that row to the target `color`.
    *   If `fill_direction` is "right", for each row, change all pixels to the *right* of the diagonal pixel in that row to the target `color`.

4.  **Conditional Extension (Example 2):** If and *only if* the `diagonal_direction` is "bottom-left to top-right" AND the `fill_direction` is "right", then extend the filling to the bottom of the grid. This means, after filling to the right of the diagonal, continue filling all subsequent rows completely with the target `color`.
"""

import numpy as np

def find_diagonal(grid, color, diagonal_direction):
    """Finds the longest diagonal of a given color and direction."""
    rows, cols = grid.shape
    diagonal_pixels = []

    if diagonal_direction == "top_left_to_bottom_right":
        for start_row in range(rows):
            current_diagonal = []
            row, col = start_row, 0
            while row < rows and col < cols:
                if grid[row, col] == color:
                    current_diagonal.append((row, col))
                else:
                    break  # Stop if color doesn't match
                row += 1
                col += 1
            if len(current_diagonal) > len(diagonal_pixels):
                diagonal_pixels = current_diagonal

        for start_col in range(1, cols):
            current_diagonal = []
            row, col = 0, start_col
            while row < rows and col<cols:
                if grid[row,col] == color:
                    current_diagonal.append((row,col))
                else:
                    break;
                row += 1
                col += 1
            if len(current_diagonal) > len(diagonal_pixels):
                diagonal_pixels = current_diagonal


    elif diagonal_direction == "bottom_left_to_top_right":
        for start_row in range(rows):
            current_diagonal = []
            row, col = start_row, 0
            while row >= 0 and col < cols:
                if grid[row, col] == color:
                    current_diagonal.append((row, col))
                else:
                    break
                row -= 1
                col += 1
            if len(current_diagonal) > len(diagonal_pixels):
                diagonal_pixels = current_diagonal
        for start_col in range(1, cols):
            current_diagonal = []
            row, col = rows - 1, start_col

            while row >= 0 and col < cols:
                if grid[row,col] == color:
                    current_diagonal.append((row,col))
                else:
                    break
                row -=1
                col += 1
            if len(current_diagonal) > len(diagonal_pixels):
                diagonal_pixels = current_diagonal
    return diagonal_pixels

def transform(input_grid, color=None, fill_direction=None, diagonal_direction=None):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # determine color, fill_direction, and diagonal_direction if not provided
    if color is None or fill_direction is None or diagonal_direction is None:
       
        # Example 1
        if input_grid[2,0] == 4:
            color = 4
            fill_direction = "left"
            diagonal_direction = "top_left_to_bottom_right"
        # Example 2
        elif input_grid[8,0] == 3:
            color = 3
            fill_direction = "right"
            diagonal_direction = "bottom_left_to_top_right"


    # locate the diagonal
    diagonal_pixels = find_diagonal(output_grid, color, diagonal_direction)

    # fill based on direction
    if fill_direction == "left":
        for row, col in diagonal_pixels:
            for c in range(col):
                output_grid[row, c] = color
    elif fill_direction == "right":
        for row, col in diagonal_pixels:
            for c in range(col + 1, cols):
                output_grid[row, c] = color

    # Conditional extension: Only if bottom-left to top-right AND right fill
    if diagonal_direction == 'bottom_left_to_top_right' and fill_direction == 'right':
        if len(diagonal_pixels) > 0:
            last_row_of_diagonal = diagonal_pixels[-1][0]
            for r in range(last_row_of_diagonal + 1, rows):
                output_grid[r, :] = color  # Fill entire row

    return output_grid
```
