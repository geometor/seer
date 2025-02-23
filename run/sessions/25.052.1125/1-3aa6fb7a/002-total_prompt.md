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

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Observation:**

```yaml
observations:
  input_grid:
    - "Two separate azure (8) objects."
    - "First object: A vertical line of two cells at (1,1) and (2,1)."
    - "Second object: A horizontal line of two cells at (3,4) and (3,5)."
  output_grid:
    - "Same azure (8) objects remain in the same positions."
    - "A blue (1) cell appears adjacent to the top of the first azure object at (1,2)."
    - "A blue (1) cell appears adjacent to the bottom of the second azure object at (4,4)."
```

**Natural Language Program:**

1.  **Identify Objects:** Locate all azure (8) colored objects within the input grid. There are two such objects.

2.  **Object 1 Transformation:**
    *   Locate the topmost cell of the first azure object.
    *   Place a blue (1) cell directly adjacent to the right of the top of this azure object.

3.  **Object 2 Transformation:**
    *    Locate the bottommost cell of the second azure object.
    *   Place a blue (1) cell directly adjacent to the left of the bottom of this azure object.

4. Retain: Maintain the initial positions and the shape of the azure objects.

In summary, the transformation rule involves identifying azure objects and placing blue cells adjacent to specific points on these objects. The first azure object gets a blue cell to the right of the top end, and second azure object receives a blue cell to the left of its bottom end.

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
