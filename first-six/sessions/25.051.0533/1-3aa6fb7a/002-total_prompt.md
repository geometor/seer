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

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (two instances)
        positions:
          - top-left corner: [1,1] (2x2 block with one cell removed)
          - bottom-right corner: [3,4] (2x2 block with one cell removed)
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (two instances)
        positions:
          - top-left corner: [1,1] (2x2 block with one cell removed)
          - bottom-right corner: [3,4] (2x2 block with one cell removed)
      - color: 1 (blue)
        shape: single cell
        positions:
          - [1,2] #next to the top object
          - [4,5] #next to the bottom object
      - color: 0 (white)
        shape: background
        position: fills the remaining cells
```

**Natural Language Program:**

1.  **Identify Objects:** Locate all instances of color 8 (azure) objects in the input grid. Note their positions. These objects form an "L" shape, consisting of a 2x2 block with one cell removed.

2.  **Preserve Objects:** Keep every object of color 8 in its original position in the output grid.

3.  **Introduce New Objects:** Add new objects to the grid.
    *    To the right of the top left object 8, introduce a single cell of color 1 (blue) if and only if the cell to the right of the object is color 0.
    *    To the left of the bottom right object 8, introduce a single cell of color 1 (blue) if and only if the cell to the left of the object is color 0.

In summary, the transformation preserves the azure "L" shaped objects and adds a blue cell adjacent to each, based on the initial positions of these shapes, with the added blue cells located on opposite sides.

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
