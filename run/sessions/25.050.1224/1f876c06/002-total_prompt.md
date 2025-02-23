# 1f876c06 • 002 • example_1 - CODE

---

**input**
```
0 0 2 0 0 6 0 0 0 0
0 0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 6
0 0 0 4 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABB63AA10>

**output**
```
0 0 2 0 0 6 0 0 0 0
0 2 0 0 0 0 6 0 0 0
2 0 0 0 0 0 0 6 0 0
0 0 0 0 0 0 0 0 6 0
0 0 0 0 0 0 0 0 0 6
0 0 0 4 0 0 0 0 0 0
0 0 0 0 4 0 0 0 0 0
0 0 0 0 0 4 0 0 0 0
0 0 0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 4 0 0
```

<PIL.Image.Image image mode=RGB size=640x640 at 0x79CABB63B520>
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 2 # Red
      positions: [(0, 2), (2, 0)]
    - color: 6 # Magenta
      positions: [(0, 5), (4, 9)]
    - color: 4 # Yellow
      positions: [(5, 3), (9, 7)]
    - color: 0 # white
      positions: All the remaining cells

output_grid:
  objects:
    - color: 2 # Red
      positions: [(0, 2), (1, 1), (2, 0)]
    - color: 6 # Magenta
      positions: [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
    - color: 4 # Yellow
      positions: [(5, 3), (6, 4), (7, 5), (8, 6), (9, 7)]
    - color: 0
      positions: All other cells
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of several single-cell objects of colors 2 (red), 6 (magenta), and 4 (yellow), with the rest being color 0 (white).

2.  **Observe Movement Pattern:** Each non-white object appears to initiate a downward-sloping diagonal line (extending down and to the right) in the output grid.
    -   Specifically for red, the colors expands 1 cell diagonally right-down.
    -   Specifically for yellow, the color expands 4 cells diagonally right-down
    -   Specifically for magenta, the color expands 4 cells diagonally right-down

3. **Transformation rule:**
   The colored cells of the input are used as seeds. From each seed, use the following steps to generate the diagonal:
   * define a line segment with slope 1 and origin at the seed cell.
   * let `k` be the row index of the seed.
   * if `k` < 5, extend the line by drawing 4 more cells
   * otherwise, draw cells until the end of the grid.
   

In summary, the transformation rule takes each isolated colored cell in the input and extends it diagonally (down and to the right) by a certain number of cells based on its row index.

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
