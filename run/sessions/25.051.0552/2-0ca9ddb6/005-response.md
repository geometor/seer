# 2-0ca9ddb6 • 005 • example_3 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in the third example.

**Observations in YAML Format**

```yaml
observations:
  input_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (2, 2)
        shape: single cell
      - color: 1 (blue)
        position: (7, 3)
        shape: single cell
      - color: 6 (magenta)
        position: (5,6)
        shape: single cell
  output_grid:
    size: 9x9
    objects:
      - color: 2 (red)
        position: (2, 2)
        shape: single cell
      - color: 1 (blue)
        position: (7, 3)
        shape: single cell
        - color: 6 (magenta)
        position: (5,6)
        shape: single cell
      - color: 4 (yellow)
        positions: [(1, 1), (1, 3), (3, 1), (3, 3)]
        shape: single cells forming a cross pattern around red object.
      - color: 7 (orange)
        positions: [ (6,3), (7, 2), (7, 4), (8,3)]
        shape: single cells forming a cross pattern around the blue object.
```

**Natural Language Description of the Transformation Rule**

1.  **Identify Single-Cell Objects:** Find all objects in the input grid that consist of a single cell. In this case, we have several such objects:
    *   Red cell (color 2) at position (2, 2).
    *   Blue cell (color 1) at positions (7, 3).
    *    Magenta cell (color 6) at position (5,6)

2.  **Replicate and Preserve original cells:** All the single cells are preserve in their original position in the output.

3. **Draw a cross around the original color cells**: For each single-cell object, except the magenta one, a cross pattern of 2 cells wide is drawn, of a specific color for each original cell.

4.  **Prescribed color for each cross**:
      * The cross around objects of color 2 (red) is made of the color 4 (yellow).
      * The cross around objects of color 1 (blue) is made of the color 7 (orange).

In summary, the transformation identifies single-cell objects in the input, retains them and creates a cross pattern from adjacent cells around them in the output using distinct colors for different objects of the input. The exception is the magenta cell, that is preserved without any surrounding cross.

```python
"""
The transformation identifies single-cell objects in the input, retains them and creates a cross pattern from adjacent cells around them in the output using distinct colors for different objects of the input.
The exception is the single-cell object of color 6, that remains unchanged.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find single-cell objects and their positions
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                # Check if it's a single-cell object
                is_single = True
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if (dr != 0 or dc != 0) and 0 <= r + dr < rows and 0 <= c + dc < cols:
                            if grid[r + dr, c + dc] == grid[r, c]:
                                is_single = False
                                break
                    if not is_single:
                        break
                if is_single:
                    objects.append((grid[r, c], (r, c)))
    return objects

def draw_cross(grid, position, color):
    # Draw a cross pattern around the given position with specified color.
    r, c = position
    rows, cols = grid.shape
    # Define cross positions: up, down, left, right
    cross_positions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for cross_pos in cross_positions:
      cr, cc = cross_pos
      if 0 <= cr < rows and 0 <= cc < cols:
          grid[cr, cc] = color

    return grid


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)

    # Draw cross for each single cell object based on the color of input cell
    for color, pos in single_cell_objects:
        if color == 2:  # Red cell
            output_grid = draw_cross(output_grid, pos, 4)  # Yellow cross
        elif color == 1:  # Blue cell
            output_grid = draw_cross(output_grid, pos, 7)  # Orange cross
        # Color 6 remains unchanged

    return output_grid
```

