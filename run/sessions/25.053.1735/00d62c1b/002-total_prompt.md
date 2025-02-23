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

<PIL.Image.Image image mode=RGB size=384x384 at 0x7B5D7C05FA90>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7B5D7C05F6D0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a 2D grid of numerical values, representing colored pixels. The primary colors involved are white (0) and green (3). The transformation seems to involve a specific interaction between adjacent green pixels, resulting in the introduction of yellow (4) pixels. The overall grid dimensions remain constant. The transformation appears local, focused on immediate neighborhoods.

**YAML Block (Facts):**


```yaml
objects:
  - type: pixel
    properties:
      color:
        - white (0)
        - green (3)
        - yellow (4)
      position: [row, column]
  - type: grid
    properties:
      dimensions: [height, width]
      cells: list of pixels

actions:
  - type: color_change
    conditions:
      - adjacent green pixels (horizontally or vertically)
    result:
      - introduction of yellow pixel between green pixels

relationships:
  - adjacency: pixels can be adjacent horizontally or vertically
```


**Natural Language Program:**

1.  **Identify** all green (3) pixels within the input grid.
2.  **Iterate** through each green pixel.
3.  For each green pixel, **check** for adjacent green pixels in the four cardinal directions (up, down, left, right).
4.  If two green pixels are adjacent, **change** to the color of the pixel in output from green (3) to yellow (4).
5. **Maintain** all the other pixels as is.
6.  The output grid has the **same dimensions** as the input grid.

Essentially the core concept is: any green pixel that horizontally or vertically borders another green pixel is turned to a yellow pixel.

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
