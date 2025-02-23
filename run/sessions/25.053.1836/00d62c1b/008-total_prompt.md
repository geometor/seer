# 00d62c1b • 008 • example_2 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 0 3 0 0
0 0 0 3 0 4 3 0 0 0
0 0 3 4 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7747C2C53910>

**output:**
```
0 0 0 0 0 0 0 0 0 0
0 0 3 0 3 0 0 0 0 0
0 0 0 3 0 3 0 0 0 0
0 0 3 0 0 0 3 0 0 0
0 0 0 0 0 3 4 3 0 0
0 0 0 3 0 3 3 0 0 0
0 0 3 3 3 0 0 0 0 0
0 0 0 3 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x7747C2C53A00>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Task Elements:**

The task involves a grid of colored pixels. The primary colors observed are white (0), green (3), and yellow (4). The transformation appears to involve a local operation around a specific color, namely yellow (4). It seems that green pixels adjacent to a yellow pixel get a priority.

**YAML Fact Block:**


```yaml
facts:
  - object: grid
    description: 2D array of pixels
    properties:
      - width: 10
      - height: 10
      - values: [0, 3, 4]

  - object: pixel
    properties:
      - color:
        - white: 0
        - green: 3
        - yellow: 4
      - position: [row, column]

  - relation: adjacency
    description: Pixels are considered adjacent if they share a side (not diagonal).

  - action: change_color
    description: A pixel's color changes based on its neighbors.
    parameters:
      - from: 4
      - to: 3
    conditions:
      neighbor: yellow
```


**Natural Language Program:**

1.  **Identify Target Pixels:** Locate all yellow (4) pixels within the input grid.

2.  **Check Neighbors** For each green pixel, iterate through all the direct neighbors.

3.  **Conditional Modification:** Find green pixels that are next to yellow pixel.

4.  **Apply Rule universally:** Change all yellow cells to Green.


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
