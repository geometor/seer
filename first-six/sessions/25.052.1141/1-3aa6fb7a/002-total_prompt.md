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

Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: Two 2x1 vertical rectangles
        positions:
          - (1,1), (2,1)
          - (3,4), (4,5) # Note, it's diagonal.
      - color: 0 (white)
        shape: Background
        positions: All other cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: Two 2x1 vertical rectangles
        positions:
          - (1,1), (2,1)
          - (3,4), (4,5)
      - color: 1 (blue)
        shape: Two single cells
        positions:
            - (1,2)
            - (4,4)
      - color: 0 (white)
        shape: Background
        positions: All other cells
```

**Natural Language Program:**

Here's a step-by-step description of the observed transformation:

1.  **Identify Objects:** In the input grid, we can identify two azure (color 8) objects. Each object is a 2x1 vertical rectangle. There are also a lot of white cells which act as background.

2.  **Observe Changes:** In the output grid, we see the same azure objects have not been altered. However, one new blue cell is added on the right side of each azure object.

3. **Infer the Rule:** It's inferred that for each vertical 2x1 azure (8) rectangle, we perform the action to add a blue(1) pixel at the right of its top and bottom.

**Transformation Rule (Concise):**

Locate each 2x1 vertical rectangle of azure color (8). Add a blue cell (1) to the immediate right of both cells that constitute the 2x1 azure object.


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
