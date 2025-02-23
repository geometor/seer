# 2-0ca9ddb6 • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7C6B13C46980>

**output:**
```
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 7 0 0 0 0 0
0 0 7 1 7 0 0 0 0
0 0 0 7 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7C6B13C28E80>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, each with a numerical value representing a color. The input grid transforms into a modified output grid. The transformation seems to involve adding new colored pixels around existing pixels, based on certain rules. The key seems to be the introduction of '4' (yellow) and '7' (orange) pixels adjacent to existing colored pixels, in specific patterns. There is also a concept of extending.

**YAML Fact Documentation:**


```yaml
facts:
  - type: grid
    description: Input and output are 2D grids of pixels.
    properties:
      - pixels have numerical values representing colors.
      - grid dimensions can vary.
  - type: object
    description: Colored pixels (non-zero values) can be considered objects.
  - type: action
    description: Extending. Adding pixels of a specific color adjacent to existing objects.
    properties:
      -  color 1 (blue) adds '7' (orange) on left, right, and below.
      -  color 2 (red) adds '4'(yellow) above and below and to either side.
      - color 6(magenta) doesn't seem to initiate any additions.
  - type: constraint
    description: The extension happens only once
```


**Natural Language Program:**

1.  **Identify Objects:** Locate all pixels in the input grid that have a non-zero value (i.e., are not white/0). Consider each of these colored pixels as an individual object.

2.  **Conditional Extension:**
    *   If an object is blue (1), add orange (7) pixels to its immediate left, right, and below, if those positions are currently white (0).
    *   If an object is red (2), add yellow (4) pixels to its immediate top, and to the left and the right if those positions are currently white (0).
    *   If the object is magenta(6), do nothing

3.  The rest of the white(0) cells stay white(0)


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
