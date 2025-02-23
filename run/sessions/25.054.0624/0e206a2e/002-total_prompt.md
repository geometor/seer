# 0e206a2e • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 3 8 1 0 0 0 0 0 0 0 0 0 0 4 0 0
0 0 8 4 8 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 8 0 8 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 8 8 4 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 8 0 8 0 0 0 0 0 0 0 0
0 0 0 4 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1152x896 at 0x70FFF0F9FAC0>

**output:**
```
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 4 8 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 3 8 8 8 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 8 8 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 3 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=1152x896 at 0x70FFF0F9FD30>
Okay, here's a breakdown of my observations, documented facts, and a natural language program describing the transformation:

**Perception of Elements**

The task involves two grids: an input grid and an output grid. Both grids contain single-digit integers (0-9), representing different colors.  The transformation seems to involve a selective shift or "sliding" of colored pixels, primarily those not colored white (0). The background (white pixels) remains unchanged. The movement of the colored pixels isn't random; there's a pattern. It appears as though non-white connected regions "drop" or move towards the bottom or the top. It looks like the direction is determined by their location, with top objects moving down and bottom objects moving up.

**YAML Block: Facts**


```yaml
facts:
  - type: grid
    description: Input and output grids of integers 0-9.
  - type: object
    description: Connected regions of non-white (non-zero) pixels.
    properties:
      - color: Integer value (1-9) representing the color.
      - position: (row, column) coordinates within the grid.
      - shape: The connected arrangement of pixels.
  - type: action
    description: Vertical movement of objects.
    properties:
      - direction: Up or Down.
      - extent: Number of rows moved. Seemingly to the nearest "obstruction" which is the edge of the grid, or another object
  - type: rule
    description: Objects in the upper part of input move down in the output. Objects in the lower part of the input move up in the output.
```


**Natural Language Program**

1.  **Identify Objects:** Find all contiguous regions (objects) of non-white (non-zero) pixels in the input grid.
2.  **Determine Movement Direction:**
    *   Find the vertical center of the grid.
    *   For each object determine if the object is located above or below of the center of the grid.
    *   If an object centroid is above the vertical center, it moves down.
    *   If an object centroid is below the vertical center, it moves up.
3.  **Move Objects:** For each object:
    *   Calculate the maximum possible movement distance in the determined direction (down or up). This distance is limited by the grid boundaries or by encountering another object.
    *   Shift the object's pixels vertically by the calculated distance.
4.  **Construct Output:** Create the output grid by placing the moved objects onto a copy of the input background (all white pixels from input).


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
