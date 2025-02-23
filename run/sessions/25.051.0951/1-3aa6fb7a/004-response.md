# 1-3aa6fb7a • 004 • refine_code - CODE

---
```python
"""
The transformation rule is as follows:

1.  **Identify Objects:** Find all vertical azure (color 8) lines that are exactly 2 pixels high and 1 pixel wide.

2.  **Transformation Rule:** For *each* identified 2x1 azure line:
    *   Place a blue pixel (color 1) immediately to the right of the *top* pixel of the azure line.
    *   If there's another azure line starting at the row below the first azure line, insert the blue line to the right of the *lower* pixel of the first line.
"""

import numpy as np

def find_vertical_lines(grid, color, height, width):
    """
    Find vertical lines of specified color, height, and width in the grid.
    """
    lines = []
    rows, cols = grid.shape
    for r in range(rows - height + 1):
        for c in range(cols - width + 1):
            if all(grid[r+i, c] == color for i in range(height)):
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    1. Find 2x1 vertical lines of azure color.
    2. Add one blue pixel at the upper-right of each of these lines,
     except if there are adjacent azure lines.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all 2x1 vertical lines of color 8 (azure)
    azure_lines = find_vertical_lines(input_grid, 8, 2, 1)

    # For each azure line, place a blue pixel (color 1) to the right of the top pixel
    for i, line in enumerate(azure_lines):
        r, c = line
        if c + 1 < output_grid.shape[1]:  # Check bounds
          if (r+1, c) in azure_lines: # Check for vertically adjacent lines
            output_grid[r+1,c+1] = 1
          else:
            output_grid[r, c + 1] = 1

    return output_grid
```

