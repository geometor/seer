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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7773C50163B0>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7773C5016AA0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Summary of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1,1), (2,1), (2,2), (4,4), (4,5), (5,4)]
      shape: Two separate 2x1 vertical shapes and 2x1 L shape.
  dimensions: 7x7

output_grid:
  objects:
    - color: 8 (azure)
      positions:  [(1,1), (2,1), (2,2), (4,4), (4,5), (5,4)]
      shape: Two separate 2x1 vertical shapes and 2x1 L shape.
    - color: 1 (blue)
      positions: [(1,2),(5,4)]
      shape: single cells

  dimensions: 7x7
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Azure Objects:** Locate all objects (contiguous regions) of color 8 (azure) in the input grid.
2.  **Preserve Azure Objects:** Keep the shape, size, and location of all azure colored object the same in the output grid.
3.  **Change color to blue:** Go over the cells of the azure objects one by one starting from top to bottom. For each azure object, locate the azure color cell that is highest and furthest to the right. Change the color of this cell from 8 (azure) to 1 (blue).

**Explanation of the Program**
The program identifies the azure objects. Then the program keeps every azure object the same with regard to shape size and position. Finally, the program modifies these original azure objects by taking only one cell of each shape and changing that cell's color from azure to blue. The single cell of the azure object that is changed is always the cell that is highest (smallest row index) and furthest right (largest column index).

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
