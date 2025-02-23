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

**Observations:**

*   **Input Grid:**
    *   We see two distinct objects made of color 8 (azure).
    *   One object is a vertical line of length 2 in the second column.
    *   The other object is a horizontal line of length 2 in the fourth row, sixth and seventh columns.

*   **Output Grid:**

    *   The azure objects (color 8) remain unchanged in position and shape.
    *   Two new cells with color 1 (blue) are present.
    *    One blue cell is to the right of the vertical line at \[1,2].
    *   One blue cell is to the left of the horizontal line at \[4,5]

**Natural Language Program:**

1.  **Identify Objects:** Locate all objects composed of color 8 (azure).
2.  **Preserve Objects:** Maintain these azure objects in the same position and shape.
3. **Vertical line**: Add a blue cell (color 1) on the right of the object.
4. **Horizontal line**: Add a blue cell (color 1) on the left of the object.

**Transformation Rule Summary:**

The transformation preserves the azure (8) objects and adds a blue cell (1) next to it, to its right if it is a vertical line, and to its left if it is a horizontal line.

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
