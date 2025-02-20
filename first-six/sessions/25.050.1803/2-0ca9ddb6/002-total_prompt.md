# 2-0ca9ddb6 • 002 • example_1 - CODE

---

**input**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 2 0 0 0 0 0 0
0 4 0 4 0 0 0 0 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 7 1 7 0
0 0 0 0 0 0 7 0 0
0 0 0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

```yaml
task_context: "The task is to transform an input grid into an output grid based on the colors of non-zero cells. Specific colors trigger different types of neighbor modifications."
natural_language_program: |
  1. Initialize the output grid as a direct copy of the input grid.
  2. Iterate through each cell of the input grid, identifying each cell by its row and column index.
  3. For each cell, check if its value is non-zero (greater than 0).
  4. If the cell's value is non-zero, determine its color.
  5. If the color of the cell is red (color code 2), then for each of the four diagonal neighbor positions (top-left, top-right, bottom-left, bottom-right) relative to the current cell, set the value of the cell at that position in the output grid to yellow (color code 4).
  6. If the color of the cell is blue (color code 1), then for each of the four orthogonal neighbor positions (up, down, left, right) relative to the current cell, set the value of the cell at that position in the output grid to orange (color code 7).
  7. After checking and potentially modifying neighbors for all non-zero cells, the output grid is considered complete.
  8. Note that the original non-zero cells in the input grid remain in their positions and with their original colors in the output grid.
  9. Cells that were zero in the input grid remain zero in the output grid unless they are modified by being neighbors of a non-zero cell according to steps 5 and 6.
```
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
