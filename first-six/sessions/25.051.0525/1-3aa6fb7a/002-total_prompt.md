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
        shape: two separate 2x1 rectangles
        positions:
          - top_left: [1,1]
          - top_left: [3,4]
      - color: 0 (white)
        shape: background
        positions:
          - all cells not occupied by color 8
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: two separate 2x1 rectangles
        positions:
          - top_left: [1,1]
          - top_left: [3,4]
      - color: 1 (blue)
        shape: single cells
        positions:
          - top_left: [1,2]
          - top_left: [4,4]
      - color: 0 (white)
        shape: background
        positions:
          - all cells not occupied by color 8 or 1
```

**Natural Language Program:**

1.  **Identify Objects:** In the input grid, we have two distinct objects of color 8 (azure). These objects are 2x1 rectangles. One is located at the top-left corner (1, 1), and the second at position (3,4).

2.  **Detect Changes**: Comparing the input and output, we can see that a color 1 (blue) cell has been added to the right of the top rectangle (at [1,2]). We can see that the other color 1 (blue) cell is added to the left of the bottom rectangle (at [4,4]).

3. **Transformation Rule:**
    -   For the top azure rectangle, add a blue cell to the immediate right of the rectangle.
    -   For the bottom azure rectangle, add a blue cell to the immediate left of the rectangle.

**Summary**

The program identifies each 2x1 azure rectangle. For the topmost rectangle, add a blue cell to the immediate right. For the bottommost rectangle, add a blue cell to the immediate left.

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
