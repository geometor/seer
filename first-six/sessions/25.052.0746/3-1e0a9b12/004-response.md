# 3-1e0a9b12 • 004 • example_2 - CODE

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Observation**

```yaml
observations:
  input_grid:
    size: 6x6
    objects:
      - color: 0 (white)
        count: 28
        shape: background
      - color: 4 (yellow)
        count: 3
        shape: vertical line
        positions: [[3,0], [4,0], [5,0]]
      - color: 7 (orange)
        count: 2
        shape: vertical line
        positions: [[4,2], [5,2]]
      - color: 8 (azure)
        count: 2
        shape: isolated cells
        positions: [[1,3], [4,3]]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [[0,5]]

  output_grid:
    size: 6x6
    objects:
      - color: 0 (white)
        count: 27
        shape: background
      - color: 4 (yellow)
        count: 3
        shape: vertical line
        positions: [[3,0], [4,0], [5,0]]
      - color: 7 (orange)
        count: 2
        shape: vertical line
        positions: [[4,2], [5,2]]
      - color: 8 (azure)
        count: 2
        shape: vertical line
        positions: [[4,3],[5,3]]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [[5,5]]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of several colored objects against a white (0) background:
    *   A vertical line of three yellow (4) cells.
    *   A vertical line of two orange (7) cells.
    *   Two azure (8) cells, one at row 1 and another at row 4 (same column).
    *   A single maroon (9) cell.

2.  **Predicate:** All colored cells (non-white) maintain their original colors throughout the transformation.

3.  **Action:**
    *   The azure (8) cells at \[1, 3] and \[4, 3] are consolidated into a single vertical line at the bottom of the grid, occupying positions \[4, 3] and \[5, 3]. The two 8s stack.
    *   The maroon (9) cell moves to the lowest available row in its column.
    *   All other colored cells remain in their original positions.

**Transformation Rule Summary**
Non-zero colored objects are moved down to the lowest available position in their respective columns, maintaining their color and x-coordinate. The previous program can produce this output. If there is a stack of objects of the same color they are grouped.

```python
"""
Non-zero colored objects are moved down to the lowest available position in their respective columns, maintaining their color and x-coordinate. If there is a stack of objects of the same color they are grouped.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the
    last row available, preserving their original x-coordinates and colors.
    """
    # Initialize the output grid as a copy of the input grid with all zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Create a dictionary to store the next available row index for each column.
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Iterate through the input grid to find and move non-zero cells.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Get the color of the current cell.
                color = input_grid[r, c]
                # Get the next available row index for the current column.
                row_index = next_available_row[c]
                # Place the cell in the output grid.
                output_grid[row_index, c] = color
                # Update the next available row index for this column.
                next_available_row[c] -= 1

    return output_grid
```

