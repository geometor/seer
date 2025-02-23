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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74AE8F216E90>

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

<PIL.Image.Image image mode=RGB size=448x448 at 0x74AE8F2163B0>

*text:*
Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 5)]
      shape: Two separate 2x1 and 1x2 azure objects and
output_grid:
  objects:
    - color: 8 (azure)
      positions: [(1, 1), (2, 1), (2, 2), (4, 4), (4, 5), (5, 5)]
      shape: Two separate 2x1 and 1x2 azure objects
    - color: 1 (blue)
      positions: [(1,2), (5,4)]
      shape: two 1x1 blue objects.

```

**Natural Language Program: Transformation Rule**

Here's a step-by-step description of the observed transformation:

1.  **Identify Azure Objects:** In the input grid, identify all objects with color 8 (azure). There are two of those, one on the top-left and one on the down-right.

2.  **Locate Top and Bottom of shapes:** Find a top most azure colored pixel in each object and remember it.

3. **Create a blue pixel**: Change pixel next to remembered to a blue pixel (color 1)

4.  **Preserve Other Pixels:** All other pixels in the input grid remain unchanged.

**Summary of the Rule**

The transformation rule takes the azure colored object in the input grid and creates a blue pixel next to its upmost pixel.

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
