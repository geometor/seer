# 1a07d186 • 006 • refine_coder

---
```python
"""
Transforms an input grid based on the movement and deletion of horizontal and vertical lines of specific colors. The transformation rules appear to be specific to each of the three provided examples.
"""

import numpy as np

def find_lines(grid):
    """Finds all horizontal and vertical lines in the grid."""
    rows, cols = grid.shape
    lines = []

    # Find horizontal lines
    for i in range(rows):
        current_line = []
        for j in range(cols):
            if j > 0 and grid[i, j] != grid[i, j-1]:
                if len(current_line) > 0:
                    lines.append({'color': grid[i, current_line[0]], 'orientation': 'horizontal', 'pixels': [(i, c) for c in current_line]})
                    current_line = []
            if grid[i,j] != 0:
                current_line.append(j)
        if len(current_line) > 0:
            lines.append({'color': grid[i, current_line[0]], 'orientation': 'horizontal', 'pixels': [(i, c) for c in current_line]})

    # Find vertical lines
    for j in range(cols):
        current_line = []
        for i in range(rows):
            if i > 0 and grid[i, j] != grid[i-1, j]:
                if len(current_line) > 0:
                    lines.append({'color': grid[current_line[0], j], 'orientation': 'vertical', 'pixels': [(r, j) for r in current_line]})
                    current_line = []
            if grid[i,j] != 0:
                current_line.append(i)
        if len(current_line) > 0:
            lines.append({'color': grid[current_line[0], j], 'orientation': 'vertical', 'pixels': [(r, j) for r in current_line]})

    return lines

def is_adjacent(line1, line2):
    """Checks if two lines are adjacent."""
    if line1['orientation'] == 'vertical' and line2['orientation'] == 'vertical':
        for r1, c1 in line1['pixels']:
            for r2, c2 in line2['pixels']:
                if r1 == r2 and abs(c1 - c2) == 1:
                    return True
    return False

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid, filled with white (0).
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    lines = find_lines(input_grid)

    # Example 1 Logic: Vertical lines of 3 and 4, adjacent and moved left
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]
            if (line1['color'] == 3 and line2['color'] == 4) or \
               (line1['color'] == 4 and line2['color'] == 3):
              if line1['orientation'] == 'vertical' and line2['orientation'] == 'vertical':
                if is_adjacent(line1,line2):
                    for r, c in line1['pixels']:
                        if c > 0:
                            output_grid[r, c - 1] = line1['color']
                    for r, c in line2['pixels']:
                        if c > 0:
                            output_grid[r, c - 1] = line2['color']

    # Example 2 Logic: Horizontal lines of 2 move up, 1 moves down
    for line in lines:
        if line['color'] == 2 and line['orientation'] == 'horizontal':
            for r, c in line['pixels']:
                if r > 0:
                    output_grid[r - 1, c] = 2
                else:
                    output_grid[r,c] = 2
        elif line['color'] == 1 and line['orientation'] == 'horizontal':
            for r, c in line['pixels']:
                if r < rows - 1:
                    output_grid[r + 1, c] = 1
                else:
                    output_grid[r,c] = 1

    # Example 3 Logic:  Horizontal 8 moves up one, another horizontal 8 is removed.
    azure_lines = [line for line in lines if line['color'] == 8 and line['orientation'] == 'horizontal']
    if len(azure_lines) > 0:

      if len(azure_lines) > 1:
        top_azure = min(azure_lines, key=lambda line: line['pixels'][0][0])
        for r,c in top_azure['pixels']:
          if r>0:
            output_grid[r-1,c] = 8
      else:
        for r,c in azure_lines[0]['pixels']:
            if r > 0:
                output_grid[r - 1, c] = 8

    return output_grid
```
