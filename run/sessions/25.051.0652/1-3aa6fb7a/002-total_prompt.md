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

**Observations and Documentation**

Here's a YAML block summarizing the initial observations:

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (rotated)
        count: 2
        positions:
          - top-left: [1,1]
          - bottom-right: [3,4]
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: L-shape (rotated)
        count: 2
        positions:
          - top-left: [1,1]
          - bottom-right: [3,4]
      - color: 1 (blue)
        shape: single cell
        count: 2
        positions:
          - next to top-left azure shape: [1,2]
          - next to bottom-right azure shape: [4,5]

```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Objects:** In the input grid, there are two L-shaped objects of color 8 (azure).

2.  **Preserve Objects:** These objects persist.

3.  **Introduce New Objects:** For the two L-shaped objects on the left, place a single cell of color 1 (blue) to their immediate right.

**Natural Language Program**
The "story" of each task is a description of how the input data is transformed to the output data as a general rule.

1.  Locate all occurrences of the L-shaped object of color 8 (azure).
2.  For each identified L-shaped object, if it is positioned on the left of the image, insert a single cell of color 1 (blue) directly to the right of the object.

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
