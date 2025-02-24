# 3aa6fb7a • 010 • refine_coder

---
```python
"""
Identifies horizontal lines of exactly two contiguous azure (8) pixels and adds a
blue (1) pixel to the immediate left or right of the line, replacing a white (0)
pixel, if one exists.
"""

import numpy as np

def find_two_azure_lines(grid):
    # type: (np.ndarray) -> list
    """Finds all horizontal lines of exactly two contiguous azure (8) pixels."""
    rows, cols = grid.shape
    two_azure_lines = []
    for row in range(rows):
        for col in range(cols - 1):  # Iterate up to the second-to-last column
            if grid[row, col] == 8 and grid[row, col + 1] == 8:
                #check that there are no other azure pixels next to this line
                is_two_pixel_line = True
                if col > 0: #check left
                    if grid[row, col-1] == 8:
                        is_two_pixel_line = False
                if col < cols - 2:
                    if grid[row, col+2] == 8:
                        is_two_pixel_line = False
                if is_two_pixel_line:
                    two_azure_lines.append((row, col, row, col + 1))  # Store start and end coordinates
    return two_azure_lines

def transform(input_grid):
    # type: (np.ndarray) -> np.ndarray
    """Transforms the input grid by adding blue pixels to the left or right of two-pixel azure lines."""

    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find all two-pixel azure lines
    azure_lines = find_two_azure_lines(input_grid)

    # Iterate through each identified line
    for line in azure_lines:
        row_start, col_start, row_end, col_end = line

        # Check for white pixel to the left
        if col_start > 0 and output_grid[row_start, col_start - 1] == 0:
            output_grid[row_start, col_start - 1] = 1

        # Check for white pixel to the right
        if col_end < cols - 1 and output_grid[row_end, col_end + 1] == 0:
            output_grid[row_end, col_end + 1] = 1

    return output_grid
```
