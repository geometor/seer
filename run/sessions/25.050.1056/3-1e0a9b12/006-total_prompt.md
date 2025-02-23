# 3-1e0a9b12 • 006 • example_3 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7A151BB0F5E0>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7A151BB0DEA0>
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations in YAML format:**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      positions: [[0,0], [0,2], [1,0], [1,1], [1,2], [1,3], [2,0], [2,3], [3,1], [3,2]]
    - color: 4 (yellow)
      count: 2
      positions: [[0,1], [2,1]]
    - color: 9 (maroon)
      count: 1
      positions: [[0,3]]
    - color: 6 (magenta)
      count: 1
      positions: [[2,2]]
    - color: 1 (blue)
      count: 1
      positions: [[3,0]]

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      positions: [[0,0], [0,1], [0,2], [0,3], [1,0], [1,1], [1,2], [1,3], [2,0], [2,2],[2,3]]
    - color: 4 (yellow)
      count: 2
      positions: [[3,1], [2,1]]
    - color: 9 (maroon)
      count: 1
      positions: [[3,3]]
    - color: 6 (magenta)
      count: 1
      positions: [[3,2]]
    - color: 1 (blue)
      count: 1
      positions: [[3,0]]
```

**Natural Language Program (Transformation Rule):**

1.  **Identify non-zero colored objects:** Locate all cells in the input grid that have a color other than 0 (white).
2.  **Move Identified objects:** Move the non-zero cells to the last row of the grid.
3.  **Preserve the bottom-up and left-right relative order**: When multiple non-zero colored objects are in a column they appear in the output following a bottom-up order and in case of objects in the same row they appear in the left to right order.

In summary, the transformation involves shifting all non-zero colored cells to the last row, while maintaining the bottom-up order for objects in the same column and preserving the left-right order for objects that were in the same row. The rest of the grid is filled with zeros.

```python
"""
Shifts all non-zero colored cells to the last row, maintaining their original order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the last row,
    maintaining their relative order, and filling the rest with zeros.

    Args:
    input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
    list of lists: The transformed grid.
    """
    # Initialize output_grid with zeros
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    # Find non-zero elements and their original positions
    non_zero_elements = []
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != 0:
                non_zero_elements.append((input_grid[i][j], i, j))  # Store value, original row, and original column

    # Sort based on the described logic. The primary key for sorting will be the original row in reverse (bottom up).
    #secondary sort key is the original col (left-to-right).

    non_zero_elements.sort(key=lambda x: ( -x[1], x[2]))

    # Place non-zero elements in the last row of output_grid
    last_row_index = 0
    for element in non_zero_elements:
        output_grid[rows - 1][last_row_index] = element[0]
        last_row_index += 1

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

<PIL.Image.Image image mode=RGB size=384x384 at 0x7A151BB0F340>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7A151BAEA5C0>
Okay, let's analyze the transformation from the input grid to the output grid in this second example.

**Observations in YAML format:**

```yaml
input_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      positions: (Too many to list individually, covers most of the grid except for the colored cells)
    - color: 9 (maroon)
      count: 1
      positions: [[0,5]]
    - color: 8 (azure)
      count: 2
      positions: [[1,3], [4,3]]
    - color: 4 (yellow)
      count: 3
      positions: [[3,0], [4,0], [5,0]]
    - color: 7 (orange)
      count: 2
      positions: [[4,2], [5,2]]

output_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 29
      positions: (Too many to list, covers most of the grid)
    - color: 9 (maroon)
      count: 1
      positions: [[5,5]]
    - color: 8 (azure)
      count: 2
      positions: [[5,3], [4,3]]
   - color: 4 (yellow)
      count: 3
      positions: [[3,0], [4,0], [5,0]]
    - color: 7 (orange)
      count: 2
      positions: [[4,2], [5,2]]

```

**Natural Language Program (Transformation Rule):**

1.  **Identify non-zero colored objects:** Locate all cells in the input grid that have a color other than 0 (white).

2.  **Move identified objects**: Move all non-zero colored objects towards the bottom of the grid.

3. **Preserve row and column**: The objects are moved preserving their column and relative row order.
   Objects in the same column maintain their relative vertical order.

In summary, the transformation involves moving all non-zero colored cells to the bottom-most available position within their respective columns, maintaining the original vertical order within each column. The remaining cells are filled with zeros.

```python
import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the bottom-most
    available position in their respective columns, maintaining their original
    vertical order.

    Args:
    input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
    list of lists: The transformed grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    for j in range(cols):
        # Collect non-zero elements from the current column
        non_zero_elements = []
        for i in range(rows):
            if input_grid[i][j] != 0:
                non_zero_elements.append(input_grid[i][j])

        # Place non-zero elements at the bottom of the column in output_grid
        for i in range(len(non_zero_elements)):
            output_grid[rows - len(non_zero_elements) + i][j] = non_zero_elements[i]

    return output_grid
```
The previous code and natural language program accurately describe and performs the column-wise shifting of non-zero elements to the bottom.

```python
"""
Moves all non-zero colored objects towards the bottom of the grid, preserving their column and relative row order. Objects in the same column maintain their relative vertical order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero elements to the bottom-most
    available position in their respective columns, maintaining their original
    vertical order.

    Args:
    input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
    list of lists: The transformed grid.
    """
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = [[0] * cols for _ in range(rows)]

    for j in range(cols):
        # Collect non-zero elements from the current column
        non_zero_elements = []
        for i in range(rows):
            if input_grid[i][j] != 0:
                non_zero_elements.append(input_grid[i][j])

        # Place non-zero elements at the bottom of the column in output_grid
        for i in range(len(non_zero_elements)):
            output_grid[rows - len(non_zero_elements) + i][j] = non_zero_elements[i]

    return output_grid
```


**input**
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7A151BAEAA40>

**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7A151BAEA620>
Okay, let's analyze the transformation from the input grid to the output grid in this third example.

**Observations in YAML format:**

```yaml
input_grid:
  size: 5x5
  objects:
    - color: 0 (white)
      count: 19
    - color: 1 (blue)
      count: 2
      positions: [[0, 3], [2, 3]]
    - color: 3 (green)
      count: 3
      positions: [[1, 1], [2, 1], [4, 1]]
    - color: 2 (red)
      count: 1
      positions: [[2, 4]]
    - color: 6 (magenta)
      count: 1
      positions: [[3, 0]]

output_grid:
  size: 5x5
  objects:
    - color: 0 (white)
      count: 17
    - color: 1 (blue)
      count: 2
      positions: [[3, 3], [4, 3]]
    - color: 3 (green)
      count: 3
      positions: [[2, 1], [3, 1], [4, 1]]
    - color: 2 (red)
      count: 1
      positions: [[4, 4]]
    - color: 6 (magenta)
      count: 1
      positions: [[4, 0]]
```

**Natural Language Program (Transformation Rule):**

1.  **Identify non-zero colored objects:** Find all cells in the input grid that have a color other than 0 (white).
2.  **Move identified object**: Move the identified objects to the bottom of the grid.
3.  **Preserve column and order:** Preserve the column and relative order of the object.
   Objects in the same column maintain their relative vertical order, filling the grid from the bottom up.

The transformation rule is the same as in the second example. The code is correct.

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
