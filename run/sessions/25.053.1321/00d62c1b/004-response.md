# 00d62c1b • 004 • refine_coder

---
```python
"""
Iterates through each pixel in the input grid.
Identifies green (3) pixels.
For each green pixel, checks if it's part of a horizontal or vertical line segment of at least three contiguous green pixels.
If the condition is met, changes the pixel's color to yellow (4) in the output grid.
Pixels that are not green remain unchanged.
Returns the modified grid.
"""

import numpy as np

def get_line_length(grid, row, col, direction):
    """
    Calculates the length of a contiguous line of green pixels starting from a given position.

    Args:
        grid: The input grid.
        row: Starting row index.
        col: Starting column index.
        direction: A tuple (row_change, col_change) indicating the direction to check.
                   (0, 1) for horizontal (right), (0, -1) for horizontal (left),
                   (1, 0) for vertical (down), (-1, 0) for vertical (up).

    Returns:
        The length of the contiguous line of green pixels in the specified direction.
    """
    rows, cols = grid.shape
    length = 0
    r, c = row, col
    dr, dc = direction

    while 0 <= r < rows and 0 <= c < cols and grid[r, c] == 3:
        length += 1
        r += dr
        c += dc
    return length
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each pixel
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is green
            if output_grid[row, col] == 3:
                # Check for horizontal line segment of length >= 3
                left_length = get_line_length(output_grid, row, col - 1, (0, -1))
                right_length = get_line_length(output_grid, row, col + 1, (0, 1))
                horizontal_length = left_length + 1 + right_length  # Include the current pixel

                # Check for vertical line segment of length >= 3
                up_length = get_line_length(output_grid, row - 1, col, (-1, 0))
                down_length = get_line_length(output_grid, row + 1, col, (1, 0))
                vertical_length = up_length + 1 + down_length  # Include the current pixel

                # Change color to yellow if part of a line segment of length >= 3
                if horizontal_length >= 3 or vertical_length >= 3:
                    output_grid[row, col] = 4

    return output_grid
```
