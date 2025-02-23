# 1-3aa6fb7a • 011 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids for the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape:  2x1 vertical rectangles and many single azure cells
        positions:
          - (0,4), (0,5)
          - (1,5)
          - (2,2)
          - (3,2), (3,3)
          - (5,4)
          - (6,3), (6,4)
      - color: 0 (white)
        shape: Background
        positions: All other cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: 2x1 vertical rectangles and many single azure cells
        positions:
          - (0,4), (0,5)
          - (1,5)
          - (2,2)
          - (3,2), (3,3)
          - (5,4)
          - (6,3), (6,4)
      - color: 1 (blue)
        shape: single cells
        positions:
            - (1,4)
            - (2,3)
            - (5,3)

      - color: 0 (white)
        shape: Background
        positions: All other cells
```

**Natural Language Program:**

Here's a step-by-step description of the observed transformation:

1.  **Identify Objects:** In the input grid, we can see azure (color 8) objects. Some of them are single cells, some of them are 2x1 vertical rectangles.

2.  **Observe Changes:**  The azure objects are the same in the input and output. In the output, a new blue cell is placed. By observation, the blue pixel is put at the right side of the top cell of each 2x1 azure vertical rectangle.

3. **Infer the Rule:** It is confirmed that, for each 2x1 vertical azure rectangle, a blue pixel is added to the right of the upper azure cell of each vertical object.

**Transformation Rule (Concise):**

Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of the top cell that constitutes the 2x1 azure object.

```python
"""
Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of the top cell that constitutes the 2x1 azure object.
"""

import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Locate each 2x1 vertical rectangle of azure color (8).
    Add a blue cell (1) to the immediate right of the top cell of the 2x1 azure object.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    for top_coord, _ in azure_rectangles:
        # Add a blue cell to the right of the top cell, if within bounds
        if top_coord[1] + 1 < output_grid.shape[1]:
            output_grid[top_coord[0], top_coord[1] + 1] = 1


    return output_grid
```

