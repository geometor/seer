# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79D121213640>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x79D121211F00>
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

Here's a YAML block summarizing the initial observations:

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      shape: single cells
      positions: [0,1], [2,1]
    - color: 9 (maroon)
      count: 1
      shape: single cell
      position: [0,3]
    - color: 6 (magenta)
      count: 1
      shape: single cell
      position: [2,2]
    - color: 1 (blue)
      count: 1
      shape: single cell
      position: [3,0]

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      shape: single cells
      positions: [2,1], [3,1]
    - color: 9 (maroon)
      count: 1
      shape: single cell
      position: [3,3]
    - color: 6 (magenta)
      count: 1
      shape: single cell
      position: [3,2]
    - color: 1 (blue)
      count: 1
      shape: single cell
      position: [3,0]
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify non-white cells:** Locate all cells in the input grid that have a color other than white (0).

2.  **Move to the bottom row:** For all non-white cells, change it the position. The new position will have this cell moved the the last row.

3.  **Preserve Color and Order, relative position:** The color of each moved cell is maintained. Also, the x coordinate of the cells are preserved.

**Natural Language Program**
1. Find all cells where the value is not 0.
2. Move all non-zero cells the the last row of the grid.
3. Change the position of the cell without modifying the original column.

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
