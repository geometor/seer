# 5ad4f10b • 006 • example_3 - CODE

---
```python
"""
The transformation extracts all green (3) colored cells from the input grid.
Then determines if the adjacent cells are 0 or 6.
Forms an output using only the selected green cells.
If adjacent to 0, the output might be 0. If adjacent to 6, the output is 3.
If all adjacent cells are 0, the output is 0.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets all 8 neighbors (including diagonals) of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            neighbor_row, neighbor_col = row + i, col + j
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                neighbors.append(grid[neighbor_row, neighbor_col])
    return neighbors

def find_target_color(output_grid):
    """Determines the target color from the output grid."""
    unique_colors = np.unique(output_grid)
    target_color = unique_colors[unique_colors != 0]
    if len(target_color)>0:
      return target_color[0]  # Return the first non-zero color
    else:
      return 0

def transform(input_grid):
    """Transforms the input grid based on the generalized rule."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)  # Initialize 3x3 output
    
    # Find target
    target_color = find_target_color(output_grid)

    # Find coordinates of the target color in the input grid.
    target_coords = np.argwhere(input_grid == target_color)
    if len(target_coords)==0:
        return output_grid

    target_coords_dict = {}
    for r, c in target_coords:
      neighbors = get_neighbors(input_grid, r, c)
      target_coords_dict[(r,c)] = neighbors

    # Prioritize target cells with at least one background neighbor.
    output_coords = []
    for (r,c), neighbors in target_coords_dict.items():
      is_valid = False
      for neighbor in neighbors:
        if neighbor == 0:
          output_coords.append((r, c, 0)) # add white
          is_valid = True
          break
        
      if not is_valid:
        output_coords.append((r, c, target_color)) # add target
    
    # Fill the output grid.
    output_row = 0
    output_col = 0
    for r, c, color in output_coords:
      if output_col > 2:
        output_col = 0
        output_row +=1
      if output_row > 2:
        break
      if color == target_color:
        all_zeros = True
        for neighbor in target_coords_dict[(r,c)]:
          if neighbor != 0:
            all_zeros = False
            break
        if all_zeros:
          output_grid[output_row,output_col] = 0
        else:
          output_grid[output_row,output_col] = target_color
      else:
          output_grid[output_row,output_col] = 0

      output_col += 1

    return output_grid
```

