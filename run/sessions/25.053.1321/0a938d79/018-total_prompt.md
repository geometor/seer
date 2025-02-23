# 0a938d79 • 018 • example_3 - CODE

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

<PIL.Image.Image image mode=RGB size=576x1408 at 0x741530570910>

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

<PIL.Image.Image image mode=RGB size=576x1408 at 0x7415308FA980>
Okay, here's my analysis of the provided example input-output pair.

**Perception of Elements:**

The task involves a grid of pixels, initially mostly white (0).  The input contains two distinct colored pixels: red (2) and green (3). The output shows that the rows containing the red and green pixels, as well as every other row below them, are filled with the color of the initial pixel in that row. The pattern of filled rows alternates, repeating until the bottom of the grid.

**YAML Block (Facts):**


```yaml
objects:
  - type: grid
    properties:
      rows: 22
      columns: 9
      cells: pixels
      default_color: white (0)
  - type: pixel
    properties:
      color: red (2)
      initial_row: 5
      initial_column: 0
  - type: pixel
    properties:
      color: green (3)
      initial_row: 7
      initial_column: 8
actions:
  - type: fill_row
    description: Fill an entire row with a specified color.
    parameters:
      - row_index
      - color
  - type: alternate
     description: perform actions using rows with a fixed interval
relationships:
  - type: contains
    description: The grid contains pixels.
  - type: propagation
    description: The color of the initial pixels propagates downwards in an alternating pattern.
```


**Natural Language Program:**

1.  **Identify Key Pixels:** Locate all pixels in the input grid that are not white (0).
2.  **Iterate Through Key Pixels:** For each non-white pixel:
    *   Get its color and the index of the row it's in.
    *   Fill the entire row with that pixel's color.
    *   Starting from the row immediately below, and repeating every other row after, fill those rows to the same color.
    * Continue the alternating row fills until reach bottom of the input.

Essentially the existence of a non-white pixel will result in that color taking
over that row and alternating rows under it.

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
