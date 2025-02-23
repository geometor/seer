# 00d62c1b • 002 • example_1 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 0 3 0 0
0 0 3 0 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7398A1243850>

**output:**
```
0 0 0 0 0 0
0 0 3 0 0 0
0 3 4 3 0 0
0 0 3 4 3 0
0 0 0 3 0 0
0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7398A1243490>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a grid of numerical values, representing colors. The primary element is the green (3) pixels forming a connected shape. The transformation seems to involve identifying specific green pixels and changing their color to yellow (4). The surrounding white (0) pixels remain unchanged. The shape and size of the grid are also consistent between input and output.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    properties:
      - type: 2D array
      - values: integers (0-9)
      - colors: [white, green, yellow]
  - object: pixel
    properties:
      - color: integer (representing a color)
      - position: (row, column)
  - observation:
      - description: Green pixels form a connected shape.
      - context: input and output
  - transformation:
      - action: color change
      - from: green (3)
      - to: yellow (4)
      - condition: specific green pixels within the shape
  - unchanged:
      - object: white pixels (0)
      - property: color, position

```


**Natural Language Program:**

1.  **Identify** all pixels with the value 3 (green).
2.  **Locate** the green pixels that have exactly two green neighbors, where neighbors may be above, below, to the left, or to the right - no diagonals.
3. **Change** the value/color for only the identified pixels in the previous step to 4 (yellow).
4.  All other pixels remain **unchanged**.

Essentially, the program finds 'internal' green pixels within the connected shape that form the plus-shaped regions, defined as green pixels touching only the green parts of the edge of the shape.

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
