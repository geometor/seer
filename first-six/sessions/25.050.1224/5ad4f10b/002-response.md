# 5ad4f10b • 002 • example_1 - CODE

---
```python
"""
The transformation extracts all azure (8) colored cells from the input grid.
Then determines if the adjecent cells are 0 or 4.
Forms an output using only the selected azure cells.
If adjacent to 0, the output is 0. If adjacent to 4, the output is 8.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the neighbors of a cell, including diagonals."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbor_row, neighbor_col = row + i, col + j
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                neighbors.append(grid[neighbor_row, neighbor_col])
    return neighbors

def transform(input_grid):
    """Transforms the input grid to the output grid based on the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)

    # Find coordinates of azure (8) cells.
    azure_coords = np.argwhere(input_grid == 8)
    
    # Create dict of azure coordinates
    azure_dict = {}
    for r, c in azure_coords:
      neighbors = get_neighbors(input_grid, r, c)
      azure_dict[(r,c)] = neighbors

    # Select coordinates of azure (8) cells for 3x3 grid, based on the yellow (4)
    # and white (0) adjacencies.
    output_coords = []

    for (r,c), neighbors in azure_dict.items():
      is_valid = False
      for neighbor in neighbors:
        if neighbor == 0:
          output_coords.append((r, c, 0)) # add white
          is_valid = True
          break
        elif neighbor == 4:
          is_valid = True
          break
      if is_valid:
        output_coords.append((r, c, 8)) # add azure

    # Place azure and white pixels in output, based on the input selection
    output_row = 0
    output_col = 0
    for r,c, color in output_coords:
      if output_col > 2:
        output_col = 0
        output_row +=1
      if output_row > 2:
        break
      if color == 8:
        all_zeros = True
        for neighbor in azure_dict[(r,c)]:
          if neighbor != 0:
            all_zeros = False
            break
        if all_zeros:
          output_grid[output_row,output_col] = 0
        else:
          output_grid[output_row,output_col] = 8
      else:
          output_grid[output_row,output_col] = 0

      output_col += 1

    return output_grid
```
