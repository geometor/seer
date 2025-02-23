# 2-0ca9ddb6 • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7745EA796BC0>

**output:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7745EA797FA0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids have the same dimensions (9x9 in this example). The grids contain single-digit integers (0-9), representing different colors. The primary colors present are white (0), red (2), blue (1), yellow (4) and orange (7). The transformation seems to involve the creation of new colored objects around existing colored objects, possibly based on some kind of "influence" or "expansion" rule.

**YAML Block - Facts:**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 9x9
      elements: integers (0-9)

  - type: pixel
    properties:
      color:
        mapping:
          0: white
          1: blue
          2: red
          4: yellow
          7: orange
      position: (row, column)

actions:
  - name: expand
    description: Create new pixels around existing pixels of a specific color.
    parameters:
      source_color: The color of the pixel to expand from.
      target_color: The color of the new pixels to create.
      shape: the relative coordinates to place the new color

relationships:
  - type: adjacency
    description: Pixels are considered adjacent if they share a side (not diagonally).
```


**Natural Language Program:**

1.  **Identify** the red (2) and blue (1) pixels in the input grid.
2.  **Expand** from the red pixel:
    *   Create yellow (4) pixels above and below the red pixel.
3.  **Expand** from the blue pixel:
    *   Create orange (7) pixels above, below, to the left and to the right of the blue pixel.

In essence: Each colored object creates a cross shape of another color on the board. The Red object makes vertical connections while the blue makes horizontal and vertical.

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
