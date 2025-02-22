# 3-1e0a9b12 • 004 • example_2 - CODE

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

**YAML Block Observation**

```yaml
observations:
  input_grid:
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

  output_grid:
    size: 4x4
    objects:
      - color: 0 (white)
        count: 12
        shape: background
      - color: 4 (yellow)
        count: 1
        shape: isolated cell
        position: [2,1]
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

1.  **Identify Objects:** The input grid consists of isolated cells of colors 1 (blue), 4 (yellow), 6 (magenta), and 9 (maroon) against a background of color 0 (white).

2.  **Predicate:** The non-white cells maintain their colors.

3. **Action:** Move the colored cells to the bottom row, maintaining the x value, stacking the cells in order from bottom to top, keeping the original colors.

**Transformation Rule Summary**
The transformation moves all non-zero colored cells to the last row available, keeping their original colors. The colored objects do not change color, they are just translated.

```python
"""
The transformation moves all non-zero colored cells to the last row available, keeping their original colors. The colored objects do not change color, they are just translated.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero colored cells to the
    last row available, preserving their original x-coordinates and colors.
    """
    # Initialize the output grid as a copy of the input grid with all zeros.
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Create a dictionary to store the next available row index for each column.
    next_available_row = {col: rows - 1 for col in range(cols)}

    # Iterate through the input grid to find and move non-zero cells.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Get the color of the current cell.
                color = input_grid[r, c]
                # Get the next available row index for the current column.
                row_index = next_available_row[c]
                # Place the cell in the output grid.
                output_grid[row_index, c] = color
                # Update the next available row index for this column.
                next_available_row[c] -= 1

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

![Image](003-example_2_input.png)


**output**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```

![Image](003-example_2_output.png)

Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block Observation**

```yaml
observations:
  input_grid:
    size: 6x6
    objects:
      - color: 0 (white)
        count: 28
        shape: background
      - color: 4 (yellow)
        count: 3
        shape: vertical line
        positions: [[3,0], [4,0], [5,0]]
      - color: 7 (orange)
        count: 2
        shape: vertical line
        positions: [[4,2], [5,2]]
      - color: 8 (azure)
        count: 2
        shape: isolated cells
        positions: [[1,3], [4,3]]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [[0,5]]

  output_grid:
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
        positions: [[4,2], [5,2]]
      - color: 8 (azure)
        count: 2
        shape: vertical line
        positions: [[4,3],[5,3]]
      - color: 9 (maroon)
        count: 1
        shape: isolated cell
        position: [[5,5]]
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** The input grid consists of a vertical line of yellow (4), two vertical lines of orange (7) and azure (8), and an isolated cell maroon(9).

2.  **Predicate:** The non-white cells maintain their original colors.

3.  **Action**:
    *   Translate vertically the azure object, to occupy the lowest available position.

    *    Other colored cells remain in their places.

**Transformation Rule Summary**
The transformation moves all non-zero colored cells to the last row available, keeping their original colors and x-coordinates.
The previous python program is enough to produce the right output.

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
