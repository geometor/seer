# 00d62c1b • 028 • refine_coder

---
```python
"""
The input is a grid of pixels. Each pixel has a color value of 0 (white) or 3 (green).
Identify green (3) pixels that are part of a 2x2 block of green (3) pixels which share at least one side and/or at least one corner.
Change the color value of the identified "internal" or "surrounded" green (3) pixels from green (3) to yellow (4).
Ensure all other pixels, those colored white, and those green pixels not part of an identified "internal" block retain their original values.
The output is a grid with the same dimensions as the input, but with the specified color changes applied.
"""

import numpy as np

def get_all_neighbors(grid, row, col):
    """
    Returns a list of all neighbors (including diagonals) of a given cell.
    """
    rows, cols = grid.shape
    neighbors = []
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  # Skip the cell itself
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                neighbors.append((r, c))
                
    return neighbors

def is_part_of_2x2(grid, row, col, neighbors):
    """
        Checks if a cell and 3 of its neighbors form a 2x2 green block
    """
    if grid[row,col] != 3:
        return False

    green_neighbors = [(r,c) for r,c in neighbors if grid[r,c] == 3]
    
    for r1, c1 in green_neighbors:
      for r2, c2 in green_neighbors:
          if (r1,c1) != (r2, c2): # different neighbors
             for r3,c3 in green_neighbors:
                if (r3,c3) != (r1,c1) and (r3,c3) != (r2,c2): # different neighbors
                    # Check if they form a 2x2 block
                    if (abs(row - r1) <= 1 and abs(col - c1) <= 1) and \
                       (abs(row - r2) <= 1 and abs(col - c2) <= 1) and \
                       (abs(row - r3) <= 1 and abs(col - c3) <= 1) and \
                       (abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1) and \
                       (abs(r1 - r3) <= 1 and abs(c1 - c3) <= 1) and \
                       (abs(r2 - r3) <= 1 and abs(c2 - c3) <= 1):
                         return True
    return False


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels 
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 3:
                neighbors = get_all_neighbors(input_grid, row, col)
                if is_part_of_2x2(input_grid,row, col, neighbors):
                    output_grid[row,col] = 4

    return output_grid
```
