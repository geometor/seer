# 1e0a9b12 • 014 • example_3 • investigate_coder

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

<PIL.Image.Image image mode=RGB size=320x320 at 0x7C67C764B880>

**output:**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7C67C764B9D0>
Okay, here's my analysis of the example input-output pair, formatted as a report:

**Perception of Elements:**

The task involves two grids of colored pixels. The colors are represented by integers. Some pixels remain unchanged, while others move or disappear. There appears to be a selective downward movement of colored, non-white (non-zero) pixels. The movement seems to stop when encountering another colored pixel.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      rows: 5
      columns: 5
      cells: integers (0-9 representing colors)
  - type: pixel
    properties:
      color: integer (0-9)
      position: (row, column)

actions:
  - name: move_down
    description: Pixels of certain colors move downwards.
    conditions:
      - color is not 0 (white)
      - The cell below is 0
    constraints:
      - movement stops if a non-zero pixel is encountered

relationships:
  - type: spatial
    description: Pixels are arranged in a 2D grid.
    properties:
      adjacency: vertical and horizontal
```


**Natural Language Program:**

1.  **Identify Movable Pixels:** Find all pixels that are not white (color value 0).
2.  **Iterate:** For each movable pixel, starting from the top row and working downwards:
3.  **Check Below:** Check the pixel directly below the current pixel.
4.  **Move if Empty:** If the cell below is white (0), move the current pixel's color value down to that cell and set the current cell to white (0).
5.  **Stop if Blocked:** If the cell below is not white (not 0), do not move the current pixel.
6. **Repeat**: Continue this downward movement for each movable pixel until the bottom of the grid is reached or movement is blocked by another non-white pixel. The process seems to flow from top to bottom. Pixels at the top seem to have precedence to move over pixels below.

Essentially this is object persistence and gravity impacting movable non white objects.

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
