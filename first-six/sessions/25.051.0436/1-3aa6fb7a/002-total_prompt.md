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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Input**

```yaml
objects:
  - color: 8 (azure)
    shape: Two separate 2x1 vertical lines
    positions:
      - (1,1) and (2,1) # y, x coordinates of the top-left corner
      - (3,4) and (4,4) # y, x coordinates of the top-left corner
```

**Transformation Rule: Natural Language Program**

1.  **Identify Objects:** Locate all objects of color 8 (azure) in the input grid. In this case, there are two separate 2x1 vertical lines of azure color.

2.  **Determine Action:**  For each of the separate vertical azure colored objects, we are changing color of the pixel to the immediate right of each of its ends to color 1 (blue).

3.  **Apply Rule:**
   *   For the first azure object at positions (1,1) and (2,1):
      *   The pixel to the right of (1,1) is (1,2). Change its color to 1.
      *   The pixel that is to the right of (2,1) is already part of the first object. No change.

   *   For the second azure object at positions (3,4) and (4,4):
      *    The pixel that is to the right of (4,4) is already part of the second object. No change
      *   The pixel to the right of (3,4) is (4,5). Change its color to 1.

4.  **Output:** The remaining grid is unchanged.

**Summary**

The transformation rule involves identifying separated, vertical and azure-colored objects in the input and applying a color change (to blue) of the pixels that are at either end and to their immediate right (if it is empty). This rule accurately transforms the provided input grid to the output grid.

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
