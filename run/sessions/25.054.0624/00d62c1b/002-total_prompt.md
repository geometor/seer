# 00d62c1b • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70FFF01B1150>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x70FFF01B1DB0>
Okay, here's my analysis of the example input-output pair, focusing on perception, facts, and a natural language program describing the transformation.

**Perception of Elements:**

The task involves a 6x6 grid. The primary colors involved are white (0) and green (3). The transformation seems to involve a change of color in a specific pattern. The green pixels in the input seem to be the focal points for the transformation. Specifically, yellow (4) pixels appear in the output adjacent to green pixels.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    dimensions: [6, 6]
    elements: pixels
    properties:
      color:
        mapping:
          0: white
          3: green
          4: yellow

  - type: pixel
    properties:
      color: [white, green, yellow]
      position: [row, column]

actions:
  - name: change_color
    agent: unknown
    target: pixel
    precondition:
      color: white
      adjacent_to: green
    postcondition:
      color: yellow

relationships:
  - type: adjacency
    between: [pixel, pixel]
    types:
      - horizontal
      - vertical
```


**Natural Language Program:**

1.  **Identify** all green (3) pixels in the input grid.
2.  **Locate** all white (0) pixels that are directly adjacent (horizontally or vertically, but not diagonally) to any green pixel.
3.  **Change** the color of those located white pixels to yellow (4).
4.  **Keep** all the green and originally-non-adjacent white pixels.
5.  The output grid retains the same dimensions as the input grid.

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
