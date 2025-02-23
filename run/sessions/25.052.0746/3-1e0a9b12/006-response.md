# 3-1e0a9b12 • 006 • example_3 - CODE

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Observation**

```yaml
observations:
  input_grid:
    size: 5x5
    objects:
      - color: 0 (white)
        count: 20
        shape: background
      - color: 1 (blue)
        count: 2
        shape: isolated cells
        positions: [[0,3], [2,3]]
      - color: 2 (red)
        count: 1
        shape: isolated cell
        position: [[2,4]]
      - color: 3 (green)
        count: 3
        shape: vertical line
        positions: [[1,1], [2,1], [4,1]]
      - color: 6 (magenta)
        count: 1
        shape: isolated cell
        position: [[3,0]]

  output_grid:
    size: 5x5
    objects:
      - color: 0 (white)
        count: 18
        shape: background
      - color: 1 (blue)
        count: 2
        shape: isolated cells
        positions: [4,3],[3,3]
      - color: 2 (red)
        count: 1
        shape: isolated cell
        position: [[4,4]]
      - color: 3 (green)
        count: 3
        shape: vertical line
        positions:  [[2,1], [3,1], [4,1]]
      - color: 6 (magenta)
        count: 1
        shape: isolated cell
        position: [[4,0]]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of several colored objects against a white (0) background:

    *   Two blue (1) cells.
    *   One red (2) cell.
    *   Three green (3) cells forming a vertical line.
    *   One magenta (6) cell.
2.  **Predicate:** All non-white cells maintain their colors.

3.  **Action:**

    *   Move all colored cells down to the lowest available position in their respective columns.
    *   If multiple cells exist in the same column, stack them from bottom to top based on their original vertical order.

**Transformation Rule Summary**

The transformation involves moving all non-zero colored cells to the lowest available row in their respective columns while maintaining their original color and x-coordinate. Stack the objects by column, maintaining its original order. The existing python program correctly performs this transformation, so no changes are required.

```python
"""
The transformation involves moving all non-zero colored cells to the lowest
available row in their respective columns while maintaining their original
color and x-coordinate. Stack the objects by column, maintaining its original
order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the
    last row available, preserving their original x-coordinates and colors,
    and stacking them based on their initial order if they share a column.
    """
    # Initialize the output grid as a copy of the input grid with all zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Create a dictionary to store the next available row index for each column.
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Store non-zero cells with their original row index for sorting.
    cells_to_move = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                cells_to_move.append((r, c, input_grid[r, c]))

    # Sort cells by column and then by original row index (ascending).
    cells_to_move.sort(key=lambda x: (x[1], x[0]))

    # Iterate through the sorted non-zero cells and place them in the output grid.
    for r, c, color in cells_to_move:
        # Get the next available row index for the current column.
        row_index = next_available_row[c]
        # Place the cell in the output grid.
        output_grid[row_index, c] = color
        # Update the next available row index for this column.
        next_available_row[c] -= 1

    return output_grid
```

