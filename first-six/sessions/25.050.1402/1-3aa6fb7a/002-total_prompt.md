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

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1AF80>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x778677E1BF10>
**Natural Language Program:**

For each connected region of color 8 in the input grid:
1. Identify the cell within the region that has the largest row index. If there are multiple such cells, choose the one with the largest column index among them. Let's call the coordinates of this cell (R, C).
2. Check the cell directly above, at coordinates (R-1, C). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
3. If step 2 did not result in a change (either the cell above was not within bounds, not color 0, or already changed), then check the cell directly to the left, at coordinates (R, C-1). If this cell is within the grid boundaries and its color is 0 (white), change its color to 1 (blue).
4. If neither step 2 nor step 3 resulted in a change, no modification is made for this region of color 8.

This process is applied independently to each connected region of color 8 in the input grid.
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
