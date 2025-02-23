# AboveBelow4 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 2 2 2 0 0 2 2 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7995F9038A00>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 4 2 2 0 0 4 2 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 4 2 2 0 0 0
4 4 4 4 4 4 4 4 4 4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 2 4 0 0 0 0 0 0
0 0 0 0 2 2 4 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7995F90382E0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The input grid contains horizontal and vertical stripes of red (2) and yellow (4) pixels against a background of white (0) pixels. The transformation appears to involve a selective replacement of some red pixels with yellow pixels, specifically at the intersections of the red stripes and the existing yellow stripe.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 10x10
      cell_values: [0, 2, 4]  # white, red, yellow
  - type: stripe
    properties:
      orientation: [horizontal, vertical]
      color: [red, yellow]
      contiguous: true
relationships:
  - type: intersection
    properties:
      objects: [red stripe, yellow stripe]
      result: color change (red to yellow)
actions:
  - type: replacement
    properties:
      source: red pixel at intersection
      target: yellow pixel
```


**Natural Language Program:**

1.  **Identify Stripes:** Locate all horizontal and vertical stripes of red (2) and yellow (4) pixels. A stripe is defined as a contiguous sequence of pixels of the same color along a row or column.
2.  **Find Intersections:** Determine the points (pixels) where the red stripes intersect the yellow stripe. An intersection occurs where a red pixel in a red stripe is in the same row or column as a section of the horizontal yellow stripe.
3.  **Color Replacement:** At each intersection point identified in step 2, change the color of the pixel from red (2) to yellow (4).
4. **Preserve other:** All other pixels should not be changed.

Essentially, the program overlays the red horizontal and vertical stripes. Where the red and yellow overlap, the pixel becomes/remains yellow.

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
