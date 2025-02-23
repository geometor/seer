# 0dfd9992 • 002 • example_1 - CODE

---

**input**
```
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 0 0 0 0 0 5
2 5 4 5 2 1 2 5 0 0 2 1 2 5 4 0 0 0 0 0 4
3 6 5 6 3 2 3 0 0 0 0 2 3 6 5 0 0 0 0 0 5
6 3 2 3 6 5 6 0 0 0 0 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 0 0 0 0 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 0 0 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 0 0 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 0 0 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 0 0 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 0 0 0 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 0 0 0 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 0 0 0 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
```

<PIL.Image.Image image mode=RGB size=1344x1344 at 0x79CABB63B520>

**output**
```
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4
3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5
6 3 2 3 6 5 6 3 2 3 6 5 6 3 2 3 6 5 6 3 2
5 2 1 2 5 4 5 2 1 2 5 4 5 2 1 2 5 4 5 2 1
```

<PIL.Image.Image image mode=RGB size=1344x1344 at 0x79CABB63BA60>
Okay, let's analyze the transformation between the input and output grids.

**Observations and Documentation (YAML)**

```yaml
input_grid:
  size: 21x21
  objects:
    - color: 0
      shape: irregular, dispersed
      count: 24
    - color: 1
      shape: irregular, dispersed
      count: 12
    - color: 2
      shape: irregular, dispersed
      count: 48
    - color: 3
      shape: irregular, dispersed
      count: 40
    - color: 4
      shape: irregular, dispersed
      count: 24
    - color: 5
      shape: irregular, dispersed
      count: 49
    - color: 6
      shape: irregular, dispersed
      count: 44
    - color: 7
      shape: irregular, dispersed
      count: 0
    - color: 8
      shape: irregular, dispersed
      count: 0
    - color: 9
      shape: irregular, dispersed
      count: 0

output_grid:
  size: 21x21
  objects:
    - color: 0
      shape: All the positions where the color was 0 are now the color that existed in the input.
      count: 0
    - color: 1
      shape: irregular, dispersed
      count: 12
    - color: 2
      shape: irregular, dispersed
      count: 48
    - color: 3
      shape: irregular, dispersed
      count: 40
    - color: 4
      shape: irregular, dispersed
      count: 24
    - color: 5
      shape: irregular, dispersed
      count: 49
    - color: 6
      shape: irregular, dispersed
      count: 44
      - color: 7
      shape: irregular, dispersed
      count: 0
    - color: 8
      shape: irregular, dispersed
      count: 0
    - color: 9
      shape: irregular, dispersed
      count: 0
```

**Determining the Transformation Rule (Natural Language Program)**

1.  **Identify Zero-Colored Cells:** Locate all cells in the input grid that have the color value '0' (white).

2. **Remove Zero Coloured Cells:** All the positions with color 0 are replaced with the color that occupied that position in the input grid.

**General Rule:** The output is created by replacing every cell of color 0 in the input to a cell in the previous position.


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
