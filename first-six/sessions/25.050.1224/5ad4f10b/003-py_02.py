"""
The transformation extracts all red (2) colored cells from the input grid.
Then determines if the adjecent cells are 0 or 1.
Forms an output using only the selected red cells.
If adjacent to 0, the output is 0. If adjacent to 1, the output is 2.
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

    # Find coordinates of red (2) cells.
    red_coords = np.argwhere(input_grid == 2)
    
    # Create dict of red coordinates
    red_dict = {}
    for r, c in red_coords:
      neighbors = get_neighbors(input_grid, r, c)
      red_dict[(r,c)] = neighbors

    # Select coordinates of red (2) cells for 3x3 grid, based on the blue (1)
    # and white (0) adjacencies.
    output_coords = []

    for (r,c), neighbors in red_dict.items():
      is_valid = False
      for neighbor in neighbors:
        if neighbor == 0:
          output_coords.append((r, c, 0)) # add white
          is_valid = True
          break
        elif neighbor == 1:
          is_valid = True
          break
      if is_valid:
        output_coords.append((r, c, 2)) # add red

    # Place red and white pixels in output, based on the input selection
    output_row = 0
    output_col = 0
    for r,c, color in output_coords:
      if output_col > 2:
        output_col = 0
        output_row +=1
      if output_row > 2:
        break
      if color == 2:
        all_zeros = True
        for neighbor in red_dict[(r,c)]:
          if neighbor != 0:
            all_zeros = False
            break
        if all_zeros:
          output_grid[output_row,output_col] = 0
        else:
          output_grid[output_row,output_col] = 2
      else:
          output_grid[output_row,output_col] = 0

      output_col += 1

    return output_grid