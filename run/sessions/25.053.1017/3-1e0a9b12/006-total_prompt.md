# 3-1e0a9b12 • 006 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x75C2E5BFE8C0>

**output:**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x75C2E5BFF130>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids (input and output) of the same dimensions (5x5). Each cell in the grid contains a single digit integer representing a color. The transformation seems to involve a selective copy and/or movement of colored pixels, while other pixels are changed to color 0 (white).

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      dimensions: 5x5
      cells: integers (0-9) representing colors

  - type: pixel
    properties:
      color: integer (0-9)
      position: (row, column)

actions:
  - type: move
    properties:
      source: (row, column)
      destination: (row, column)
    conditions:
      - color of source pixel is not 0

  - type: change_color
    properties:
      target: (row, column)
      new_color: integer
    conditions:
      - specific to the transformation logic (to be determined)
      
relationships:
  - spatial: pixels are arranged in a grid, adjacency matters.
  - conditional: movement and color changes depend on certain conditions.
```


**Natural Language Program:**

1.  **Initialization:** Start with the input grid.

2.  **Copy Down:** Iterate through the input grid from top to bottom.
    *   If a pixel is not white (color 0), check downwards in its column. If a non-zero pixel in the column is found, copy/move all continuous non-zero pixels downwards to positions below the last non-zero pixel.

3.  **Whitespace:** All remaining pixels that have not been filled through step 2, change them to white (color 0).

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
