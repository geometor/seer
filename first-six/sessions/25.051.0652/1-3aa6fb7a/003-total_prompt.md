# 1-3aa6fb7a • 003 • example_2 - NLP

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

Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

Here's a YAML block summarizing the initial observations:

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (rotated)
        count: 2
        positions:
          - top-left: [1,1]
          - bottom-right: [3,4]
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (rotated)
        count: 2
        positions:
          - top-left: [1,1]
          - bottom-right: [3,4]
      - color: 1 (blue)
        shape: single cell
        count: 2
        positions:
          - next to top-left azure shape: [1,2]
          - next to bottom-right azure shape: [4,5]

```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Objects:** In the input grid, there are two L-shaped objects of color 8 (azure).

2.  **Preserve Objects:** These objects persist.

3.  **Introduce New Objects:** For the two L-shaped objects on the left, place a single cell of color 1 (blue) to their immediate right.

**Natural Language Program**
The "story" of each task is a description of how the input data is transformed to the output data as a general rule.

1.  Locate all occurrences of the L-shaped object of color 8 (azure).
2.  For each identified L-shaped object, if it is positioned on the left of the image, insert a single cell of color 1 (blue) directly to the right of the object.

```python
"""
Transformation Rule:
1. Locate all occurrences of the L-shaped object of color 8 (azure).
2. For each identified L-shaped object, if it is positioned on the left of the image, insert a single cell of color 1 (blue) directly to the right of the object.
"""

import numpy as np

def find_l_shape_objects(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of (row, col) tuples representing the corner of the L-shape.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            if grid[r, c] == color:
                # Check for L-shape (rotated and normal)
                if grid[r + 1, c] == color and grid[r, c + 1] == color:
                    objects.append((r, c))
                elif grid[r, c+1] == color and grid[r+1,c+1] == color:
                    objects.append((r,c))


    return objects

def is_object_on_left(grid, obj_pos):
    """
    Checks the object is on the left part of the grid.

    """
    rows, cols = grid.shape
    
    if obj_pos[1] < cols/2 :
        return True

    return False

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    objects = find_l_shape_objects(output_grid, 8)

    for obj_pos in objects:
        if is_object_on_left(output_grid, obj_pos):
            # Determine the position to insert the blue cell
            insert_row, insert_col = obj_pos
            
            #check which kind of L-shape and adjust insert_col:
            rows, cols = output_grid.shape
            if insert_col + 1 < cols and output_grid[insert_row,insert_col+1] == 8 :   
                insert_col += 2  # Insert to the right of the object
            else:
                insert_col +=1

            # check boundaries
            if 0 <= insert_row < rows and 0 <= insert_col < cols:

                # Insert blue cell (color 1)
                output_grid[insert_row, insert_col] = 1

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

![Image](003-example_2_input.png)


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

![Image](003-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
