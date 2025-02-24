# f2829549 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 7 7 1 5 0 0
0 0 7 1 0 5 5
0 7 0 1 5 5 0
0 0 7 1 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x256 at 0x7BFC47F93310>

**output:**
```
0 0 0
3 0 0
0 0 3
3 3 0
```

<PIL.Image.Image image mode=RGB size=192x256 at 0x7BFC475475B0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves transforming a grid of colored pixels (represented by numbers 0-9) into a smaller grid of colored pixels. The colors in the output grid seem to be derived from specific patterns or objects in the input grid. The input grid appears to contain a vertical line of blue (1) pixels, and various other colored pixels, particularly orange (7) and gray (5). The output grid contains green (3) and white (0) pixels. There's a reduction in dimensions from the input to the output.

**YAML Block - Facts:**


```yaml
facts:
  - observation: Input grid is 4x7 (rows x columns).
  - observation: Output grid is 4x3 (rows x columns).
  - observation: Input grid contains a vertical line of blue (1) pixels in the fourth column.
  - observation: Output grid contains green (3) where the line is not all white.
  - observation: Output colors are only green (3) or white (0)
  - object: Vertical blue line
    properties:
      color: blue (1)
      location: column 4
      length: 4 (extends the full height of the input grid)
  - object: input_grid
    properties:
      dimensions: 4x7
  - object: output_grid
    properties:
     dimensions: 4x3
  - relation: Column of 3 corresponds to blue and white columns of 1 in the input.

```


**Natural Language Program:**

1.  **Identify Key Feature:** Locate the vertical blue (1) line in the input grid.
2.  **Reduce Columns:** Condense each set of columns into 1.
3.  **Determine New Value:**
      *   If an entire column in original is white, it maps to white (0).
      *   If a column to left of blue contains orange or to right contains grey, then it maps green.

Essentially, the program creates the smaller image and fills in the blanks with
white or green.

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
