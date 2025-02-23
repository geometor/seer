# 00d62c1b • 018 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 3 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 3 3 0 3 3 0 3 0 0
3 0 0 3 0 0 3 0 3 0
0 0 0 3 0 0 3 3 0 0
0 0 0 3 0 0 3 0 0 0
0 0 0 3 0 0 3 0 0 0
0 0 0 0 3 3 0 3 0 0
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FA38657820>

**output:**
```
0 0 0 0 0 3 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 3 3 0 3 3 0 3 0 0
3 0 0 3 4 4 3 4 3 0
0 0 0 3 4 4 3 3 0 0
0 0 0 3 4 4 3 0 0 0
0 0 0 3 4 4 3 0 0 0
0 0 0 0 3 3 0 3 0 0
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x70FA386F29B0>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a grid of pixels, each represented by a single digit integer (0-9). The primary colors observed are white (0), green (3), and yellow (4).  The transformation seems to involve identifying a specific object within the input grid and modifying a subset of its pixels based on their color.

**YAML Block (Facts):**


```yaml
objects:
  - name: grid
    type: 2D array
    elements: pixels
    properties:
      - height: 10
      - width: 10
      - color_values: [0, 3, 4]

  - name: green_object
    type: contiguous_block
    properties:
      - color: 3
      - shape: irregular
      - description: >
         The object looks like the number 8 written on the grid.

actions:
  - name: identify_object
    description: Locate the green (3) object within the grid.

  - name: modify_pixels
    description: Change the color of interior pixels of the object
    details: >
      Change color of pixels inside the object, from green(3) to yellow(4) if
      they are inside the largest green object.

relationships:
  - type: containment
    subject: grid
    object: green_object
    description: The grid contains the green object.
  - type: color_change
    subject: Interior green pixels
    object: yellow
    description: internal pixels of the green object change to yellow, others remain.
```


**Natural Language Program:**

1.  **Identify the Target Object:** Locate the largest contiguous block of green (3) pixels within the input grid. This forms the primary object.

2.  **Identify inside pixels.** A pixel is considered to be on the inside of the
    object if is it part of a contiguous block of green pixels and is fully
    surrounded horizontally and vertically by other green pixels from the
    object.

3.  **Modify Pixel Colors:** Traverse the identified interior green pixels. Change the color
    of the pixel from green (3) to yellow (4).

4. **Leave other pixels unchanged.** All pixels which are not inside of the
   main green object remain unchanged.

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
