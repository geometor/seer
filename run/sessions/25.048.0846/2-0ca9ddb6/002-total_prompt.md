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

<PIL.Image.Image image mode=RGB size=576x576 at 0x7017B1F8F430>

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

<PIL.Image.Image image mode=RGB size=576x576 at 0x7017B1F8E7A0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  dimensions: [9, 9]
  objects:
    red_object:
      color: 2
      position: [3, 2]
      shape: single cell
    blue_object:
      color: 1
      position: [6, 6]
      shape: single cell
    background:
      color: 0
      position: all other cells
      shape: fills the remaining space

output_grid:
  dimensions: [9, 9]
  objects:
    red_object:
      color: 2
      position: [3, 2]
      shape: single cell
    blue_object:
      color: 1
      position: [6, 6]
      shape: single cell
    yellow_object:
        color: 4
        position: [[2,1], [2, 3], [4, 1], [4, 3]]
        shape: frame around red object
    orange_object:
      color: 7
      position: [[5, 6], [6, 5], [6, 7], [7, 6]]
      shape: frame around blue object
    background:
      color: 0
      position: all other cells
      shape: fills the remaining space

```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Key Objects:** In the input grid, we have two distinct objects: a single red cell (color 2) and a single blue cell (color 1). The rest is the background.

2.  **Preserve Original objects:** The red and blue cells from the input grid maintain their original position and color in the output grid.

3.  **Frame the red object:** A yellow (color 4) frame of single cells is added surrounding the red cell. The yellow frame occupies the cells directly above, below, and to the sides (i.e. it takes a cross shape, centered in the original red cell, with arms of length 1).

4.  **Frame the blue object:** An orange (color 7) frame of single cells is added, surrounding the blue cell, in the same way as the frame around the red cell.

5. **Fill the rest:** All other cells on the board remain of the background color.

**Summary of the transformation rule:**

The transformation preserves the position and color of the initial red and blue cells and frames those cells with a cross of the same size. The cross surrounding the red cell is color 4, while the cross surrounding the blue cell is color 7.

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
