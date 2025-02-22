# 3-1e0a9b12 • 010 • example_3 - CODE

---

**input**
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```

![Image](001-example_1_input.png)


**output**
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```

![Image](001-example_1_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Summary**

```yaml
observations:
  - input_grid:
      size: 4x4
      objects:
        - color: 0 (white)
          count: 11
          shape: background
        - color: 4 (yellow)
          count: 2
          shape: isolated cells
          positions: [0,1], [2,1]
        - color: 9 (maroon)
          count: 1
          shape: isolated cell
          position: [0,3]
        - color: 6 (magenta)
          count: 1
          shape: isolated cell
          position: [2,2]
        - color: 1 (blue)
          count: 1
          shape: isolated cell
          position: [3,0]
  - output_grid:
      size: 4x4
      objects:
        - color: 0 (white)
          count: 12
          shape: background
        - color: 4 (yellow)
          count: 1
          shape: isolated cells
          positions: [2,1]
        - color: 9 (maroon)
          count: 1
          shape: isolated cell
          position: [3,3]
        - color: 6 (magenta)
          count: 1
          shape: isolated cell
          position: [3,2]
        - color: 1 (blue)
          count: 1
          shape: isolated cell
          position: [3,0]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of single-cell colored objects (1, 4, 6, 9) on a white (0) background.

2.  **Shift Non-Zero Objects Down:** All non-zero colored objects are moved to the last row of the grid.

3.  **Preserve Order if Possible:**
    - The blue object (1) stays in the first column (index 0).
    - The yellow object at the original position [0,1] disappears.
    - The yellow object that was at [2,1] moves to the last row, keeping its horizontal position [3,1].
    - The magenta object (6) moves down to the last row [3,2].
    - The maroon object (9) moves down to the last row [3,3].

4. **Whites stay as background**

In essence, all the non-white single-cell objects move to the last row, maintaining their relative horizontal order, except the yellow object in the first row.

```python
"""
Moves all non-zero single-cell objects to the last row of the grid,
maintaining their relative horizontal order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored objects to the last row.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid).tolist()
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Create an empty last row for the output grid
    last_row = [0] * cols

    # Find and move non-zero objects
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                # Check to see if it isn't part of a larger object:
                is_single = True
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 <= r+i < rows and 0 <= c+j < cols:
                            if (i!=0 or j!=0) and input_grid[r+i,c+j] == input_grid[r,c]:
                                is_single = False
                                break
                    if not is_single:
                        break
                #if the object is single, we can move it
                if is_single:
                    last_row[c] = input_grid[r, c]
                    #clear initial position only if it's not in the last row already:
                    if r != rows-1:
                        output_grid[r][c] = 0


    # Replace the last row of the output grid with the new last row
    output_grid[rows - 1] = last_row

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

![Image](005-example_2_input.png)


**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

![Image](005-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid in the second example.

**YAML Block Summary**

```yaml
observations:
  - input_grid:
      size: 6x6
      objects:
        - color: 0 (white)
          count: 28
          shape: background
        - color: 9 (maroon)
          count: 1
          shape: isolated cell
          position: [0,5]
        - color: 8 (azure)
          count: 1
          shape: isolated cells
          positions: [1,3]
        - color: 4 (yellow)
          count: 3
          shape: vertical line
          positions: [[3,0], [4,0], [5,0]]
        - color: 7 (orange)
          count: 2
          shape: vertical line
          position: [[4,2], [5,2]]
        - color: 8 (azure)
          count: 1
          shape: isolated cell
          position: [4,3]
  - output_grid:
      size: 6x6
      objects:
        - color: 0 (white)
          count: 27
          shape: background
        - color: 4 (yellow)
          count: 3
          shape: vertical line
          positions: [[3,0], [4,0], [5,0]]
        - color: 7 (orange)
          count: 2
          shape: vertical line
          position: [[4,2], [5,2]]
        - color: 8 (azure)
          count: 1
          shape: isolated cell
          position: [5,3]
        - color: 9 (maroon)
          count: 1
          shape: isolated cell
          position: [5,5]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of various objects: a vertical line of yellow (4), a vertical line of orange (7), and single cells of azure (8) and maroon (9).

2.  **Move to last row single-colored objects:**
    Azure object and maroon objects move to the last row. Azure in the input was at position \[1,3] and now it keeps it horizontal position but in the last row \[5,3]. Something similar happens with maroon object. It moves from \[0,5] to \[5,5].

3.  **Preserve Other Objects:**
    Objects formed by more than one pixel are preserved, such as vertical lines of yellow (4) and orange (7)
   
4.  **White remains as background.**
    
In essence, the single-cell objects move to the last row, maintaining their horizontal position.

```python
"""
Moves all non-zero single-cell objects to the last row of the grid,
maintaining their relative horizontal order.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored objects to the last row.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid).tolist()
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Create an empty last row for the output grid
    last_row = [0] * cols

    # Find and move non-zero objects
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                # Check to see if it isn't part of a larger object:
                is_single = True
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 <= r+i < rows and 0 <= c+j < cols:
                            if (i!=0 or j!=0) and input_grid[r+i,c+j] == input_grid[r,c]:
                                is_single = False
                                break
                    if not is_single:
                        break
                #if the object is single, we can move it
                if is_single:
                    last_row[c] = input_grid[r, c]
                    #clear initial position only if it's not in the last row already:
                    if r != rows-1:
                        output_grid[r][c] = 0


    # Replace the last row of the output grid with the new last row
    output_grid[rows - 1] = last_row

    return output_grid
