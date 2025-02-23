# 3-1e0a9b12 • 005 • example_3 - NLP

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x720C51F12320>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x720C51F12D40>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      positions: (0,1), (2,1)
    - color: 9 (maroon)
      count: 1
      position: (0,3)
    - color: 6 (magenta)
      count: 1
      position: (2,2)
    - color: 1 (blue)
      count: 1
      position: (3,0)

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 11
      shape: background
    - color: 4 (yellow)
      count: 2
      shape: L-shape
      positions: (3, 1) (2,1)
    - color: 9 (maroon)
      count: 1
      position: (3,3)
    - color: 6 (magenta)
      count: 1
      position: (3,2)
    - color: 1 (blue)
      count: 1
      position: (3,0)
```

**Determining the Transformation Rule**

Here's a natural language description of the transformation:

1.  **Identify Non-Background Objects:** Locate all the colored cells (non-zero values) within the input grid.

2.  **Move Objects:** Move all identified non-background objects to the last row of the grid.

3. **Preserve Order:** Maintain the horizontal order of the objects as they appear from left to right in their original positions in the input.

**Natural Language Program**
```
Collect all non-background colored cells.
Move all of them to the last row.
Preserve the relative order of appearance from left to right.
```


*text:*
```python
"""
Collect all non-background colored cells.
Move all of them to the last row.
Preserve the relative order of appearance from left to right.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the last row,
    preserving their original left-to-right order.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero (non-background) elements and their coordinates
    non_zero_elements = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_elements.append((input_grid[r, c], c))

    # Sort the non-zero elements based on their original column position (left-to-right)
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the non-zero elements in the last row of the output grid
    last_row_index = 0
    for value, _ in non_zero_elements:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1
    
    # copy elements from the last row of input if background
    for c in range(cols):
        if input_grid[rows-1,c]!=0 and output_grid[rows-1,c]==0:
           for r in range(rows-1,-1,-1):
              if input_grid[r,c]!=0:
                output_grid[rows-1,c]=input_grid[r,c]
                break
                

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

<PIL.Image.Image image mode=RGB size=384x384 at 0x720C51F126E0>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x720C51F13BB0>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**Observations and Documentation**

```yaml
input_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      shape: background
    - color: 4 (yellow)
      count: 3
      positions: (3,0), (4,0), (5,0)
    - color: 7 (orange)
      count: 2
      positions: (4,2), (5,2)
    - color: 8 (azure)
      count: 2
      positions: (1,3), (4,3)
    - color: 9 (maroon)
      count: 1
      position: (0,5)

output_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      shape: background
    - color: 4 (yellow)
      count: 3
      positions: (3,0), (4,0), (5,0)
    - color: 7 (orange)
      count: 2
      positions: (4,2), (5,2)
    - color: 8 (azure)
      count: 2
      positions: (4,3), (5,3)
    - color: 9 (maroon)
      count: 1
      position: (5,5)
```

**Determining the Transformation Rule**

The transformation rule observed in this example is slightly different, but conceptually similar to the first:

1.  **Identify Non-Background Objects:** Start by identifying all non-zero (colored) cells in the input grid.

2. **Copy Objects:** The key idea is Copy.

3. **Preserve Order:** Maintain the order.

**Natural Language Program**

```
Copy all non-background colored cells from each row to the last row.
```

```python
"""
Copy all non-background colored cells from each row to the last row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the last row,
    preserving their original left-to-right order.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero (non-background) elements and their coordinates
    non_zero_elements = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_elements.append((input_grid[r, c], c))

    # Sort the non-zero elements based on their original column position (left-to-right)
    non_zero_elements.sort(key=lambda x: x[1])

    # Place the non-zero elements in the last row of the output grid
    last_row_index = 0
    for value, _ in non_zero_elements:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1
    
    # copy elements from the last row of input if background
    for c in range(cols):
        if input_grid[rows-1,c]!=0 and output_grid[rows-1,c]==0:
           for r in range(rows-1,-1,-1):
              if input_grid[r,c]!=0:
                output_grid[rows-1,c]=input_grid[r,c]
                break
                

    return output_grid.tolist()
```
The provided code already captures correctly the logic of "moving to the last row," I refined the code to be more general. The core idea is that we are identifying the colored cells and collecting to the last row.


*text:*
```python
"""
Copy all non-background colored cells from each row to the last row,
preserving their relative order within each row and across the grid.
"""

import numpy as np

def find_non_background_cells(grid):
    """
    Finds all non-background (non-zero) cells in the grid.
    Returns a list of tuples: (row, col, value).
    """
    non_background_cells = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != 0:
                non_background_cells.append((r, c, grid[r][c]))
    return non_background_cells

def transform(input_grid):
    """
    Transforms the input grid by copying all non-zero colored cells to the last row,
    preserving their original left-to-right order, then copying any pre-existing
    non-zero elements on last row.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero elements.
    non_zero_elements = find_non_background_cells(input_grid)

    # Sort non-zero elements by column then by row.
    non_zero_elements.sort(key=lambda x: (x[1], x[0]))


    # Place the sorted non-zero elements in the last row.
    last_row_index = 0
    for _, _, value in non_zero_elements:
        output_grid[rows - 1, last_row_index] = value
        last_row_index += 1
    
    # copy elements from the last row of input if background at that place
    for c in range(cols):
        if input_grid[rows-1,c]!=0 and output_grid[rows-1,c]==0:
           for r in range(rows-1,-1,-1):
              if input_grid[r,c]!=0:
                output_grid[rows-1,c]=input_grid[r,c]
                break

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

<PIL.Image.Image image mode=RGB size=320x320 at 0x720C51F124D0>

**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x720C51EEF280>
**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
