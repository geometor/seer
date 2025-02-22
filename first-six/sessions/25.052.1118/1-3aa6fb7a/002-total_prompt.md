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

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical rectangles
      positions:
        - top-left corner at (1,1)
        - top-left corner at (3,4)
    - color: 0 (white)
      shape: background
      positions:
        - all cells not occupied by azure objects

output_grid:
  objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical rectangles
      positions:
        - top-left corner at (1,1)
        - top-left corner at (3,4)
    - color: 1 (blue)
      shape: two single-cell objects
      positions:
         - (2,2)
         - (4,5)
    - color: 0 (white)
      shape: background
      positions:
        - all cells not occupied by azure or blue objects
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** Locate all azure (color 8) objects in the input grid.  There are two such objects, each a 2x1 vertical rectangle.

2.  **Observe Invariance**: The Azure objects do not change position or shape.

3.  **Add a Blue Pixel**. For each azure (color 8) object:
    *   A blue pixel is added to the direct right of the top cell of the azure object (at the same level)

**Transformation Rule Summary**

The transformation preserves existing azure colored vertical rectangles and adds blue pixels (1) next to each top part of the azure rectangles.

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
