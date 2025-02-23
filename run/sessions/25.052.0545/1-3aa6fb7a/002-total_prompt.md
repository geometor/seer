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

**Observations**

First, let's describe the input and output grids in terms of objects and their properties:

**Input Grid:**

*   There are two azure (8) colored objects.
*   The first object is an L-shape composed of three cells in the top-left.
*    The second object is an inverted-L shape composed of three cells in the bottom right.

**Output Grid:**

*   There are two azure (8) colored objects (same as input).
*    There are two new single-celled blue (1) object appearing "inside" the original azure objects, one on the left branch of each L.

**Transformation Rule (Natural Language Program)**

Here's a step-by-step description of the transformation:

1.  **Identify Azure Objects:** Locate all azure (8) colored objects in the input grid.

2.  **Analyze Shape:** For each azure object, check their shape. In this case they all form either L or inverted L.

3.  **Insert Blue Pixel:** For an azure object, select its leftmost vertical segment. Add a blue pixel (1) to the right of that segment.

**Summary of differences**

The transformation rule places a blue pixel beside the left side of each azure L.

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
