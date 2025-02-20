# 1-3aa6fb7a • 004 • example_2 - CODE

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
    - object_1:
        color: 8 (azure)
        shape: L-shape (rotated 180 degrees)
        position: (1,1) & (2,1) & (2,2)
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (3,4) & (3,5) & (4,5)
  output_grid:
     - object_1:
        color: 8 (azure)
        shape: L-shape (rotated 180 degrees)
        position: (1,1) & (2,1) & (2,2)
    - object_2:
        color: 8 (azure)
        shape: L-shape
        position: (3,4) & (3,5) & (4,5)
    - object_3:
        color: 1 (blue)
        shape: single cell
        position: (1,2)
     - object_4:
        color: 1 (blue)
        shape: single cell
        position: (4,4)

```

**Natural Language Description:**

The input grid contains two L-shaped objects of color 8 (azure). The first L-shape made of azure color is at row 2-3 and column 2-3, with one arm point to up, and one arm pointing to the right. The second object is at row 4-5, col 5-6, with one arm point up, and one arm point to left. The output grid contains the same two L-shaped azure color at the same location and shape as the input. In addition, the two vertexes' positions of the two azure L-shapes appear single-celled blue color.

**Transformation Rule (Natural Language Program):**

1.  **Identify** all L-shaped objects of color 8 (azure) in the input grid.
2.  **Preserve** these L-shaped objects in the output grid, maintaining their original positions and shapes.
3.  **Locate** the vertex (the "corner" cell where the two arms of the L-shape meet) of each identified L-shape.
4. **Introduce** the blue color at the location of the vertexes, as well as the location of the upper arm (the cell above the vertex).

This rule explains how to go from the input grid to the output grid.

```python
"""
The input grid contains two L-shaped objects of color 8 (azure). The output grid preserves these L-shaped objects. 
Additionally, a single blue (color 1) cell is added at the vertex of each L-shape.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds the vertices of L-shaped objects of a specific color in the grid.
    Returns a list of (row, col) tuples representing the vertex coordinates.
    """
    vertices = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Check for 2x2 blocks and identify L-shapes
            block = grid[r:r+2, c:c+2]
            if np.sum(block == color) == 3:
                # Find the vertex of the L-shape within the 2x2 block
                if block[0, 0] == color and block[0, 1] == color and block[1, 0] == color:
                  if r > 0 and grid[r-1,c] == color:
                    continue
                  vertices.append((r + 1, c + 1))
                elif block[0, 0] == color and block[0, 1] == color and block[1, 1] == color:
                  if r > 0 and grid[r-1,c+1] == color:
                    continue
                  vertices.append((r + 1, c))
                elif block[0, 0] == color and block[1, 0] == color and block[1, 1] == color:
                  if c+2 < cols and grid[r+1,c+2] == color:
                      continue;
                  vertices.append((r, c + 1))

                elif block[0, 1] == color and block[1, 0] == color and block[1, 1] == color:
                  if c > 0 and grid[r+1,c-1] == color:
                    continue;
                  vertices.append((r, c))
    return vertices

def transform(input_grid):
    """
    Transforms the input grid according to the L-shape vertex rule.
    """
    output_grid = np.copy(input_grid)
    l_shape_vertices = find_l_shapes(input_grid, 8)

    # Add blue cells at the vertices
    for r, c in l_shape_vertices:
        output_grid[r, c] = 1

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

Okay, let's analyze the second example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (0,4), (0,5), (1,5)
    - object_2:
        color: 8 (azure)
        shape: L-shape (rotated 90 degrees clockwise)
        position: (2,2), (3,2), (3,3)
    - object_3:
        color: 8 (azure)
        shape: L-shape (rotated 180 degrees)
        position: (5,4), (6,4), (6,5)

  output_grid:
    - object_1:
        color: 8 (azure)
        shape: L-shape
        position: (0,4), (0,5), (1,5)
    - object_2:
        color: 8 (azure)
        shape: L-shape (rotated 90 degrees clockwise)
        position: (2,2), (3,2), (3,3)
    - object_3:
        color: 8 (azure)
        shape: L-shape (rotated 180 degrees)
        position: (5,4), (6,4), (6,5)
    - object_4:
        color: 1 (blue)
        shape: single cell
        position: (1,4)
    - object_5:
        color: 1 (blue)
        shape: single cell
        position: (2,3)
    - object_6:
        color: 1 (blue)
        shape: single cell
        position: (5,3)
```

**Natural Language Description:**

The input grid has three L-shaped objects, all colored azure (8). The output grid contains the same three L-shaped objects, in the same positions and orientations.  Additionally, the output grid has a single blue (1) cell placed at the vertex (corner) of each of the azure L-shapes.

**Transformation Rule (Natural Language Program):**

1.  **Identify** all L-shaped objects of color 8 (azure) in the input grid.
2.  **Copy** these L-shaped objects to the output grid, maintaining their original positions and shapes.
3.  **Find** the vertex (corner cell) of each L-shaped object.
4.  **Place** a blue (color 1) cell at the vertex location of each L-shaped object in the output grid.

The Python code provided in the previous response correctly implements this rule. No changes are necessary to the `transform` or `find_l_shapes` function. This example confirms the correctness of the previous solution, including handling of multiple L-shapes and different orientations.

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
