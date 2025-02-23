# 00d62c1b • 008 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 0 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7B5D7C05FA90>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 4 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7B5D7C05F970>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a grid of pixels, most of which are white (0). There's a distinct shape formed by green (3) pixels. The transformation seems to involve identifying a specific location within the green shape and changing a single pixel at that location to yellow (4). The core challenge is figuring out the rule for selecting *which* green pixel becomes yellow.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    properties:
      - type: 2D array
      - values: integers (0-9) representing colors
  - object: green_shape
    properties:
      - color: green (3)
      - shape: irregular, contiguous
  - object: yellow_pixel
    properties:
      - color: yellow (4)
      - location: within the green_shape
      - uniqueness: only one yellow pixel appears in the output
  - action: change_color
    description: One green pixel within the green shape is changed to yellow.
    parameters:
      - from_color: 3
      - to_color: 4
      - selection_rule:  "center most according to some definition"
  - relationship: yellow pixel is inside or on the border of the green shape
```


**Natural Language Program:**

1.  **Identify the Green Shape:** Locate all pixels with the value 3 (green) that form a contiguous shape.
2.  **Find the Center:** Determine the "center" of the green shape. based on the example:
    + find green pixel at the center of the height of the shape
    + then find the center of those
3.  **Change Color:** Change the color of the center-most green pixel to 4 (yellow).


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
