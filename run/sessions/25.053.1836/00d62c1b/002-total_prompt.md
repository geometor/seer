# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7747C2C53910>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7747C2C53550>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a 2D grid (matrix) of single-digit integers, representing colors. The primary colors involved are white (0) and green (3). The transformation seems to involve a change in color of specific green (3) pixels to yellow (4) based on their position relative to other green pixels. The overall grid dimensions remain constant.

**YAML Block - Facts:**


```yaml
objects:
  - type: pixel
    properties:
      color:
        - white (0)
        - green (3)
        - yellow (4)
      position: [row, column]
relationships:
  - type: adjacency
    description: Pixels can be adjacent horizontally, vertically, or diagonally.
actions:
  - type: color_change
    trigger: Specific green pixels change to yellow.
    condition:  A green pixel changes to yellow if and only if another green pixel exist both vertically and horizontally.
```


**Natural Language Program:**

1.  **Identify** all green (3) pixels in the input grid.
2.  **Iterate** through each identified green pixel.
3.  For each green pixel, **check for adjacency:**
    *   Check if there is at least one other green pixels directly above or below it AND another green pixel exists directly to its left or to it's right.
4.  If *both* of the above conditions are true, **change** the pixel's color from green (3) to yellow (4).
5.  All other pixels **retain** their original color.
6.  The output grid has the **same dimensions** as the input grid.

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
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
