# 00d62c1b • 026 • example_4 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 3 0 0 0 0
0 0 3 0 0 3 0 0 0 0
0 0 3 0 0 3 0 3 0 0
0 0 3 3 3 3 3 3 3 0
0 0 0 3 0 0 0 0 3 0
0 0 0 3 0 0 0 3 3 0
0 0 0 3 3 0 0 3 0 3
0 0 0 3 0 3 0 0 3 0
0 0 0 0 3 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x74153085B970>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 3 3 3 0 0 0 0
0 0 3 4 4 3 0 0 0 0
0 0 3 4 4 3 0 3 0 0
0 0 3 3 3 3 3 3 3 0
0 0 0 3 0 0 0 0 3 0
0 0 0 3 0 0 0 3 3 0
0 0 0 3 3 0 0 3 4 3
0 0 0 3 4 3 0 0 3 0
0 0 0 0 3 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7415308FA950>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, each with a numerical value representing a color. The primary colors observed are white (0) and green (3). There's a transformation where some green (3) pixels in the input become yellow (4) in the output. The transformation seems to be localized and specific to certain green pixels. It does not appear to follow simple global operations like color replacement or rotations.

**YAML Fact Block:**


```yaml
objects:
  - type: grid
    description: 2D array of pixels
    properties:
      - height: 10
      - width: 10
      - cells: pixels with color values
  - type: pixel
    properties:
      - color: integer value (0-9)
      - position: (row, column)
  - type: shape
    description: contiguous area of pixels of the same color.

actions:
    - name: color_change
      agent: pixel
      precondition:
          - color: 3 # green
      postcondition:
          - color: 4 or 3 #yellow or green
      parameters:
          - position: (row,column)

relationships:
  - type: adjacency
    description: pixels sharing an edge or corner.
  - type: containment
    description: one object is contained within grid
```


**Natural Language Program:**

1.  **Identify Target Pixels:** Examine the input grid. The transformation focuses on green (3) pixels.
2.  **Apply Transformation Rule:** Within a contiguous shape of green, find interior green pixels, defined as:
    - Surrounded on 4 sides (up, down, left, right) by green pixels.
3. Change these interior pixels to yellow (4).
4.  **Output:** Create the output grid with the modified pixels.

In summary. The program identifies contiguous green area. In that area, the most "interior" green pixels (i.e. surrounded by green pixels up, down, left, right) is recolored to yellow.

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
