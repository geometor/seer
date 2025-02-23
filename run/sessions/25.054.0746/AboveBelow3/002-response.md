# AboveBelow3 • 002 • example_1 • investigate_coder

---
```python
"""
Identify all horizontal lines of pixels with the color green (value 3).
Delete the top green horizontal line.
"""

import numpy as np

def find_horizontal_lines(grid, color):
    lines = []
    for i, row in enumerate(grid):
        start = -1
        for j, pixel in enumerate(row):
            if pixel == color:
                if start == -1:
                    start = j
            elif start != -1:
                lines.append((i, start, j - 1))
                start = -1
        if start != -1:
            lines.append((i, start, len(row) - 1))
    return lines

def transform(input_grid):
    """
    Transforms the input grid by removing the top horizontal green line.
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find all horizontal lines of color green (3)
    green_lines = find_horizontal_lines(output_grid, 3)
    
    # Find the top-most green line.
    if green_lines:
        top_green_line_row = min(line[0] for line in green_lines)
        #remove the top green line
        for line in green_lines:
          if line[0] == top_green_line_row:
            for col in range(line[1],line[2]+1):
                output_grid[line[0]][col] = 0

    return output_grid
```

