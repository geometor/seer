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

<PIL.Image.Image image mode=RGB size=576x576 at 0x75C2E517C2E0>

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x75C2E517E590>
Okay, here's my analysis of the provided example, focusing on perception, object documentation, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a grid of pixels, each represented by a single digit (0-9), corresponding to different colors. The input grid appears to be transformed into the output grid by adding new colored pixels around existing non-zero pixels. The added pixels seem to form a sort of "halo" or "border" around the original pixels. The colors of the added pixels depend on the color of the adjacent filled pixel.

**YAML Documentation of Facts:**


```yaml
objects:
  - name: grid
    type: 2D array
    properties:
      - width: 9
      - height: 9
      - cells: pixels (integers 0-9)

  - name: pixel
    type: cell
    properties:
      - color: integer (0-9)
      - position: (row, column)

actions:
  - name: add_border
    description: Adds pixels of a specific color around existing non-zero pixels.
    parameters:
      - color_map: mapping of input pixel color to border pixel color and position

relationships:
  - adjacency: Pixels can be adjacent horizontally, vertically, or diagonally.
  - border: Added pixels form a border around original non-zero pixels.

color_mapping:
    input_output:
        '1': ['7',[(1,0),(0,1),(-1,0),(0,-1)]] # relative positions
        '2': ['4',[(1,0),(-1,0)]]
        '6': ['7',[(-1,0)]]
```


**Natural Language Program:**

1.  **Iterate** through each cell (pixel) in the input grid.
2.  **Identify** "seed" pixels: If a pixel has a non-zero value, consider it a "seed" pixel.
3.  For each seed pixel determine a set of "border" positions relative to it.
4.  For each seed pixel and relative position pair:
    *   Check if calculated border position is within the bounds of the grid.
    *   Check the "seed" pixel's color, and determine the border color from a fixed mapping.
    *   Check the input and get border pixel color from color mapping.
    *   Set the border pixel in the output grid to the determined border color.
5.  **Copy** seed pixel to same location in output.
6.  Pixels that are not seeds or borders are 0 (white) in the output.

Essentially, the transformation adds a colored border around each non-zero pixel in the input grid. The color of the border pixels, and the relative positions, depends on the color of the original, central pixel.

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
