# d037b0a7 • 008 • example_2 • investigate_coder

---

## Example 2

**input:**
```
0 2 0
7 0 8
0 0 0
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7D20A517B7C0>

**output:**
```
0 2 0
7 2 8
7 2 8
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7D20A517BCA0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves a 3x3 grid of colored pixels. The input grid transforms into an output grid. The colors present are white (0), red (2), orange (7), and azure (8). The transformation appears to involve a specific color, in this case red (2), influencing the output. The transformation seems to fill every color in the row below the red with the red color. It also fills the row above the red with the red color, in this case the above is white (0) and stays white.

**YAML Fact Block:**


```yaml
facts:
  - task_type: grid_transformation
  - grid_size: 3x3
  - colors:
    - white: 0
    - red: 2
    - orange: 7
    - azure: 8
  - objects:
      - grid: 2d array of pixels
      - pixel: individual cell in grid with a color value.
  - actions:
      - fill_color: change the cell's color based on surrounding colors.
  - transformation_rule: >
    If a 'red' color is present, every color in that row below that color becomes 'red'.
```


**Natural Language Program:**

1.  **Identify Red Pixels:** Locate all pixels in the input grid that have the color red (value 2).
2. **Fill the row below:** For each red pixel found, examine the next row. Transform every pixel in the next row to be the same color as the "red" pixel, in this case, red (2).
3.  The output grid is the result of these transformations.


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
