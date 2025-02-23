# 3-1e0a9b12 • 005 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Block Observation**

```yaml
observations:
  input_grid:
    size: 6x6
    objects:
      - color: 0 (white)
        count: 28
        shape: background
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [(0, 5)]
      - color: 8 (azure)
        count: 2
        shape: isolated cells
        positions: [(1, 3), (4, 3)]
      - color: 4 (yellow)
        count: 3
        shape: vertical line
        position: column 0, rows 3-5
      - color: 7 (orange)
        count: 2
        shape: vertical line
        position: column 2, rows 4-5
  output_grid:
    size: 6x6
    objects:
      - color: 0 (white)
        count: 28
        shape: background
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [(5, 5)]
      - color: 8 (azure)
        count: 2
        shape: vertical line
        position: column 3, rows 4-5
      - color: 4 (yellow)
        count: 3
        shape: vertical line
        position: column 0, rows 3-5
      - color: 7 (orange)
        count: 2
        shape: vertical line
        position: column 2, rows 4-5
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** Identify all colored cells.

2.  **Object Preservation**: All the objects and colors persist.

3. **Move Objects Down:** Move objects to the bottom of the grid, one above the other.

4.  **Preserve Vertical Stacks:** If multiple cells of the same color form a contiguous vertical line in the input, they remain stacked vertically in the output. We can see that color yellow(4), color orange(7) and color azure(8) remain stacked.

5. **Preserve Column:** The non-white objects stay in their original column.

6.  **Stack Within Columns:** Within each column, objects "stack" at the bottom, filling upwards. If a column has a connected vertical line, that line is preserved as a single unit during stacking.

7. **Fill Remaining:** Empty spaces are filled with white.

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

