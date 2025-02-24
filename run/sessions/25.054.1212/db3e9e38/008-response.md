# db3e9e38 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid by expanding a vertical orange line into a checkerboard pattern of orange and azure, leaving the area below the line unchanged.
"""

import numpy as np

def find_orange_line(grid):
    """Finds the vertical orange line in the grid."""
    rows, cols = grid.shape
    for j in range(cols):
        for i in range(rows):
            if grid[i, j] == 7:
                # Found start of potential line
                start_row = i
                end_row = i
                while end_row + 1 < rows and grid[end_row + 1, j] == 7:
                    end_row += 1
                return start_row, end_row, j
    return None, None, None

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    start_row, end_row, col = find_orange_line(input_grid)

    if start_row is None:  # No orange line found
        return output_grid

    rows, cols = input_grid.shape

    # Checkerboard expansion
    for i in range(start_row, end_row + 1):
           if i - 1 >= 0 :
              if output_grid[i-1,col] == 0:
                output_grid[i-1, col] = 8
           if i + 1 < rows and i + 1 <= end_row:
              if output_grid[i + 1, col] == 0:
                output_grid[i+1, col] = 8
           if col - 1 >= 0 :
              if output_grid[i,col-1] == 0:
                output_grid[i, col-1] = 8
           if col + 1 < cols :
              if output_grid[i,col+1] == 0:
                output_grid[i, col+1] = 8
    return output_grid
```
