# 4-0d3d703e • 002 • example_1 - CODE

---

**input**
```
3 1 2
3 1 2
3 1 2
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7291F661E8F0>

**output**
```
4 5 6
4 5 6
4 5 6
```

<PIL.Image.Image image mode=RGB size=192x192 at 0x7291F661E830>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Input and Output**

```yaml
input_grid:
  size: 3x3
  objects:
    - color: 3 (green)
      shape: vertical line
      position: (0,0), (1,0), (2,0)
    - color: 1 (blue)
      shape: vertical line
      position: (0,1), (1,1), (2,1)
    - color: 2 (red)
      shape: vertical line
      position: (0,2), (1,2), (2,2)

output_grid:
  size: 3x3
  objects:
    - color: 4 (yellow)
      shape: vertical line
      position: (0,0), (1,0), (2,0)
    - color: 5 (gray)
      shape: vertical line
      position: (0,1), (1,1), (2,1)
    - color: 6 (magenta)
      shape: vertical line
      position: (0,2), (1,2), (2,2)
```

**Natural Language Program: Transformation Rule**

The transformation rule appears to be a simple color mapping, incrementing each color value by one. There is no movements, no interaction. The shape and the positions remain constant.

1.  **Iterate** through each cell in the input grid.
2.  **Increment** the color value of the current cell by 1. But this is a special increment:
    if the value is 0, transform to 1
    if the value is 1, transform to 2
    if the value is 2, transform to 3
    if the value is 3, transform to 4
    if the value is 4, transform to 5
    if the value is 5, transform to 6
    if the value is 6, transform to 7
    if the value is 7, transform to 8
    if the value is 8, transform to 9
    if the value is 9, transform to 0.
3.  **Place** the new color value into the corresponding cell in the output grid.

Alternative and simpler description:

1.  **Iterate** through each cell in the input grid.
2.  **Transform** the number `n` in each cell into `(n + 1) % 10`.
3. **Place** the new number into the corresponding cell in the output grid.

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
