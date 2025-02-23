# 25d8a9c8 • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
2 2 4
2 2 4
1 1 1
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC48A62B30>

**output:**
```
0 0 0
0 0 0
5 5 5
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC48A61AE0>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a 3x3 grid. The input grid has colors in each cell, represented by single-digit integers.  The output grid appears to be a modified version of the input grid, with some colors changed. The bottom row seems to be of particular significance, as all elements change from input to output based on properties of the input.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    dimensions: 3x3
    cells:
      - properties:
          value: integer (0-9)
          color: mapped from value
          location: row, column coordinates

observations:
  - input_bottom_row:
      values: [1, 1, 1]
      color: blue
  - output_bottom_row:
    values: [5,5,5]
    color: grey
  - input_other_rows:
    values_row_1: [2,2,4]
    values_row_2: [2,2,4]
    colors: [red, red, yellow]

actions:
    - bottom_row_change_to_grey: all values in the bottom row are replaced by 5 (gray) if they are all the same color and value
    - other_rows_change_to_white: all values in other row are replaced by 0 (white)

relationships:
  - bottom_row_input_output: The change in the bottom row's color appears to relate to bottom row of the input and is a different color from input.
  - other_row_input_output: the change from red/yellow to all white appears to be a consistent operation.

```


**Natural Language Program:**

1.  **Examine the bottom row of the input grid.**
    *   If all cells in the bottom row of the input have the same value (and therefore, color)
2.  **Modify the Bottom Row.** Set all values in the output grid's bottom row to the value 5 (gray).
3.  **Modify all other rows.** Set all the values in all other rows of the output grid to 0 (white)

In summary, the transformation detects if the entire bottom row of input is of the same color, it changes bottom row of the output grid all to grey, and the other rows all to white.

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
