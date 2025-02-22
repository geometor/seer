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

![Image](001-example_1_input.png)


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

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input to the output grid.

**YAML Description**

```yaml
observations:
  input:
    objects:
      - color: 8 (azure)
        shape: Two separate 2x1 vertical rectangles
        positions:
          - (1,1) and (2,1) # row, column indexing starting from 0
          - (3,4) and (4,4)
    grid_size: (7, 7)
  output:
    objects:
      - color: 8 (azure)
        shape: Two separate 2x1 vertical rectangles
        positions:
          - (1,1) and (2,1)
          - (3,4) and (4,4)
      - color: 1 (blue)
        shape: single cell
        positions:
            - (1,2)
            - (4,3)
    grid_size: (7, 7)

```

**Natural Language Program**

Here's a step-by-step description of the transformation:

1.  **Identify Objects:** In the input grid, we identify two azure (color 8) objects. Each object is a 2x1 vertical rectangle.
2.  **Preserve Objects:** These two azure objects are preserved in their original locations in the output grid.
3.  **Add Blue cell, first object:** A blue cell (color 1) is added to the output grid, to the right of the top cell of the first azure object.
4.  **Add Blue cell, second object:** A blue cell (color 1) is added to the output grid, to the left of the bottom cell of the second azure object.

**Complete Natural Language Description**
The output preserves the azure colored object and adds a blue pixel adjacent to the azure object, to the right of its top-left corner, and one to the left of the bottom-right one.

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
