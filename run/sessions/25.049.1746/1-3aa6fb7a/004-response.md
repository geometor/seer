# 1-3aa6fb7a • 004 • example_2 - CODE

---

*text:*

```python
"""
The transformation rule identifies single-pixel azure (color 8) objects in the input grid. For each identified azure pixel, the adjacent pixel in the clockwise direction (starting from the top: top, right, bottom, left) is changed to blue (color 1).
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Returns a dictionary of neighbor coordinates (top, right, bottom, left) for a given cell.
    Out-of-bounds neighbors are not included.
    """
    rows, cols = grid.shape
    neighbors = {}
    if row > 0:
        neighbors['top'] = (row - 1, col)
    if col < cols - 1:
        neighbors['right'] = (row, col + 1)
    if row < rows - 1:
        neighbors['bottom'] = (row + 1, col)
    if col > 0:
        neighbors['left'] = (row, col - 1)
    return neighbors
  

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for row in range(rows):
        for col in range(cols):
            # Check if the current cell is azure (color 8)
            if input_grid[row, col] == 8:
                # Get the neighbors
                neighbors = get_neighbors(input_grid,row,col)

                is_single = True
                for direction, coord in neighbors.items():
                  if input_grid[coord] == 8:
                    is_single = False
                    break

                if is_single:
                  # one position clockwise
                  if 'top' in neighbors:
                      output_grid[neighbors['top']] = 1
                  elif 'right' in neighbors:
                    output_grid[neighbors['right']] = 1
                  elif 'bottom' in neighbors:
                    output_grid[neighbors['bottom']] = 1
                  elif 'left' in neighbors:
                    output_grid[neighbors['left']] = 1


    return output_grid
```

