# 94f9d214 • 020 • example_4 • investigate_coder

---

## Example 4

**input:**
```
3 3 3 3
3 0 0 0
3 0 3 3
3 3 0 3
1 1 1 0
0 1 1 1
1 0 1 1
0 1 1 1
```

<PIL.Image.Image image mode=RGB size=256x512 at 0x7BFC4890B7F0>

**output:**
```
0 0 0 0
0 0 0 0
0 2 0 0
0 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7BFC4890A950>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. The input grid contains two distinct subgrids separated by a few rows. The first subgrid has digits `3` and `0`, while the second one is comprised of digits `1` and `0`. The output grid contains only `0`s, with a single `2` in it. The output grid is the same size as the first sub-grid from the input. The position of the `2` in output grid somehow corresponds with position of non-zero and zero values in the input grids.

**YAML Fact Block:**


```yaml
facts:
  - object: input_grid
    properties:
      type: 2D array
      values: [0, 1, 3]
      sections:
          - top_left: [0,0]
            top_right: [0,3]
            bottom_left: [3,0]
            bottom_right: [3,3]
            values: [0,3]
          - top_left: [4,0]
            top_right: [4,3]
            bottom_left: [7,0]
            bottom_right: [7,3]
            values: [0,1]

  - object: output_grid
    properties:
      type: 2D array
      values: [0, 2]
      size: matches input_grid top section dimensions

  - observation: single_non_zero_output
    description: The output grid contains only one non-zero value (2).

  - observation: input has two segments
    description: top segment is 4x4, bottom segment starts on row 5 and is also 4x4

  - relationship: output_size_matches_input_section1
    description: The dimensions of the output grid are the same as the dimensions of first section of the input grid.

  - relationship: non_zero_position_relates
    description: position of the `2` is related to a `0` in first section of input that has `3`s surrounding it and a corresponding `1` in that location in the second input section
```


**Natural Language Program:**

1.  **Identify Input Sections:** Divide the input grid into two sections. The first section goes from the top of the grid until the last row that starts with a non-zero and non-one number. In the provided data this is row index `0` to `3`. The next section starts from first row that begins with either `0` or `1` until the end of the grid.
2.  **Determine Output Size:** The output grid has the same dimensions as the first identified section of the input.
3. **Locate Critical Input Cell** Find the `0` in first section of input grid which is surrounded by most `3`'s, including diagonals.
4.  **Check Corresponding Cell in Second Section**: Check value in second section of input with same coordinates as `0` identified in previous step. If this value is `1`, this is location of non-zero value `2` for the output grid.
5.  **Create Output Grid:** Initialize an output grid of the determined size, filled with 0s.
6. **Find matching coordinate** Find the coordinates in input grid top section where value is `0` AND surrounded by maximum number of `3` AND the same coordinates in bottom section contains a `1`.
7.  **Populate Output:** Place a `2` in the output grid at the coordinates of `0` found in previous step. All other cells in the output grid remain 0.

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
