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

```yaml
task_context: "The task is to modify an input grid based on the contiguous regions of color 8 (azure). For each such region, we need to identify its 'end points', specifically those cells within the region that have exactly one neighbor also belonging to the same region. From these 'end points', we determine the 'top-most' and 'bottom-most' based on their row and column indices. Then, for the 'top-most' end point, we place a color 1 (blue) cell immediately to its right. For the 'bottom-most' end point, we place a color 1 cell immediately to its left."
natural_language_program: |
  For each connected component of color 8 in the input grid:
  1. Identify all cells that form the connected component of color 8.
  2. For each cell in this component, count the number of its neighbors (up, down, left, right) that are also part of the same component.
  3. Determine the "end points" of the component. An "end point" is a cell that has exactly one neighbor within the same color 8 component.
  4. Find the "top-most end point" among all identified end points. This is the end point with the minimum row index. If there's a tie in row indices, choose the one with the minimum column index.
  5. Find the "bottom-most end point" among all identified end points. This is the end point with the maximum row index. If there's a tie in row indices, choose the one with the minimum column index.
  6. In the output grid, place a color 1 (blue) cell immediately to the right of the "top-most end point".
  7. In the output grid, place a color 1 (blue) cell immediately to the left of the "bottom-most end point".
  8. If a grid cell is not modified by steps 6 or 7, it retains its original color from the input grid.
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
