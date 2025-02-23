# f35d900a • 014 • example_3 • investigate_coder

---

## Example 3

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 4 0 0 0 0 0 0 0 0 0 0 2 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1024x1088 at 0x70FFF4DAB880>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 4 4 4 0 0 0 0 0 0 0 0 2 2 2 0
0 4 2 4 5 0 5 0 0 5 0 5 2 4 2 0
0 4 4 4 0 0 0 0 0 0 0 0 2 2 2 0
0 0 5 0 0 0 0 0 0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 5 0 0 0 0 0 0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 5 0 0 0 0 0 0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 5 0 0 0 0 0 0 0 0 0 0 5 0 0
0 2 2 2 0 0 0 0 0 0 0 0 4 4 4 0
0 2 4 2 5 0 5 0 0 5 0 5 4 2 4 0
0 2 2 2 0 0 0 0 0 0 0 0 4 4 4 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1024x1088 at 0x70FFF01B3FA0>
Okay, here's my analysis of the provided example, focusing on perception, documented facts, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a grid of pixels, initially mostly white (0) with a few colored pixels (red=2, yellow=4). The transformation seems to involve creating a symmetrical pattern, expanding, and introducing a new color (gray=5). The output grid mirrors the layout and colors of the input grid, but introduces a gray color where a colored pixel is adjacent to another colored pixel. The main challenge is to identify adjacency and color replacement rule.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    description: 2D array of pixels
    properties:
      - width: 16
      - height: 17
      - cells: integers (0-9) representing colors

  - type: pixel
    description: individual cell in the grid
    properties:
      - color: integer value (0=white, 2=red, 4=yellow, 5=gray)
      - position: (row, column) coordinates

actions:
  - type: mirroring
    description: The relative position of the original colored pixels is preserved, with the original input mirrored in output.
  - type: expansion
    description: Expanding the colored pixels to their adjacent.
  - type: replacement
    description: Replacing white pixels with gray based on adjacency to colored pixels
    parameters:
      - original_color: 0 (white)
      - new_color: 5 (gray)
      - condition: adjacent to two differently colored pixels

relationships:
  - adjacency: pixels sharing a side (not diagonal)
  - symmetry: pattern is mirrored across a vertical and horizontal center axes.

```


**Natural Language Program:**

1.  **Mirroring and Initial Expansion**: Copy each non-white pixel from the input to the output, then "expand" the colors.
    *   Expand red (2) to all directly adjacent white pixels.
    *   Expand yellow (4) to all directly adjacent white pixels.
    *   Mirror the initial colored pixels positions across a vertical and a horizontal axis.

2.  **Adjacency Check and Gray Fill**: For each white (0) pixel in the *output* grid:
    *   Check if it is adjacent to at least one non-white pixel.
    *   Check if the adjacent non-white pixels contain at least two different colors.
    *   If *both conditions are true*, replace the white pixel with gray (5). Otherwise, keep the current value of the pixel.
3. If the cell is not white and has not been changed to gray, maintain its input color in the output grid.

Essentially, the transformation preserves the initial colored cells positions, expands them and adds gray color where different colors are adjacent.

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
