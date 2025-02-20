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
    *   The other object is a horizontal line of length 2 in the fourth row, starting from the fifth column.
    *   The rest of the grid is filled with color 0 (white).

*   **Output Grid:**
    *   The azure objects (color 8) are preserved in the same positions.
    *   Two new cells with color 1 (blue) appear.
    *    One blue cell appears at position (1,2), inmediately to the right of the element (1,1).
    *    The second blue cell is located in the position (4,5), inmediately to the left of the element (4,6).

**Natural Language Program:**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid.
2.  **Preserve:** Keep these azure objects in their original positions in the output grid.
3. **Paint:**
    *    If the element to the right of a position occupied by a blue object has a different color (other than 8), paint it blue (1).
    *    If the element to the left of a position occupied by a blue object has a different color (other than 8), paint it blue (1).

**Transformation Rule Summary:**

The transformation preserves the azure (8) objects and adds blue (1) cells immediately to the right of the first azure element of a vertical line, and to the left of the second element of a horizontal line.

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
