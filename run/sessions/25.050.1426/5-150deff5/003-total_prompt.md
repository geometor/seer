# 5-150deff5 • 003 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0 0 0 0
0 0 5 5 5 5 5 0 0 0 0
0 0 0 5 5 5 0 0 0 0 0
0 0 0 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 5 0 0 0
0 0 0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0 0
0 0 8 8 2 2 2 0 0 0 0
0 0 0 2 8 8 0 0 0 0 0
0 0 0 2 8 8 8 8 0 0 0
0 0 0 2 0 0 8 8 0 0 0
0 0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

**Natural Language Program:**

The transformation applied to the input grid involves the following steps:

1. **Identify the gray object:** Locate the contiguous region of cells with color 5 (gray) in the input grid. This region constitutes the object to be transformed.

2. **Determine boundary and interior cells:** For each cell within the identified gray object, determine if it is a boundary cell or an interior cell.
    - A cell is considered a **boundary cell** if at least one of its immediate neighbors (up, down, left, right) is not part of the gray object (i.e., is color 0 or white).
    - A cell is considered an **interior cell** if all of its immediate neighbors (up, down, left, right) that are within the grid boundaries are also part of the gray object.

3. **Recolor boundary cells:** Change the color of all boundary cells of the gray object from gray (color 5) to azure (color 8).

4. **Recolor interior cells:** Change the color of all interior cells of the gray object from gray (color 5) to red (color 2).

5. **Maintain background:** All cells in the grid that are not part of the original gray object (i.e., cells with color 0 or white) remain unchanged.

In essence, the transformation outlines the gray shape with azure and fills its interior with red, while leaving the surrounding white background untouched.
```python
"""
The transformation applied to the input grid involves the following steps:

1. **Identify the gray object:** Locate the contiguous region of cells with color 5 (gray) in the input grid. This region constitutes the object to be transformed.

2. **Determine boundary and interior cells:** For each cell within the identified gray object, determine if it is a boundary cell or an interior cell.
    - A cell is considered a **boundary cell** if at least one of its immediate neighbors (up, down, left, right) is not part of the gray object (i.e., is color 0 or white).
    - A cell is considered an **interior cell** if all of its immediate neighbors (up, down, left, right) that are within the grid boundaries are also part of the gray object.

3. **Recolor boundary cells:** Change the color of all boundary cells of the gray object from gray (color 5) to azure (color 8).

4. **Recolor interior cells:** Change the color of all interior cells of the gray object from gray (color 5) to red (color 2).

5. **Maintain background:** All cells in the grid that are not part of the original gray object (i.e., cells with color 0 or white) remain unchanged.

In essence, the transformation outlines the gray shape with azure and fills its interior with red, while leaving the surrounding white background untouched.
"""

import numpy as np

def _is_boundary(grid, i, j, gray_object):
    """Helper function to check if a cell is on the boundary of the gray object."""
    rows, cols = grid.shape
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < rows and 0 <= y < cols and (x, y) not in gray_object:
            return True
    return False

def transform(input_grid):
    """Transforms the input grid by recoloring a gray object's boundary to azure and its interior to red."""
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the gray object (contiguous region of color 5)
    gray_object = set()
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 5:
                gray_object.add((i, j))

    # Determine boundary and interior cells, and recolor them
    for i, j in gray_object:
        if _is_boundary(input_grid, i, j, gray_object):
            output_grid[i, j] = 8  # Azure for boundary cells
        else:
            output_grid[i, j] = 2  # Red for interior cells

    return output_grid
```

**input**
```
0 0 0 0 0 0 0 0 0 0
0 5 5 5 5 5 5 0 0 0
0 5 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 5 5 0 0 0
0 0 0 0 5 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 0 0 0 0 0 0 0
0 8 8 2 8 8 2 0 0 0
0 8 8 2 8 8 2 0 0 0
0 0 0 2 0 0 2 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 8 8 0 0 0
0 0 0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

![Image](002-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
