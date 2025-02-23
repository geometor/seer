# 3-1e0a9b12 • 005 • example_3 - NLP

---
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  dimensions: 5x5
  objects:
    - color: 1 (blue)
      positions: [(0, 3), (2, 3)]
    - color: 3 (green)
      positions: [(1, 1), (2, 1), (4, 1)]
    - color: 2 (red)
      positions: [(2, 4)]
    - color: 6 (magenta)
      positions: [(3, 0)]
    - color: 0 (white)
      positions: All the remaining cells
  background_color: 0 (white)

output_grid:
  dimensions: 5x5
  objects:
    - color: 1 (blue)
      positions: [(3, 3)]
    - color: 3 (green)
      positions: [(2, 1), (3, 1)]
    - color: 2 (red)
      positions: [(4, 4)]
    - color: 6 (magenta)
      positions: [(4, 0)]
      - color: 0 (white)
      positions: All the remaining cells
  background_color: 0 (white)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid contains objects of colors 1 (blue), 3 (green), 2 (red) and 6 (magenta). All other cells are 0 (white).

2.  **Move Objects:** The program proceeds as follow:

    \- All the colored objects are moved to the last rows, preserving the column order. In detail:
    - The object of color 6 moves from (3, 0) to (4, 0).
    - The object of color 3 in position (1,1) moves to (2,1). The other two objects of color 3 moves to (3,1) and (4,1).
    - The object of color 1 in position (0, 3) moves to (3,3). The other object of color 1 moves to (4,3).
    - The object of color 2 moves from (2,4) to (4,4).

3.  **Final Output**: The cells that are not occupied by the moved objects become, or remain, 0.

In summary, all the colored objects are moved to the last rows preserving the column order. The first object of a certain colors is moved to the row with index equal to the total number of istances of that color.

```python
"""
The transformation rule is as follows:
1. Identify all the colored objects.
2. Move the objects to the last rows, preserving the columns and putting the i-th object of color c to the row with index equal to the total number of objects of color c.
3. All other cells in the grid, not occupied by the moved objects, are set to 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize the output grid as a copy of the input grid, then set everything to 0.
    output_grid = np.zeros_like(input_grid)
    
    # Get the dimensions of the input grid.
    rows, cols = input_grid.shape
    
    # Create a dictionary to count and track colored cells.
    color_counts = {}
    
    # Iterate through the input grid to find single-cell objects (non-zero cells).
    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:
                # Update color count
                if color not in color_counts:
                    color_counts[color] = [0,0] #count, row_index
                color_counts[color][0] += 1

    # Iterate through the input grid to find single-cell objects (non-zero cells).
    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:
                # Move the object to the correct row.
                output_grid[color_counts[color][0]-1-color_counts[color][1], c] = color
                color_counts[color][1] += 1
                
    return output_grid
```

