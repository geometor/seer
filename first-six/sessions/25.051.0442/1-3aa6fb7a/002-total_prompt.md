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

![Image](000-example_1_input.png)


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

![Image](000-example_1_output.png)

Okay, let's analyze the transformation between the input and output grids.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: 'L-shape'
      positions: [[1,1], [2,1], [2,2]]
    - color: 8 (azure)
      shape: 'reverse L-shape'
      positions: [[3,4], [3,5], [4,5]]
output_grid:
  objects:
    - color: 8 (azure)
      shape: 'L-shape'
      positions: [[1,1], [2,1], [2,2]]
    - color: 8 (azure)
      shape: 'reverse L-shape'
      positions: [[3,4], [3,5], [4,5]]
    - color: 1 (blue)
      shape: 'single cell'
      positions: [[1,2]]
    - color: 1 (blue)
      shape: 'single cell'
      positions: [[4,4]]      
```

**Natural Language Description of Transformation Rule**

1.  **Identify Objects:** In the input grid, we can see two distinct objects of color 8 (azure). One is an "L-shape" in the top-left corner, and the other is a "reverse L-shape" in the bottom-right corner.

2.  **Detect Changes:** The azure shapes are preserved from input to output. The changes are single blue cells that were not present in input grid.

3. **Determine filling rule:** Find the cell to the immediate right of the top-left corner of each azure object and change the color of this cell to 1 (blue).

**Natural Language Program**
```
For each azure object in the input grid:
    Locate the top-left corner of the object.
    Move one cell to the right of the top-left corner.
    Change the color of this cell to blue (1).
    Preserve the initial objects.
```

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
