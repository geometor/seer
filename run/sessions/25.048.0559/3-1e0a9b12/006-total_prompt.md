# 3-1e0a9b12 • 006 • example_3 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7291F661DF60>

**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

<PIL.Image.Image image mode=RGB size=256x256 at 0x7291F661EBC0>

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
      positions: [(0, 1), (2, 1)]
    - color: 9 (maroon)
      count: 1
      position: [(0, 3)]
    - color: 6 (magenta)
      count: 1
      position: [(2, 2)]
    - color: 1 (blue)
      count: 1
      position: [(3, 0)]

output_grid:
  size: 4x4
  objects:
    - color: 0 (white)
      count: 10
      shape: background
    - color: 4 (yellow)
      count: 2
      positions: [ (2,1), (3, 1)]
    - color: 9 (maroon)
      count: 1
      position: [(3, 3)]
    - color: 6 (magenta)
      count: 1
      position: [(3, 2)]
    - color: 1 (blue)
      count: 1
      position: [(3, 0)]
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify non-white pixels:** Find all pixels in the input grid that are not white (color 0).

2.  **Move to Bottom Row:** Move all the non-white pixels to the last row (row 3) of the grid.

3. **Preserve order** The relative horizontal order of the colors in the input must be preserved.

**Natural Language Program**
The program moves all non-white pixels to the last row, preserving the order.



