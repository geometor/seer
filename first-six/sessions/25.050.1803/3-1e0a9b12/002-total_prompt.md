# 3-1e0a9b12 • 002 • example_1 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

![Image](000-example_1_output.png)

**Natural Language Description of Transformation:**

The transformation rule is to move all non-zero colored objects in each column of the input grid to the bottom of the corresponding column in the output grid, while maintaining their vertical order within each column.  Any empty spaces created at the top of the columns in the output grid are filled with white color (0).

**Step-by-step transformation:**

1. **Column-wise Processing:** The transformation is applied independently to each column of the input grid.
2. **Identify Non-Zero Objects:** For each column, identify all the cells that are not white (color 0).
3. **Preserve Vertical Order:** Note the order of these non-zero objects from top to bottom within the column.
4. **Move to Bottom:** In the output grid, for the same column index, place these non-zero objects in the bottom-most rows, maintaining the same vertical order identified in step 3.
5. **Fill with White:** Fill all the rows above the placed non-zero objects in the output column with white color (0).
6. **Repeat for All Columns:** Repeat steps 2-5 for every column in the input grid.

This process results in an output grid where all the colored objects from each input column are stacked at the bottom of the corresponding output column, with any remaining space at the top of the columns filled with white.
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
