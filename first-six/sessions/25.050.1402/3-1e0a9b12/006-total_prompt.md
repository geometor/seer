# 3-1e0a9b12 • 006 • example_3 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x778677E1B550>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x778677E19E10>
**Natural Language Program:**

The transformation rule is to move all non-zero numbers in each column to the bottom of the column, filling the empty spaces at the top with zeros.  The order of the non-zero numbers within each column is preserved, although in this example each column contains at most one non-zero number.

**Step-by-step transformation:**

1. **Iterate through each column** of the input grid from left to right.
2. **For each column**, identify and extract all the non-zero numbers, maintaining their original order from top to bottom.
3. **Count the number of non-zero numbers** extracted for the current column. Let's call this count 'N'.
4. **In the corresponding column of the output grid**, fill the bottom 'N' rows with the extracted non-zero numbers, in the same order as they were extracted.
5. **Fill the remaining rows at the top** of the output column with zeros.
6. Repeat steps 2-5 for all columns.

This process effectively "pushes down" all the non-zero numbers in each column to the bottom.
```python
"""
The transformation rule is to move all non-zero numbers in each column to the bottom of the column, filling the empty spaces at the top with zeros. The order of the non-zero numbers within each column is preserved.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero numbers in each column to the bottom.
    
    Args:
        input_grid (list of lists): The input grid represented as a 2D list.
    
    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column
    for j in range(cols):
        # Extract non-zero numbers from the current column
        non_zero_elements = input_grid[:, j][input_grid[:, j] != 0]
        
        # Count the number of non-zero elements
        num_non_zero = len(non_zero_elements)
        
        # Fill the bottom 'num_non_zero' rows of the output column with the extracted numbers
        output_grid[rows - num_non_zero:, j] = non_zero_elements
        
        # Fill the remaining top rows with zeros (this is already done during initialization)

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

<PIL.Image.Image image mode=RGB size=384x384 at 0x778677E1B2B0>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7786773723E0>
**Natural Language Program:**

The transformation rule involves processing each column of the input grid independently. For each column, the operation is to gather all non-zero numbers and reposition them at the bottom of the same column in the output grid, while filling the top portion of the column with zeros. The relative order of the non-zero numbers within each column is maintained during this process.

**Step-by-step transformation:**

1. **For each column** in the input grid, proceeding from the first column to the last:
    - **Identify all non-zero numbers** present in the current column.
    - **Extract these non-zero numbers**, maintaining their original top-to-bottom order within the column.  Think of collecting these numbers as if picking them up from top to bottom.
    - **Count the number of extracted non-zero numbers**. Let's call this count 'N'.
    - **Place these 'N' non-zero numbers** in the output grid's corresponding column, starting from the bottom-most rows and moving upwards for 'N' rows.  The order of placement should be the same as the extracted order.
    - **Fill the remaining positions** in the output grid's column, above the placed non-zero numbers, with zeros.

2. Repeat step 1 for every column in the input grid.

This procedure effectively "stacks" all the non-zero numbers in each column at the bottom, preserving their vertical order and padding the top with zeros.
```python
"""
The transformation rule involves processing each column of the input grid independently. For each column, the operation is to gather all non-zero numbers and reposition them at the bottom of the same column in the output grid, while filling the top portion of the column with zeros. The relative order of the non-zero numbers within each column is maintained during this process.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero numbers in each column to the bottom.
    
    Args:
        input_grid (list of lists): The input grid represented as a 2D list.
    
    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Iterate through each column
    for j in range(cols):
        # Extract non-zero numbers from the current column
        non_zero_elements = input_grid[:, j][input_grid[:, j] != 0]
        
        # Count the number of non-zero elements
        num_non_zero = len(non_zero_elements)
        
        # Fill the bottom 'num_non_zero' rows of the output column with the extracted numbers
        output_grid[rows - num_non_zero:, j] = non_zero_elements
        
        # Fill the remaining top rows with zeros (this is already done during initialization)

    return output_grid.tolist()
```


**input**
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x778677373760>

**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x778677371E10>
**Natural Language Program:**

The transformation rule operates on each column of the grid independently. For each column, the goal is to rearrange the numbers such that all non-zero numbers are moved to the bottom of the column, while the top positions are filled with zeros. The relative vertical order of the non-zero numbers within each column is maintained.

**Step-by-step transformation:**

1. **Process each column:** Iterate through the input grid column by column, starting from the leftmost column and moving to the right.

2. **Identify non-zero objects in the column:** Within the current column, locate all cells containing non-zero numbers. These are the "objects" we are interested in.

3. **Preserve and extract non-zero objects:**  As you scan the column from top to bottom, collect all the non-zero number objects in the order they appear. Imagine you are picking up the non-zero numbers from top to bottom in the column.

4. **Count the non-zero objects:** Determine the total count of non-zero objects you've extracted from the current column. Let's say this count is 'N'.

5. **Reposition non-zero objects at the bottom:** In the output grid's corresponding column, start from the bottom row and fill the bottom 'N' rows with the extracted non-zero objects, maintaining the order in which you collected them.

6. **Fill top positions with zero objects:** For the remaining rows in the output column, above the positioned non-zero objects, fill them with zeros. These become "zero objects".

7. **Repeat for all columns:** Continue steps 2-6 for every column in the input grid.

By applying this process to each column, we effectively "push" all the non-zero number objects in each column downwards to the bottom, stacking them up and filling the space above with zero objects. The original vertical order of the non-zero objects within each column is preserved during this transformation.
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
