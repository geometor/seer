# 2-0ca9ddb6 • 009 • example_3 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 2
      position: (2, 2)
      shape: single cell
    - color: 1
      position: (7, 3)
      shape: single cell
    - color: 6
      position: (5, 6)
      shape: single cell
  dimensions: (9, 9)

output_grid:
  objects:
    - color: 2
      position: (2, 2)
      shape: single cell
    - color: 1
      position: (7, 3)
      shape: single cell
    - color: 6
      position: (5, 6)
      shape: single cell
    - color: 4
      positions: [(1, 1), (1, 3), (3, 1), (3, 3)]
      shape: single cells forming a square-like pattern
    - color: 7
      positions: [(6, 3), (7, 2), (7, 4), (8, 3)]
      shape: single cells forming a cross-like pattern
  dimensions: (9, 9)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify initial objects:** In the input grid, we have three single-cell objects: color 2 at (2, 2), color 1 at (7, 3), and color 6 at (5,6).

2.  **Preserve Singletons:** The single cells of colors 2, 1, and 6 from the input are preserved in the output.

3.  **Color 4 insertion (around color 2):**
    *   Two cells of color 4 are added in the row *above* the color 2 cell, one column to the left and one to the right.
    *   Two cells of color 4 are added in the row *below* the color 2 cell, one column to the left and one to the right.

4.  **Color 7 insertion (around color 1):**
    *   One cell of color 7 is placed directly *above* the color 1 cell.
    *    Cells of color 7 fill the 3x3 neighborhood around the original cell *excluding* the cell itself and its horizontal neighbors.

5.  **Color 6 Preservation:** The color 6 cell remains unchanged. This is a no-op, but important to identify explicitly, since in previous tasks all special single cells were modified.

**Transformation Rule Summary**

The transformation preserves all single cells. New color cells are added in specific patterns around the original positions of color 2 (using color 4) and color 1 (using color 7) cells. The color 6 cell is preserved but undergoes no change in its surroundings.

```python
"""
The transformation preserves single cells of colors 2, 1 and 6. It then introduces new objects based on the positions of cells of color 2 and 1.

For each cell of color 2:
- Two cells of color 4 are placed in the row above, one column to the left and right.
- Two cells of color 4 are placed in the row below, one column to the left and right.

For each cell of color 1:
- A cell of color 7 is placed in the row above.
- Cells of color 7 fill the 3x3 neighborhood around the original cell, excluding the cell itself and its horizontal neighbors.
"""

import numpy as np

def find_objects(grid, color):
    # Find coordinates of all cells with the specified color.
    return np.array(np.where(grid == color)).T

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    #output_grid = np.zeros_like(input_grid)

    # Find the objects of color 2, 1 and 6.
    objects_2 = find_objects(input_grid, 2)
    objects_1 = find_objects(input_grid, 1)
    objects_6 = find_objects(input_grid, 6)
    
    # Apply rules for object of color 2.
    for obj_2 in objects_2:
        row, col = obj_2
        if row - 1 >= 0:
            if col - 1 >= 0:
                output_grid[row - 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row - 1, col + 1] = 4
        if row + 1 < output_grid.shape[0]:
            if col - 1 >= 0:
                output_grid[row + 1, col - 1] = 4
            if col + 1 < output_grid.shape[1]:
                output_grid[row + 1, col + 1] = 4

    # Apply rules for object of color 1.
    for obj_1 in objects_1:
        row, col = obj_1
        if 0 <= row - 1 < output_grid.shape[0]:
            output_grid[row - 1, col] = 7  # Above

        # 3x3 neighborhood excluding horizontal neighbors
        for i in range(max(0, row - 1), min(row + 2, output_grid.shape[0])):
            for j in range(max(0, col - 1), min(col + 2, output_grid.shape[1])):
                if (i, j) != (row, col) and j==col: #exclude also the horizontal neighbors
                    output_grid[i, j] = 7
                    
    return output_grid
```

