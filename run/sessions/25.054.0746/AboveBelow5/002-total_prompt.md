# AboveBelow5 • 002 • example_1 • investigate_coder

---

## Example 1

**input:**
```
0 0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0 0
0 1 0 0 0 1 0 0 0
0 1 0 0 0 3 0 0 1
0 1 0 0 0 1 0 0 1
0 1 0 0 0 1 0 0 1
0 1 0 0 0 1 0 0 3
0 3 0 0 0 1 0 0 1
0 1 0 0 0 1 0 0 1
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7995F90382E0>

**output:**
```
0 0 0 0 0 3 0 0 0
0 0 0 0 0 3 0 0 0
0 3 0 0 0 3 0 0 0
0 3 0 0 0 3 0 0 3
0 3 0 0 0 1 0 0 3
0 3 0 0 0 1 0 0 3
0 3 0 0 0 1 0 0 3
0 3 0 0 0 1 0 0 1
0 1 0 0 0 1 0 0 1
```

<PIL.Image.Image image mode=RGB size=576x576 at 0x7995F45BAFE0>
Okay, here's my analysis of the provided example, formatted as a report:

**Perception of Elements:**

The task involves two grids of colored pixels. The colors seem to be changing based on some underlying rule related to their initial color and possibly their position. We have white (0), blue (1), and green (3). It appears we are swapping some blues with greens and some greens with blues.

**YAML Fact Block:**


```yaml
facts:
  - observation: |
      The input and output grids have the same dimensions (9x9).
  - object: pixels
    properties:
      color: [white, blue, green]
      position: [row, column]
    actions:
      - name: change_color
        conditions:
          - if original color is blue and a specific pattern is met, change to green.
          - if original color is green and a specific pattern is met, change to blue.
  - relationship: |
       The color change seems to be dependent on original color and spatial properties. Specifically a vertical stripe in the center.
```


**Natural Language Program:**

1.  **Identify Key Column:** Locate the central vertical column (column index 5, since the grid is 9x9).

2.  **Conditional Color Swap:**
    *   Iterate through each pixel in the input grid.
    *   If a pixel in the input is blue (1) AND it is *not* in the central column, change it to green (3) in the output grid.
    *   If a pixel in the input is green (3) AND it *is* in the central column, change to blue (1) in the output grid.

3.  **Preserve Other Pixels:** All other pixels (white/0) retain their original color and position in the output grid.

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
