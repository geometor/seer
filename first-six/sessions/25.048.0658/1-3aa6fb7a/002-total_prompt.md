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

<PIL.Image.Image image mode=RGB size=448x448 at 0x720C51F12D40>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x720C51F13BB0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
observations:
  input_grid:
    objects:
      - color: 8
        shape: two separate 2x1 vertical shapes and two single 1x1 squares.
        position: 
          - One 2x1 shape at (1,1), (2,1)
          - One 1x1 shape at (2,2)
          - One 2x1 shape at (3,4), (4,4)
          - One 1x1 shape at (3,5)
    background_color: 0
    size: 7x7

  output_grid:
      - color: 8
        shape: same as input.
        position: same as input.
      - color: 1
        shape: 1x1.
        position: replaces single square objects of color 8.
    background_color: 0
    size: 7x7

```

**Natural Language Program**

Here's a step-by-step description of the transformation rule:

1.  **Identify Objects:** In the input grid, locate all the objects that are azure (color 8).
2.  **Categorize:** Identify if an object of colour 8 consists of 2 vertically stacked squares, or a single 1x1 square.
3.  **Conditional Replacement:** All single azure (color 8) square objects are replaced by blue (color 1).
4. **Preservation:** All other azure objects, and empty cells maintain their original color.

In essence, single-celled azure objects are replaced with blue, while others, bigger objects, are preserved, as well as the white background.

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
