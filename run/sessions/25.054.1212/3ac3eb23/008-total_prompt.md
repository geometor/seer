# 3ac3eb23 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 4 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x384 at 0x7BFC4423DCF0>

**output:**
```
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=448x384 at 0x7BFC4423F730>
Okay, here's my analysis of the example input-output pair, presented as a report:

**Perception of Elements:**

The task involves 2D grids (likely representing images) where each cell contains a single digit (0-9), representing a color. The primary colors involved seem to be white (0) and yellow (4). The input grid contains a single yellow pixel, while the output grid contains a pattern of yellow pixels arranged in vertical and horizontal lines.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      - dimensions: [rows, columns]
        values: [6, 7]
      - cells: pixels
        properties:
          - color: integer (0-9)
  - type: pixel
    properties:
      - color: integer (0-9)
      - location: [row, column]
  - type: line # derived object
    properties:
      - orientation: [vertical, horizontal]
      - color: yellow (4)
      - origin: [row, column] # Starting pixel of the line
      - length: integer

actions:
 - draw_line:
    input:
      - grid
      - origin_pixel
      - orientation
      - length
    output:
      - modified_grid

relationships:
  - input_grid: contains a single yellow pixel
  - output_grid: contains vertical and horizontal lines of yellow pixels
  - lines_origin: location of the original yellow pixel in the input_grid.

```


**Natural Language Program:**

1.  **Identify the Seed:** Locate the single yellow (4) pixel in the input grid. This pixel's location serves as the origin.

2.  **Vertical Line:** Create a vertical line of yellow (4) pixels, extending upwards and downwards from the origin. The line should extend to reach the edges of the input grid.

3.  **Horizontal Line:** Create a horizontal line of yellow (4) pixels, extending leftwards and rightwards from the origin, extending all the way to reach the edges of the grid.

In essence, the transformation creates a cross-shaped pattern of yellow pixels, centered on the location of the initial yellow pixel in the input grid. The lines of the cross extend to the boundaries of the grid.

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
