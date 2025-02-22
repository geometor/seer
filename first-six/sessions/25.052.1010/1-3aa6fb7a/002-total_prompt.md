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

**YAML Block Summary**

```yaml
observations:
  - object_1:
      color: 8 (azure)
      shape: Two separate 2x1 rectangles
      position: 
        - Top rectangle: Starts at row 2, column 2
        - Bottom rectangle: Starts at row 4, column 5
      count: 2
  - object_2:
      color: 1 (blue)
      shape: single cell 
      position: NA
      count: 2 in the output.
```

**Natural Language Description of the Transformation**

1.  **Identify Objects:** In the input grid, we can identify two separate objects of color 8 (azure). Each object is a 2x1 rectangle.

2.  **Transformation Rule:**
    *   Locate the top right corner of object 1 (top rectangle). Insert color 1 (blue) at this cell.
    *   Locate the bottom left corner of object 2 (bottom rectangle). Insert color 1 (blue) at this cell.

**Explanation of the "Story"**

The transformation rule looks like adding number "1" (blue color) at the corners of shape 8.


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
