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

**YAML Summary of Observations**

```yaml
task: 001-example_1
observations:
  input_grid:
    - "Two separate objects of color 8 (azure)."
    - "Object 1: A vertical line of length 2 at position (1,1)."
    - "Object 2: A horizontal line of length 2 at position (4,3)."
  output_grid:
    - "Same two objects of color 8 (azure)."
    - "Object 1: Remains a vertical line of length 2 at position (1,1)."
    - "Object 2: Remains a horizontal line of length 2 at position (4,3)."
    - "A new color 1 (blue) appears at position (2,1) next to the first object (Object 1)"
    - "A new color 1 (blue) appears at position (4,4) next to the second object (Object 2)"
```

**Natural Language Program: Step-by-step Transformation**

1.  **Identify Objects:** Locate all distinct azure (color 8) objects in the input grid. In this case, we have two such objects: a vertical line and a horizontal line.

2.  **Preserve Objects:** The azure objects are unchanged between input and output.

3. **Introduce New Color:** For each of the two original azure objects, add a blue (color 1) pixel. The blue pixel should be put to the right of the bottom of the Object 1. The blue pixel should be put on the left of the top pixel of Object 2.

**Elaboration**
The main rule is to add specific colored pixels to identified objects in specific positions.

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