```

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Summary**

```yaml
observations:
  - input_grid:
      size: 3x3
      objects:
        - color: 0 (white)
          count: 7
          shape: background
        - color: 5 (gray)
          count: 2
          shape: diagonal line
          positions: [0,0], [1,1]
  - output_grid:
      size: 3x3
      objects:
        - color: 0 (white)
          count: 7
          shape: background
        - color: 5 (gray)
          count: 2
          shape: diagonal line
          positions: [1,1], [2,2]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid has two gray (5) colored cells forming a diagonal line, and the rest is white (0).

2.  **Shift Diagonal Down-Right:** The diagonal line of gray cells is shifted down and to the right by one cell.

3. **Whites stay as background.**

```python
"""
Shifts a diagonal line of gray cells down and to the right by one cell.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by shifting the diagonal line of gray cells.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # Find the diagonal and shift it
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 5:
                if r + 1 < rows and c + 1 < cols:
                    output_grid[r + 1, c + 1] = 5

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

![Image](009-example_3_input.png)


**output**
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```

![Image](009-example_3_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Summary**

```yaml
observations:
  - input_grid:
      size: 5x5
      objects:
        - color: 0 (white)
          count: 20
          shape: background
        - color: 1 (blue)
          count: 2
          shape: isolated cells
          positions: [0,3], [2,3]
        - color: 3 (green)
          count: 3
          shape: vertical line of isolated cells
          positions: [1,1], [2,1], [4,1]
        - color: 2 (red)
          count: 1
          shape: isolated cell
          position: [2,4]
        - color: 6 (magenta)
          count: 1
          shape: isolated cell
          position: [3,0]
  - output_grid:
      size: 5x5
      objects:
        - color: 0 (white)
          count: 19
          shape: background
        - color: 3 (green)
          count: 2
          shape: vertical line
          positions: [2,1], [3,1]
        - color: 1 (blue)
          count: 1
          shape: isolated cells
          positions: [4,3]
        - color: 2 (red)
          count: 1
          shape: isolated cell
          position: [4,4]
        - color: 6 (magenta)
          count: 1
          shape: isolated cell
          position: [4,0]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of single-cell colored objects (1, 2, 6) on a white (0) background. The input grid also consists of a vertical line of green (3) color.

2.  **Shift Non-Zero Single Objects Down:** All non-zero colored single objects are moved to the last row of the grid.

3.  **Preserve Green Objects and move them:**
    - The green objects (3) are preserved but the one in the input that was on the position [4,1] is removed and the other two, are moved down by one cell.

4. **Whites stay as background**

In essence, all the non-white and non-green single-cell objects move to the last row, maintaining their relative horizontal order. The green objects, move down by one cell except the last one that disappears.

```python
"""
Moves all non-zero single-cell objects to the last row of the grid,
maintaining their relative horizontal order. Green objects move down.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving non-zero colored objects to the last row.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid).tolist()
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Create an empty last row for the output grid
    last_row = [0] * cols

    # Find and move non-zero objects
    for c in range(cols):
        for r in range(rows):
            if input_grid[r, c] != 0:
                # Check to see if it isn't part of a larger object:
                is_single = True
                for i in range(-1,2):
                    for j in range(-1,2):
                        if 0 <= r+i < rows and 0 <= c+j < cols:
                            if (i!=0 or j!=0) and input_grid[r+i,c+j] == input_grid[r,c]:
                                is_single = False
                                break
                    if not is_single:
                        break
                #if the object is single, we can move it
                if is_single:
                    if input_grid[r,c] != 3:
                        last_row[c] = input_grid[r, c]
                        #clear initial position only if it's not in the last row already:
                        if r != rows-1:
                            output_grid[r][c] = 0
                    else:
                        if r+1 < rows and input_grid[r+1,c] != 3:
                            output_grid[r+1][c] = 3
                            output_grid[r][c] = 0


    # Replace the last row of the output grid with the new last row
    output_grid[rows - 1] = last_row

    return output_grid
```

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
