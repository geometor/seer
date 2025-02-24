# a3df8b1e • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
1 0
```

<PIL.Image.Image image mode=RGB size=128x640 at 0x7BFC4890A0E0>

**output:**
```
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
```

<PIL.Image.Image image mode=RGB size=128x640 at 0x7BFC475876A0>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a transformation of a 2D grid of pixels, where each pixel has a color value represented by an integer (0 or 1 in this case). The input grid appears to have a single blue pixel (1) at the bottom left corner, with the rest being white (0). The output grid has the same dimensions but exhibits a checkerboard pattern of alternating white (0) and blue (1) pixels. The bottom left pixel is blue in the input and the pixel to its right is blue in the output.

**YAML Block (Facts):**


```yaml
facts:
  - object: grid
    type: 2D array
    properties:
      - width: 2
      - height: 10
      - cell_values: [0, 1]  # white, blue
  - observation: input_grid_has_single_blue_pixel_at_bottom_left
  - observation: output_grid_has_checkerboard_pattern
  - relationship: output_pattern_alternates_starting_from_top_left_0
  - action: replace input with checkboard pattern
```


**Natural Language Program:**

1.  **Initialization:** Start with the given input grid dimensions (10x2).

2.  **Checkerboard Pattern:** Create a new grid of the same size. Fill the output grid with a checkerboard pattern. Iterate through each cell of the output grid, alternating between white (0) and blue (1) pixels.
    The top-left pixel (0,0) will be 0. The coordinate to its right, (0,1) will be 1.
    For all other pixels, the color value will be the inverse of the pixel above it.

In essence, the program replaces the whole input grid by alternating colors, with the top-left pixel as 0, and other pixels on the same row alternating, and next row starting with the inverse of the element at the start of the previous row.

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
