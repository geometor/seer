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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F15E10>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x76CC79F16EC0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
input_grid:
  objects:
    - color: 8
      shape: 'L-shape'
      position: (1,1) and connected cells
    - color: 8
      shape: 'L-shape'
      position: (3,4) and connected cells
  grid_size: (7,7)

output_grid:
    - color: 8
      shape: 'L-shape'
      position: (1,1) and connected cells
    - color: 8
      shape: 'L-shape'
      position: (3,4) and connected cells
    - color: 1
      shape: 'single cell'
      position: (2,1)
    - color: 1
      shape: 'single cell'
      position: (3,4)
  grid_size: (7,7)
```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we can identify two distinct L-shaped objects, both composed of azure (color 8) cells. One located in top-left, the other in bottom-right.

2.  **Detect Change**: The L-shapes formed by color 8 are kept, and where each shape began, a color 1 is placed.

3. **Transformation Rule:** The program scans the input, keeps every shape, and adds a blue pixel (color 1) in the starting top-left cell of each color 8 shape.


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
