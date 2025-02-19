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

<PIL.Image.Image image mode=RGB size=576x576 at 0x778677E1B2B0>

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x778677E19E10>
```yaml
task_context: "The task is to modify a grid by adding colored cells around existing non-zero colored cells based on their original color. Specifically, red cells get yellow diagonals, and blue cells get orange orthogonals."
objects:
  - red_cell:
      color: 2
      action: surround with yellow diagonals
  - blue_cell:
      color: 1
      action: surround with orange orthogonals
predicates:
  - is_red: cell color is 2
  - is_blue: cell color is 1
actions:
  - add_yellow_diagonals: place yellow cells at the four diagonal positions of the red cell
  - add_orange_orthogonals: place orange cells at the four orthogonal positions of the blue cell
transformation_rule: "For each red cell in the input grid, place yellow cells at its diagonal positions in the output grid. For each blue cell in the input grid, place orange cells at its orthogonal positions in the output grid. Keep all other cells as they are from the input, except for the positions where new colors are placed."
```

**Natural Language Program:**

The process transforms the input grid by examining each cell.
If a cell contains the color red (2), then in the output grid, yellow cells (4) are placed at the four diagonal positions relative to this red cell.
If a cell contains the color blue (1), then in the output grid, orange cells (7) are placed at the four orthogonal (up, down, left, right) positions relative to this blue cell.
If a cell is of any other color, it remains unchanged in the output grid, unless it becomes modified by the placement of new colors around red or blue cells.
The modifications for red and blue cells are independent and can potentially overlap. If they do overlap, the color placed last will overwrite the previous one. In this example, no overlaps occur.
The process is applied to each cell in the input grid that is either red or blue.
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