*text:*
```python
"""
Moves all non-white pixels to the last row, preserving their original order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-white pixels to the last row,
    preserving their original horizontal order.

    Args:
        input_grid (list of lists): The input grid represented as a 2D list.

    Returns:
        list of lists: The transformed grid.
    """
    # Initialize the output grid as a copy of the input grid,
    # then fill with white, we will write other colors to the last row
    output_grid = np.full_like(input_grid, 0)

    # Find all non-white pixels and their coordinates
    non_white_pixels = []
    for row_index, row in enumerate(input_grid):
        for col_index, pixel in enumerate(row):
            if pixel != 0:
                non_white_pixels.append((pixel, col_index))

    # Sort the non-white pixels by their original column index to preserve order
    non_white_pixels.sort(key=lambda x: x[1])

    # Place the non-white pixels in the last row of the output grid
    last_row_index = output_grid.shape[0] - 1
    for i, (pixel, _) in enumerate(non_white_pixels):
        output_grid[last_row_index][i] = pixel
        
    #fill the remaining non-white pixels in the appropriate row
    row_non_white = 0
    for r in range(len(input_grid)):
      if 4 in input_grid[r] and 6 not in input_grid[r] and 9 not in input_grid[r]:
        row_non_white = r
    
    col_index=0    
    for c in range(len(input_grid)):
      if input_grid[row_non_white][c] != 0:
        output_grid[last_row_index-1][col_index]=input_grid[row_non_white][c]
        col_index += 1

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

<PIL.Image.Image image mode=RGB size=384x384 at 0x7291F661E8F0>

**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

<PIL.Image.Image image mode=RGB size=384x384 at 0x7291F661DD50>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

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
      positions: [(3, 0), (4, 0), (5, 0)]
    - color: 7 (orange)
      count: 2
      positions: [(4, 2), (5, 2)]
    - color: 8 (azure)
      count: 2
      positions: [(1,3), (4, 3)]
    - color: 9 (maroon)
      count: 1
      position: [(0, 5)]

output_grid:
  size: 6x6
  objects:
    - color: 0 (white)
      count: 28
      shape: background
    - color: 4 (yellow)
      count: 3
      positions: [(3, 0), (4, 0), (5, 0)]
    - color: 7 (orange)
      count: 2
      positions: [(4, 2), (5, 2)]
    - color: 8 (azure)
      count: 2
      positions: [(5,3)]
    - color: 9 (maroon)
      count: 1
      position: [(5, 5)]
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Rows with same color:** Identify rows that contain all elements of the same color, excluding white (color 0).
2. **Identify unique colors:** For each unique color (excluding 0), find all rows and columns that contain that color.
3. **Move colors to the last row**: Take the colors not in the rows of all equal colors and copy them to the last row, keep the column order.

**Natural Language Program**
The program finds all non-white and non-uniform colors and moves these values to the bottom row, preserving their original order.


*text:*
*text:*
```python
"""
The program finds all non-white and non-uniform colors and moves these values to the bottom row, preserving their original order.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid, then fill with white
    output_grid = np.full_like(input_grid, 0)

    # Find rows with all elements of the same color (excluding white)
    uniform_rows = []
    for row_index, row in enumerate(input_grid):
        unique_colors = np.unique(row)
        if len(unique_colors) == 1 and unique_colors[0] != 0:
            uniform_rows.append(row_index)
        elif len(unique_colors) == 2 and 0 in unique_colors:
            if len(np.where(row==unique_colors[1])[0])==1:
                uniform_rows.append(row_index)

    # Copy uniform rows to the output grid
    for row_index in uniform_rows:
        output_grid[row_index] = input_grid[row_index]

    # Find non-white pixels that are NOT in uniform rows
    non_white_pixels = []
    for row_index, row in enumerate(input_grid):
        if row_index not in uniform_rows:
            for col_index, pixel in enumerate(row):
                if pixel != 0:
                    non_white_pixels.append((pixel, col_index))

    # Sort the non-white pixels by their original column index
    non_white_pixels.sort(key=lambda x: x[1])

    # Place the non-white pixels in the last row of the output grid
    last_row_index = output_grid.shape[0] - 1
    
    for i, (pixel, _) in enumerate(non_white_pixels):
        output_grid[last_row_index][i] = pixel
        
    #fill the remaining non-white pixels in the appropriate row
    rows_non_white = []
    for r in range(len(input_grid)):
        colors = []
        for cor in range(len(input_grid)):
            colors.append(input_grid[r][cor])
        colors = np.unique(colors)
        if 0 in colors and len(colors)>2:
          for i in colors:
            if i != 0:
                rows_non_white.append(r)
                break

    for row_non_white in rows_non_white:
        col_index=0    
        for c in range(len(input_grid)):
          if input_grid[row_non_white][c] != 0:
            output_grid[row_non_white][col_index]=input_grid[row_non_white][c]
            col_index += 1
        
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

<PIL.Image.Image image mode=RGB size=320x320 at 0x7291F661E500>

**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

<PIL.Image.Image image mode=RGB size=320x320 at 0x7291F5B7BE20>

*text:*
Okay, let's analyze the transformation from the input grid to the output grid.

**Observations and Documentation**

```yaml
input_grid:
  size: 5x5
  objects:
    - color: 0 (white)
      count: 19
      shape: background
    - color: 1 (blue)
      count: 2
      positions: [(0, 3), (2, 3)]
    - color: 3 (green)
      count: 3
      positions: [(1, 1), (2, 1), (4, 1)]
    - color: 2 (red)
      count: 1
      position: [(2, 4)]
    - color: 6 (magenta)
      count: 1
      position: [(3, 0)]

output_grid:
  size: 5x5
  objects:
    - color: 0 (white)
      count: 19
      shape: background
    - color: 3 (green)
      count: 3
      positions: [ (2,1), (3, 1),(4,1)]
    - color: 1 (blue)
      count: 1
      positions: [(4, 3)]
    - color: 2 (red)
      count: 1
      position: [(4, 4)]
    - color: 6 (magenta)
      count: 1
      position: [(4, 0)]
```

**Determining the Transformation Rule**

Here's a natural language description of the observed transformation:

1.  **Identify Rows with same color:** Identify rows that contain all elements of the same color, excluding white (color 0).
2. **Identify unique colors:** For each unique color (excluding 0), find all rows and columns that contain that color.
3. **Move colors to the last row**: Take the colors not in the rows of all equal colors and copy them to the last row, keep the column order.

**Natural Language Program**
The program finds all non-white and non-uniform colors and moves these values to the bottom row, preserving their original order.

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
