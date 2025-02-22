# 1-3aa6fb7a • 011 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: Two 2x1 vertical rectangles
        positions:
          - (1,1), (2,1)
          - (3,4), (4,5) # Note, it's diagonal.
      - color: 0 (white)
        shape: Background
        positions: All other cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: Two 2x1 vertical rectangles
        positions:
          - (1,1), (2,1)
          - (3,4), (4,5)
      - color: 1 (blue)
        shape: Two single cells
        positions:
            - (1,2)
            - (4,4)
      - color: 0 (white)
        shape: Background
        positions: All other cells
```

**Natural Language Program:**

Here's a step-by-step description of the observed transformation:

1.  **Identify Objects:** In the input grid, we can identify two azure (color 8) objects. Each object is a 2x1 vertical rectangle. There are also a lot of white cells which act as background.

2.  **Observe Changes:** In the output grid, we see the same azure objects have not been altered. However, one new blue cell is added on the right side of each azure object.

3. **Infer the Rule:** It's inferred that for each vertical 2x1 azure (8) rectangle, we perform the action to add a blue(1) pixel at the right of its top and bottom.

**Transformation Rule (Concise):**

Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of both cells that constitute the 2x1 azure object.


```python
"""
Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of both cells that constitute the 2x1 azure object.
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
    Add a blue cell (1) to the immediate right of both cells of the 2x1 azure object.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles = find_2x1_vertical_rectangles(output_grid, 8)

    for top_coord, bottom_coord in azure_rectangles:
        # Add a blue cell to the right of the top cell, if within bounds
        if top_coord[1] + 1 < output_grid.shape[1]:
            output_grid[top_coord[0], top_coord[1] + 1] = 1
        # Add a blue cell to the right of the bottom cell, if within bounds
        if bottom_coord[1] + 1 < output_grid.shape[1]:
            output_grid[bottom_coord[0], bottom_coord[1] + 1] = 1

    return output_grid
```


**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

![Image](011-example_2_input.png)


**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

![Image](011-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
