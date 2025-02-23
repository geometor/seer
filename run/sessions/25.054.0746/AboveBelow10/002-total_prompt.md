# AboveBelow10 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0 0 0 0 0 0
0 4 0 0 0 0 0 0 0 0 0 0 0 0
0 0 4 0 0 0 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0 0 0 0 0 0 0
0 0 0 0 0 4 0 0 0 0 0 0 0 0
0 0 0 0 0 0 4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 4 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x704 at 0x7995F85D0370>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0 0 0 0 0 0
4 4 0 0 0 0 0 0 0 0 0 0 0 0
4 4 4 0 0 0 0 0 0 0 0 0 0 0
4 4 4 4 0 0 0 0 0 0 0 0 0 0
4 4 4 4 4 0 0 0 0 0 0 0 0 0
4 4 4 4 4 4 0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=896x704 at 0x7995F85D0E80>
Okay, here's my analysis of the example input-output pair, structured as requested:

**Perception of Elements:**

The task involves a grid of pixels, initially mostly white (0) with a diagonal line of yellow (4) pixels extending from the top-left to the bottom-right. The transformation appears to involve "filling in" the area below this diagonal line with yellow (4) pixels, creating a triangular region of yellow. The boundary seems to be the original diagonal line of yellow pixels.

**YAML Block (Facts):**


```yaml
objects:
  - name: grid
    type: 2D array
    description: A grid of pixels represented by numerical values.
  - name: pixel
    type: integer
    description: Represents a color, with 0 being white and 4 being yellow.
  - name: diagonal_line
    type: object
    description: A sequence of yellow (4) pixels running diagonally from top-left to bottom-right.
  - name: yellow_triangle
    type: region
    description: the area bounded by x=0, y=2 and the yellow diagonal.

properties:
  - name: color
    type: attribute
    values: {0: white, 4: yellow}
  - name: position
    type: attribute
    description: Row and column index within the grid.

actions:
  - name: fill
    description: Change the color of pixels within a defined region.

relationships:
  - name: below
    description: Spatial relationship indicating pixels located at lower row indices than a reference object (the diagonal line).
```


**Natural Language Program:**

1.  **Identify the diagonal:** Locate the existing diagonal line of yellow (4) pixels extending from the top-left corner downwards.
2.  **Fill below the diagonal:** For each row, starting from the top, change all pixels to the left of the yellow diagonal pixel in that row to yellow (4). Stop when reaching the bottom of the grid or end of a row. The result is a filled triangle.


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
