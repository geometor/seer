# 3-1e0a9b12 • 003 • example_2 - NLP

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
```python
"""
The transformation rule is to move all non-zero colored objects in each column of the input grid to the bottom of the corresponding column in the output grid, while maintaining their vertical order within each column. Any empty spaces created at the top of the columns in the output grid are filled with white color (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero elements in each column to the bottom,
    maintaining their order, and filling the remaining spaces with zeros.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)  # Initialize output_grid with zeros

    num_rows, num_cols = input_grid.shape

    # Iterate through each column
    for j in range(num_cols):
        # Extract non-zero elements from the current column
        non_zero_elements = input_grid[:, j][input_grid[:, j] != 0]
        
        # Calculate the starting row index for placing non-zero elements at the bottom
        start_row = num_rows - len(non_zero_elements)
        
        # Place the non-zero elements at the bottom of the corresponding column in output_grid
        output_grid[start_row:, j] = non_zero_elements

    return output_grid
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

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
