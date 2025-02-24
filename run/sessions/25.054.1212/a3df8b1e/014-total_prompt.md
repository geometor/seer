# a3df8b1e • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC4890A0E0>

**output:**
```
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x640 at 0x7BFC4890A380>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a transformation of a 2D grid of pixels. The primary colors involved are white (0) and blue (1). The input grid appears mostly white, with a single blue pixel in the bottom-left corner. The output grid is also mostly white but contains a cross-shaped pattern of blue pixels. The location of the single blue pixel in the input seems to determine the center of the cross in the output.

**YAML Block - Facts:**


```yaml
objects:
  - name: input_grid
    type: 2D array
    properties:
      - colors: [white, blue]
      - size: 10x4
  - name: output_grid
    type: 2D array
    properties:
      - colors: [white, blue]
      - size: 10x4
  - name: blue_pixel
    type: object
    properties:
      - color: blue
      - location: [row_index, column_index] # in input_grid

actions:
  - name: find_blue_pixel
    description: Locate the single blue pixel in the input grid.
  - name: create_cross
    description: Generate a cross pattern of blue pixels in the output grid.
    parameters:
      - center_row: row index of the blue pixel in the input grid
      - center_col: column index of the blue pixel in the input grid

relationships:
  - input_grid.blue_pixel.location determines output_grid.cross.center
```


**Natural Language Program:**

1. **Find the Blue Pixel:** Scan the input grid to find the location (row and column) of the single blue (1) pixel.
2. **Center the Cross:**  Use the row and column of the blue pixel found in step 1 as the center coordinates for a cross pattern in the output grid.
3. **Create the Cross:** In the output grid, change the color of the pixels in the same row and column as the located blue pixel to blue(1), forming a cross. All other pixels should remain white(0).

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
