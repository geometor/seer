# beb8660c • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
2 2 0
0 4 0
8 8 8
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC475872E0>

**output:**
```
0 0 4
0 2 2
8 8 8
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC443EC2B0>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a 3x3 grid of colored pixels. The input and output grids have the same dimensions. The colors in the input grid seem to be rearranged in the output grid. The bottom row (azure) remains unchanged. The other colors seem to swap positions, and some of the cells in the other rows of the grid get replaced by white, while some stay the same. It looks like it is a sort of rotation but with some color overwrites.

**YAML Block (Facts):**


```yaml
facts:
  - type: grid
    dimensions: [3, 3]
    description: Input and output grids have identical dimensions.
  - type: object
    attribute: color
    values: [red, yellow, azure, white]
    description: Pixels in the grids can have one of four colors.
  - type: observation
    description: The bottom row (azure pixels) remains unchanged between input and output.
  - type: transformation
    description: Colors in the top two rows are rearranged. Specifically yellow and red switch, with some being replaced with white.
  - type: action
    name: rotation or partial rotation
    description: It looks like we take the center 2x2 and rotate it clockwise, then overwrite top left corner with background.

```


**Natural Language Program:**

1.  **Identify the Bottom Row:** Leave it unchanged.
2.  **Isolate**: Consider the other positions of the 3x3 grid.
3. **Swap and Overwrite**: Rotate colors clock wise one step (90 degrees) in the 2x2 sub-grid defined by the center. Overwrite the cell that now contains what use to be the top-left of the input with the background color (white or `0`).

In summary, leaving the bottom row unchanged, rotate the 2x2 top-right sub-grid defined by center pixel, one step clockwise, and replace cell with the color that used to be in top-left with background color (white/0).

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
