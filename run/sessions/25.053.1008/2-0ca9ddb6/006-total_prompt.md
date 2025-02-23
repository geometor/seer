# 2-0ca9ddb6 • 006 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x762C40176A40>

**output:**
```
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 6 0 0
0 0 0 7 0 0 0 0 0
0 0 7 1 7 0 0 0 0
0 0 0 7 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x762C40176470>
Okay, here's my analysis of the provided example, formatted as requested:

**Perception of Elements:**

The task involves a grid of colored pixels. The input grid seems to contain isolated single-pixel objects of various colors. The output grid introduces new colored pixels adjacent to some of the existing pixels, forming crosses or partial crosses. The original pixels seem to remain unchanged. The colors of the new pixels can be different from the original source.

**YAML Documentation:**


```yaml
facts:
  - type: grid
    description: Input and output are 2D grids of colored pixels.
  - object: pixel
    properties:
      - color: integer value (0-9) representing a color.
      - position: row and column index in the grid.
  - observation: input_grid
    description: Contains isolated single-pixel objects.
  - observation: output_grid
    description:  Adds pixels around certain input pixels, forming crosses or partial crosses.
  - relationship: adjacency
    description: New pixels are added adjacent to existing pixels (up, down, left, right).
  - action: add_pixel
    parameters:
      - color: The color of the new pixel.
      - position: The position of the new pixel, relative to an existing pixel.
  - transformation: pattern
    description: The transformation adds pixels in cross shape based on the color of the input pixel
```


**Natural Language Program:**

1.  **Iterate** through each non-white pixel in the input grid.
2.  **Check** color of pixel, for each non-white pixel:
    *   If the pixel is blue (1), add orange (7) pixels to its top, bottom, left, and right.
    *   If the pixel is red (2), add a yellow (4) pixel to top and left
    *   If the pixel is magenta (6), don't add any pixels.
3.  **Preserve** all the original, input pixels in the output grid.
4. If the neighbors are outside the grid, the pixels are not drawn.


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
