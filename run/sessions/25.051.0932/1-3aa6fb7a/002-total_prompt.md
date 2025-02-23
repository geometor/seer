# 1-3aa6fb7a • 002 • example_1 - CODE

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
