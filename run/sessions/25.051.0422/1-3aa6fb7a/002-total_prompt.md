# 1-3aa6fb7a • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical lines, and two separate 1x2 horizontal lines
      positions:
        - (1,1) top left of first vertical line
        - (2,1) bottom left of first vertical line
        - (3,4) top left of second vertical line
        - (4,5) bottom right of the second vertical line
        - (1,2) top right of first vertical line
        - (2,2) bottom right of first vertical line
        - (3,5) top right of second vertical line
        - (4,4) bottom left of the second vertical line

    - color: 0 (white)
      shape: background
      positions: all other cells

output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: two separate 2x1 vertical lines, and two separate 1x2 horizontal lines
      positions: same as input
    - color: 1 (blue)
      shape: single cells
      positions:
        - (1, 2)
        - (4, 4)
    - color: 0 (white)
      shape: background
      positions: all other cells
```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, we have two azure (color 8) objects. Two are 2x1 vertical lines, and two are 1x2 horizontal lines.

2.  **Observe Changes**: The first vertical line has been filled in its right neighbor cell with blue color. The second vertical line has been filled in its left neighbor cell with blue color.

3.  **Transformation Rule:** For the two vertical lines, we fill the directly adjacent cells with color blue: for the first vertical azure line, the right neighbor; for the second vertical azure line, the left neighbor.

In summary, the transformation involves adding blue (color 1) pixels adjacent to the right and to the left of the two vertical azure lines. The azure and white objects remain unchanged.

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
{ natural language description of the transformation rule }
"""

{ imports }

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
