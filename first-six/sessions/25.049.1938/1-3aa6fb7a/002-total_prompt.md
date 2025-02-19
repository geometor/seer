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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7ED3BD52EE00>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x7ED3BD52E3B0>
Okay, let's analyze the transformation between the input and output grids.

**YAML Description**

```yaml
objects:
  - color: 8 (azure)
    description: Two separate azure colored structures, each made of three cells in an L-shape.
    
  - color: 1 (blue)
      description: single blue cells

transformation:
  - The transformation involves identifying specific cells within the azure structures and changing color of those cells to blue (1)
  - In the example, the two cells changed to blue are located in the corner of the object that is furthest away from other objects.
```

**Natural Language Program**

1.  **Identify Objects:** Locate all azure (8) colored objects. In this case, we have two L-shaped structures.

2.  **Action- Change single cell color:** For each azure object, the corner cell that forms the corner furthest away from all other shapes is recolored to blue (1).

This natural language program describes the "story" of the transformation: identifying particular azure shapes and recoloring the furthest away corner of each.

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
