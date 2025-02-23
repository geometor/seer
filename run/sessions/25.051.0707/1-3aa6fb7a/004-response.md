# 1-3aa6fb7a • 004 • example_2 - CODE

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)  # First line
          - (4,4), (5,4)  # Second line
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two 2x1 vertical lines
        positions:
          - (1,1), (2,1)
          - (4,4), (5,4)
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,2)
          - (4,4)
      - color: 0 (white)
        shape: background
        positions: fills the rest of the grid
```

**Natural Language Description of Transformation:**

1.  **Identify Objects:** In the input grid, we have two vertical lines of color 8 (azure), each two cells high. The rest of the grid is filled with color 0 (white).

2.  **Detect Changes:** We can see changes in the output inside each one of the azure lines. In the output grid, the azure lines that were found in the input, are kept intact.

3.  **Describe Action:** Within each azure line, the program searches for the cell located immediately to the right of the top cell of each vertical line. The color of this cell is changed to 1 (blue). If the cell to the right of the bottom cell of each line is also azure, it keeps its original color.

**Natural Language Program**
```
for each vertical azure line in the input:
    find top_cell
    find right_neighbor = cell to the right of the top_cell
    set color of right_neighbor to blue
    
```

```python
"""
The transformation rule identifies vertical lines of color 8 (azure) in the input grid.
For each of these lines, it finds the cell immediately to the right of the top cell of the line.
The color of this cell is then changed to 1 (blue) in the output grid. The azure lines themselves are kept.
"""

import numpy as np

def find_vertical_lines(grid, color):
    """
    Finds vertical lines of a specified color in the grid.
    Returns a list of (row, col) tuples representing the top cell of each line.
    """
    lines = []
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                lines.append((r, c))
    return lines

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    azure_lines = find_vertical_lines(input_grid, 8)

    for top_row, top_col in azure_lines:
        # Find the cell to the right of the top cell
        right_neighbor_row = top_row
        right_neighbor_col = top_col + 1

        # Check if the right neighbor is within bounds
        if right_neighbor_col < output_grid.shape[1]:
            output_grid[right_neighbor_row, right_neighbor_col] = 1

    return output_grid
```

