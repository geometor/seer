# d037b0a7 • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
4 0 0
0 2 0
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC48908FA0>

**output:**
```
4 0 0
4 2 0
4 2 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7BFC47F93D30>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a 3x3 grid. The input grid contains three non-zero colored pixels: yellow (4) at the top-left, red (2) in the center, and white (0) elsewhere. The output grid duplicates the yellow pixel vertically downwards, filling the first column. The red pixel remains in the center, and also gets duplicated in the cell below. The last column is same as last column in input, all zeros.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    type: 2D array
    dimensions: 3x3
  - object: pixel
    type: element
    property: color (represented by integer value)
  - object: yellow_pixel
    value: 4
    initial_position: [0, 0] # row, column
    action: duplicate_vertically
  - object: red_pixel
    value: 2
    initial_position: [1, 1]
    action: duplicate_once_below
  - object: other_pixels
    value: 0
    initial_position: all others
    action: remain unchanged
```


**Natural Language Program:**

1.  **Identify** the yellow pixel (value 4) in the top-left corner ([0,0]) of the input grid.
2.  **Copy** the yellow pixel to the cells directly below it in the first column ([1,0] and [2,0]).
3.  **Identify** the red pixel (value 2) in the center of the grid ([1,1]).
4. **Copy** the red pixel in the cell directly below ([2,1]).
5.  **Keep** the all the other pixels in the input grid (those with the value of 0) in same positions.

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
