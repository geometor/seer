# d037b0a7 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 2 0
7 0 8
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC4890A3B0>

**output:**
```
0 2 0
7 2 8
7 2 8
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC4890A380>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves transforming a 3x3 grid of colored pixels (represented by numbers 0-9) into another 3x3 grid. The input grid contains four distinct colors (represented by 0, 2, 7, and 8), while the output grid maintains the same color and shape. The output grid is a copy of input grid, however any '0' are replaced with the color immediately to their right, or left.

**YAML Fact Block:**


```yaml
facts:
  - type: grid
    dimensions: [3, 3]
    description: Input and output grids are 3x3 matrices.
  - type: cell
    values: [0, 2, 7, 8]
    description: Cells can have values representing different colors.
    color_map: {0: white, 2: red, 7: orange, 8: azure}
  - type: object
    attribute: color
    description: Contiguous blocks of single color can be considered objects.
  - type: transformation
    description: 'replace any 0 by value to its left or right. '
  - type: relationship
    description: Zeros that are transformed are adjacent to the non-zero color.
```


**Natural Language Program:**

1.  **Iterate** through each cell of the input grid.
2.  **Identify** all '0' (white) color cells.
3. If cell is color 0, check the color to its right and to its left, replace by that value.


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
