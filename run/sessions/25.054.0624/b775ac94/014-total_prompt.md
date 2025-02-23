# b775ac94 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 8 8 0 0 0 0 0
0 0 0 0 0 0 0 8 8 0 0 0 0 0
0 0 0 0 0 0 0 0 0 8 4 0 0 0
0 0 0 0 0 0 0 0 0 0 6 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 2 4 0 0 0 0 0 0 0 0
0 2 2 2 2 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x896 at 0x70FFF0ECDB70>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 8 8 0 0 4 4 0
0 0 0 0 0 0 0 8 8 0 0 4 4 0
0 0 0 0 0 0 0 0 0 8 4 0 0 0
0 0 0 0 0 0 0 0 0 0 6 0 0 0
0 0 0 0 0 0 1 0 0 0 0 6 6 0
0 0 0 0 0 1 1 1 1 0 0 6 6 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 2 4 0 0 0 0 0 0 0 0
0 2 2 2 2 4 4 4 4 0 0 0 0 0
0 0 0 2 0 0 4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x896 at 0x70FFF0F9D4E0>
Okay, here's my analysis of the provided input-output example:

**Perception of Elements:**

The task involves 2D grids containing colored pixels. The transformation seems to involve a combination of object duplication and shifting/expansion. Specifically, colored objects in the input grid appear to be replicated and, in some cases, expanded horizontally in the output grid. The background (white, represented by '0') remains unchanged.

**YAML Block (Facts):**


```yaml
objects:
  - type: colored_region
    attributes:
      - color: varies (blue, red, green, yellow, gray, magenta, orange, azure, maroon)
      - shape: contiguous block of pixels of the same color
      - size: varies
      - position: (row, column) coordinates

actions:
  - type: duplication
    description: Create a copy of an object.
  - type: horizontal_expansion
    description: Extend the object to the right, potentially doubling its width.
  - type: shift
    description: Move yellow and azure object

relationships:
  - input_object: original object in the input grid
  - output_object: corresponding (possibly modified) object in the output grid
  - spatial: relative positions of objects within the grid (above, below, next to)
```


**Natural Language Program:**

1.  **Identify Objects:** Locate all contiguous colored regions (objects) within the input grid.
2.  **Process Each Object:** For each identified object:
    *   **Yellow Object.** Shift right.
        *   If the yellow object is one cell. Do not expand.
        *   If the object's shape is an L shape. Expand the width of the top of the L and the bottom of the L by one to the right.
    *   **Azure object.** Shift the object to the right.
    *   **Other color Objects:** Duplicate the object.
        *   The new, duplicated object will retain its same color.
        *    Expand to the right, doubling the width.

3.  **Background:** The white background (value 0) remains unchanged throughout the transformation.

Essentially, duplicate most of the colored objects by expanding them to the right. The blue and yellow objects only shift one cell to the right.

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
