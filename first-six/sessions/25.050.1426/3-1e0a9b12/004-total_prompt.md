# 3-1e0a9b12 • 004 • example_2 - CODE

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

**Natural Language Program:**

The transformation operates column by column. For each column in the input grid, identify all the non-zero color values.  Then, in the output grid, populate the same column from bottom to top with these identified non-zero color values in the same order they appeared in the input column. Fill the remaining cells in the top rows of the output column with the color white (0). This effectively pushes all colored blocks in each column to the bottom.
```python
"""
The transformation operates column by column. For each column in the input grid, identify all the non-zero color values.  Then, in the output grid, populate the same column from bottom to top with these identified non-zero color values in the same order they appeared in the input column. Fill the remaining cells in the top rows of the output column with the color white (0). This effectively pushes all colored blocks in each column to the bottom.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by pushing all non-zero values in each column to the bottom.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate over each column
    for j in range(cols):
        # Extract non-zero values from the current column
        non_zero_values = input_grid[:, j][input_grid[:, j] != 0]
        # Calculate the starting row index for placing non-zero values
        start_row = rows - len(non_zero_values)
        # Place the non-zero values at the bottom of the output column
        output_grid[start_row:, j] = non_zero_values

    return output_grid.tolist()
```


**input**
```
0 0 0 0 0 9
0 0 0 8 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 0 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

![Image](002-example_2_output.png)

**Natural Language Program:**

The transformation is applied column by column. For each column, we identify the colored blocks (non-zero cells).  The action is to "push down" these colored blocks to the bottom of the column, maintaining their original order from top to bottom within that column.  Any empty spaces created at the top of the column after pushing the colored blocks down are filled with white (color 0).  This effectively sorts the colors in each column by placing all white blocks (0) at the top and all colored blocks at the bottom, preserving the relative order of the colored blocks.
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
