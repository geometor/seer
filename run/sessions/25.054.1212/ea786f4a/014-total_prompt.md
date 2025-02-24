# ea786f4a • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 0 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7BFC47500F40>

**output:**
```
0 3 3 3 3 3 0
3 0 3 3 3 0 3
3 3 0 3 0 3 3
3 3 3 0 3 3 3
3 3 0 3 0 3 3
3 0 3 3 3 0 3
0 3 3 3 3 3 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7BFC442192D0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, initially mostly green (value 3) with a single white pixel (value 0) in the center. The transformation seems to involve inverting the colors (green to white and white to green) in a specific pattern around the initially white pixel. The pattern appears to be a square or diamond shape centered on the initial white pixel, expanding outwards.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    properties:
      - type: 2D array
      - values: integers (0-9) representing colors
      - initial_state: predominantly green (3), single central white pixel (0)
  - object: pixel
    properties:
      - color: integer value (0-9)
      - location: row, column indices within grid
  - action: color_inversion
    description: swapping color values based on a defined rule
    parameters:
      - original_color: the color to be replaced.
      - replacement_color: The color to replace with.
  - relationship: spatial_pattern
    description: The pattern of color inversion forms a cross shape centered on the initial white pixel.
    properties:
      - shape: cross
      - center: location of the original white pixel

```


**Natural Language Program:**

1.  **Identify the Center:** Locate the single white pixel (value 0) in the input grid. This is the center of the transformation.

2.  **Invert Colors in cross pattern:** all pixels that are the same color as the most frequent color get flipped to 0 if they are the same Manhattan distance in the x or y direction from the center. All instances of 0 are also changed to the most frequent color.

In simpler, high level terms.

1.  Find the initial white cell
2.  Create a cross shape, centered on the white cell.
3.  Cells inside the cross that used to be green are now white.
4. The initial white cell is changed to green.

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
