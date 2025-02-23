# 2-0ca9ddb6 • 005 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**Observations and Documentation**

```yaml
input_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      position: (2, 6), (7,1)
      shape: single cell
    - color: 1 (blue)
      position: (3, 2), (6, 6)
      shape: single cell
    - color: 0 (white)
      position: all other cells
      shape: background

output_grid:
  size: 9x9
  objects:
    - color: 8 (azure)
      position: (0, 3)
      shape: single cell
    - color: 2 (red)
      position: (2, 6), (7,1)
      shape: single cell
    - color: 1 (blue)
      position: (3, 2), (6, 6)
      shape: single cell
    - color: 4 (yellow)
      position: (1, 5), (1, 7), (3, 5), (3, 7), (7,0), (7,2), (9,0), (9,2)
      shape: single cells forming a plus shape around red cells, but not directly touching them.
    - color: 7 (orange)
      position: (2,1), (2,3), (3,0), (3,4), (4,3), (5,6), (6,5), (6,7), (8,6)
      shape: single cells forming a plus shape around blue cells, but not directly touching them
    - color: 0 (white)
      position: all other cells
      shape: background
```

**Natural Language Description of the Transformation Rule**

1.  **Identify Target Color Cells:** Locate cells with colors blue (1) and red (2).

2.  **Create Plus Shapes:**
    *   For each identified red cell (color 2), generate a "plus" shape centered around, but *not* touching, the original cell using yellow (color 4).  The "arms" of the plus extend one cell away from the red cell.
    *   For each identified blue cell (color 1), generate a "plus" shape centered around, but *not* touching, the original cell using orange (color 7). The "arms" of the plus extend one cell away from the blue cell.

3.  **Preserve Other Cells:** Any cell that is not part of the generated "plus" shapes retains its original color (including azure (8) in this case and 0, the background).

In summary, the transformation identifies blue and red cells, then constructs "plus-shaped" patterns of specific colors around them. Azure cells are considered as the background and are not modified.

```python
"""
1.  **Identify Target Color Cells:** Locate cells with colors blue (1) and red (2).

2.  **Create Plus Shapes:**
    *   For each identified red cell (color 2), generate a "plus" shape centered around, but *not* touching, the original cell using yellow (color 4).  The "arms" of the plus extend one cell away from the red cell.
    *   For each identified blue cell (color 1), generate a "plus" shape centered around, but *not* touching, the original cell using orange (color 7). The "arms" of the plus extend one cell away from the blue cell.

3.  **Preserve Other Cells:** Any cell that is not part of the generated "plus" shapes retains its original color (including azure (8) in this case and 0, the background).
"""

import numpy as np

def create_plus_shape(grid, center, color):
    """Creates a plus shape around a center cell with a specified color."""
    rows, cols = grid.shape
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in offsets:
        r, c = center[0] + dr, center[1] + dc
        if 0 <= r < rows and 0 <= c < cols:
            grid[r, c] = color
    return grid

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:  # Red cell
                output_grid = create_plus_shape(output_grid, (r, c), 4)  # Yellow plus
            elif input_grid[r, c] == 1:  # Blue cell
                output_grid = create_plus_shape(output_grid, (r, c), 7)  # Orange plus

    return output_grid
```

