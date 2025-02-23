# 0a938d79 • 014 • example_3 - CODE

---

# Example

**input:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 3
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

<PIL.Image.Image image mode=RGB size=576x1408 at 0x7D261845B670>

**output:**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
0 0 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3
0 0 0 0 0 0 0 0 0
2 2 2 2 2 2 2 2 2
```

<PIL.Image.Image image mode=RGB size=576x1408 at 0x7D261845B9D0>
Okay, here's my analysis of the provided example:

**Perception of Elements:**

The task involves two grids: an input grid and an output grid. Both grids contain numerical values representing colors. The primary colors observed are white (0), red (2), and green (3). The input grid contains single, isolated instances of red and green pixels, while the output grid transforms these into horizontal lines of the same color, repeated vertically in a pattern.

**YAML Block (Facts):**


```yaml
objects:
  - name: red_pixel
    type: pixel
    color: red
    value: 2
    initial_location: (5,0)
    behavior: expands horizontally and repeats vertically

  - name: green_pixel
    type: pixel
    color: green
    value: 3
    initial_location: (7,8)
    behavior: expands horizontally and repeats vertically

  - name: white_pixel
      type: pixel
      color: white
      value: 0
      initial_location: everywhere else
      behavior: gets overwritten by red and green lines, else remains white
properties:
  - grid_size:
    input: (22, 9)
    output: (22, 9)
  - expansion: horizontal
  - repetition: vertical alternating
actions:
  - expand:
    agent: red_pixel, green_pixel
    direction: horizontal
  - repeat_pattern:
     agent: red_pixel, green_pixel
     pattern: vertical alternating starting with the original color.
relationships:
  - red_pixel:
    to: green_pixel
    relation: alternate vertical repetition
```


**Natural Language Program:**

1.  **Identify Key Pixels:** Locate all pixels in the input grid that are not white (color 0). In this case, find the red pixel (value 2) and the green pixel (value 3).
2.  **Horizontal Expansion:** For each identified pixel, expand its color horizontally to fill the entire row.
3.  **Vertical Repetition:** Duplicate each expanded row vertically. Alternate rows with orignal locations for red and green, so one row of red, then a row of white, the next a row of green and a row of white, etc, throughout the entire grid. If lines of different colors are on top of each other, they will overwrite each other in the order red and green pixels.


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
