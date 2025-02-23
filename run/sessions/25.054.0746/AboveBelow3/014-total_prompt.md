# AboveBelow3 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 4 4 0 0 0
0 0 0 0 0 0 0
0 0 1 1 0 0 0
0 0 1 1 0 0 0
0 4 4 4 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7995F9038A00>

**output:**
```
0 0 0 0 0 0 0
0 0 4 4 0 0 0
0 0 1 1 0 0 0
0 0 1 1 0 0 0
0 4 4 4 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x448 at 0x7995F7B9A860>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a grid of colored pixels. The colors present are white (0), yellow (4), and blue (1).  The primary observation is a shift in the position of a colored object, or multiple colored objects. Specifically, a yellow object at the top, and blue square in the middle.

**YAML Block (Facts):**


```yaml
objects:
  - type: rectangle
    color: yellow
    initial_position: row 1, columns 3-4
    final_position: row 2, columns 3-4
    size: 1x2
  - type: square
    color: blue
    initial_position: rows 3-4, columns 3-4
    final_position: rows 3-4, columns 3-4
    size: 2x2
  - type: rectangle
    color: yellow
    initial_position: row 5, columns 2-4
    final_position: row 5, column 2-4
    size: 1x3

actions:
  - type: vertical_shift
    object: yellow rectangle
    direction: down
    magnitude: 1

relationships:
  - type: adjacent
    objects: [yellow rectangle, blue square, yellow_rectangle2]
  - type: static # blue square don't change
    object: blue square
```


**Natural Language Program:**

1.  **Identify Objects:** Locate the three distinct objects:
    *   A 1x2 yellow rectangle on the top.
    *   A 2x2 blue square in the center.
    *   A 1x3 yellow object in the bottom.
2.  **Move First Object:** Shift the top 1x2 yellow rectangle down by one row.
3.  **Preserve Static Object:** Preserve blue square as static,
4.  **Preserve Second Object:** preserve second yellow object

Essentially, the transformation involves moving the yellow rectangle at the top, one position downwards, keeping the rest.

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
