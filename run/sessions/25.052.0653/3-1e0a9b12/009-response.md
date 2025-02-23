# 3-1e0a9b12 • 009 • example_3 - NLP

---
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

