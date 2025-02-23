# 5-150deff5 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0 0 0 0
0 0 5 5 5 5 5 0 0 0 0
0 0 0 5 5 5 0 0 0 0 0
0 0 0 5 5 5 5 5 0 0 0
0 0 0 5 0 0 5 5 0 0 0
0 0 0 0 0 5 5 5 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x75C2E470D9C0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0
0 0 8 8 0 0 0 0 0 0 0
0 0 8 8 2 2 2 0 0 0 0
0 0 0 2 8 8 0 0 0 0 0
0 0 0 2 8 8 8 8 0 0 0
0 0 0 2 0 0 8 8 0 0 0
0 0 0 0 0 2 2 2 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=704x576 at 0x75C2E470DD80>
Okay, here's a breakdown of my observations and proposed transformation rule for the example provided:

**Perception of Task Elements:**

The task involves transforming a grid of colored pixels. The primary element is a recognizable shape formed by connected pixels of a single color (gray - 5) in the input grid. This shape appears to be undergoing a color transformation and possibly a type of "splitting" or "alternating" color fill. The background (white - 0) remains unchanged.

**YAML Block - Facts:**


```yaml
objects:
  - name: shape
    type: contiguous_pixels
    initial_color: gray (5)
    properties:
      - connected: true
      - bounded: true
  - name: background
    type: pixels
    color: white (0)
    properties:
      - static: true

actions:
  - name: color_transform
    target: shape
    type: substitution
    parameters:
      - from: gray (5)
        to:
          - azure (8)
          - red (2)
    rule: alternating_fill

relationships:
   - subject: shape
     relation: contained_within
     object: background
```


**Natural Language Program:**

1.  **Identify the Shape:** Locate the contiguous block of pixels that are not white (0). In the example input, this is the gray (5) shape.
2.  **Alternating Color Fill:** Starting from the top-left pixel of the identified shape, replace the original color (gray) with azure (8).
3.  Apply an alternating pattern - fill.
4. The pattern starts on the topleft most pixel of the object, and alternates horizontally and vertically.
5.  Leave white (0) pixels unchanged.

In essence, the transformation identifies a non-white object within the grid, it performs
an alternating color fill on it, and preserves the background.

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
