# 67385a82 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 3 0 0 0 3
0 3 3 3 0 0
0 0 0 0 3 0
0 3 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x256 at 0x7BFC47547A30>

**output:**
```
0 8 0 0 0 3
0 8 8 8 0 0
0 0 0 0 3 0
0 3 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x256 at 0x7BFC47547C70>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a grid of colored pixels, with numerical values representing different colors. The primary colors involved appear to be white (0), green (3), and azure (8). The transformation seems to involve selectively changing some pixels of one color to another, specifically green (3) to azure (8) in some instances. The layout and positions of the green pixels seem to influence which ones get changed.

**YAML Block (Facts):**


```yaml
objects:
  - type: pixel
    properties:
      color:
        - white (0)
        - green (3)
        - azure (8)
      position: [row, column]
actions:
  - type: color_change
    from_color: green (3)
    to_color: azure (8)
    conditions:
        - adjacent green pixels in a line
relationships:
  - adjacency: pixels can be horizontally or vertically adjacent
```


**Natural Language Program:**

1.  **Identify Target Objects:** Locate all pixels with the color green (value 3).
2.  **Check for Horizontal Contiguous Blocks:** For each green pixel, check if it's part of a horizontal contiguous block of green pixels (i.e., has green neighbors to its immediate left or right).
3. **Conditional Color Change:** Change color of pixels identified at the previous stage. If a green pixel is part of the group, change its color to azure (8).

In short the program identifies groups of horizontally adjacent green pixels and changes them to azure.

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
