# 3-1e0a9b12 • 009 • example_3 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in this new example.

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
        positions: [(0, 3), (2, 3)]
      - color: 3 (green)
        count: 3
        shape: vertical line
        positions: column 1, rows 1, 2, 4
      - color: 2 (red)
        count: 1
        shape: isolated cell
        position: [(2, 4)]
      - color: 6 (magenta)
        count: 1
        shape: isolated cell
        position: [(3, 0)]

  output_grid:
     size: 5x5
     objects:
      - color: 0 (white)
        count: 18
        shape: background
      - color: 3 (green)
        count: 3
        positions: column 1, row 2,3,4
      - color: 1 (blue)
        count: 2
        positions: [(3,3), (4,3)]
      - color: 2 (red)
        count: 1
        position: [(4, 4)]
      - color: 6 (magenta)
        count: 1
        position: [(4, 0)]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** First, identify all non-white (non-zero) colored cells.

2.  **Object Preservation:** All non-white cells persist in the output.

3.  **Move Objects Down:** Move all objects towards the bottom of the grid.
4. **Preserve Columns:** All objects remain in the same columns.
5. **Stack Within Columns:** Non-white cells "stack" downwards within their respective columns, with the lowest cell in each column moving to the last row, the next lowest to the second-to-last row, and so on.
6. **Fill Remaining:** Empty spaces are filled with white.

```python
"""
Moves objects to the bottom of the grid, preserving vertical stacks and column order, then filling the rest with white.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving objects to the bottom, maintaining vertical stacks and column order.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    for col in range(cols):
        # Extract non-zero elements and their vertical connections
        column_elements = []
        i = 0
        while i < rows:
            if input_grid[i, col] != 0:
                start_row = i
                end_row = i
                while end_row + 1 < rows and input_grid[end_row + 1, col] == input_grid[start_row, col]:
                    end_row += 1
                column_elements.append((input_grid[start_row, col], end_row - start_row + 1))
                i = end_row + 1
            else:
                i += 1

        # Place elements at the bottom of the output column
        current_row = rows - 1
        for value, height in reversed(column_elements):
            output_grid[current_row - height + 1:current_row + 1, col] = value
            current_row -= height

    return output_grid
```

