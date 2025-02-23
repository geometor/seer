# 3-1e0a9b12 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7C3262DFF0A0>

**output:**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7C3262DFF370>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a 4x4 grid of single-digit integers (representing colors) to another 4x4 grid. The most obvious change is the rearrangement of non-zero elements. Some zero-value cells remain zero, while others become non-zero. The positions of the original non-zero values seem to be key.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    dimensions: 4x4
    elements: integers (0-9)
    description: Represents a 2D array of colored pixels.
  - type: cell
    properties:
      value: integer (0-9)
      row: integer (0-3)
      column: integer (0-3)
      is_non_zero: boolean

actions:
  - name: rearrange
    description: Moves non-zero cells to different positions within the grid.
  - name: shift_down
    description: moves a set of values down some number of rows
  - name: shift_right
    description: moves a set of values right some number of columns

relationships:
  - type: spatial
    description: Cells are arranged in rows and columns within the grid.
  - type: transformation
    description: The input grid is transformed into the output grid by rearranging cells.

```


**Natural Language Program:**

1.  **Identify Non-zero Cells:** Locate all cells in the input grid with values other than 0.
2.  **Record Values and original positions** Store the set of values for each non zero cell.
3.  **Move Non-zero Cells:** Move the non zero cells, as a set, down one row, wrapping to the first row.
4. **Move Non-zero Cells:** Move the non zero cells, as a set, right one column, wrapping to the first column.
5. **Zero out all rows except the bottom row.** Set all cells in rows other than the last row to 0.
6.  **Fill Bottom Row:** Place the ordered sequence of original non-zero values, from left to right, into the bottom row, from left to right, skipping 0 values.

In short: The non-zero values are extracted, and then placed on the bottom row, while everything else is zeroed out. The non-zero cells move down by 1, and right by 1. The extracted values are then put into the bottom row in their original order.

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
