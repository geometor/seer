# f25ffba3 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 9
0 0 3 9
0 0 3 9
2 0 3 9
2 4 3 9
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC48A62920>

**output:**
```
2 4 3 9
2 0 3 9
0 0 3 9
0 0 3 9
0 0 0 9
0 0 0 9
0 0 3 9
0 0 3 9
2 0 3 9
2 4 3 9
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC48A62B30>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves a grid of colored pixels. The input and output grids have the same dimensions (10x4). There are several distinct colors present: white (0), maroon (9), green (3), red (2), and yellow (4). The most noticeable change is the rearrangement of the rows. A distinct colored object, the vertical line composed by values 3 and 9 on right border seems to stay.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    dimensions: [10, 4]
    colors: [white, maroon, green, red, yellow]
  - type: object
    description: vertical line
    colors: [green, maroon]
    position: right border
  - type: transformation
    description: row permutation
    details: |
      The rows of the input grid are reordered to produce the output grid.
      The vertical line composed by values 3 and 9 seem to indicate the rows permutation order.

```


**Natural Language Program:**

1.  **Identify Key Structure:** Recognize the vertical line of green (3) and maroon (9) pixels on the right edge of the grid.

2.  **Row Reordering:** Extract the rows of input grid by reading it, and reorder the rows based on the vertical line on the right.

3.  **Construct Output:** Copy the bottom five rows from input, and prepend it to itself, reversing order.

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
