"""
1.  Identify all non-zero pixels (colored objects).
2.  Locate the maroon pixel (color 9). Move this pixel to the last row of the grid, while maintaining its original column.
3.  Locate the azure pixel (color 8) that is not part of a contiguous vertical object of size=2, move it to the last row, keep the original column if unoccupied, if occupied by an object, move object to the next available row.
4.  All other objects remain in their original positions.
"""

import numpy as np

def find_object(grid, color, exclude_positions=None):
    # Find the position of a specific colored pixel.
    if exclude_positions is None:
        exclude_positions = []

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in exclude_positions:
                return (r, c)
    return None

def get_contiguous_vertical_objects(grid):
    # Find objects that are vertically contiguous with size
    objects = []

    for c in range(grid.shape[1]):
      for r in range(grid.shape[0]):
        color = grid[r,c]
        if(color != 0):
            count = 0
            for r2 in range(r, grid.shape[0]):
                if grid[r2,c] == color:
                    count = count + 1
                else:
                    break;
            if count > 0:
                obj = {'color': color, 'position':(r,c), 'size': count}
                objects.append(obj)

    return objects

def is_cell_occupied(grid, row, col):
    # Check if a cell is occupied by a non-zero value.
    return grid[row, col] != 0

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Move the maroon pixel (color 9)
    maroon_pos = find_object(input_grid, 9)
    if maroon_pos:
        output_grid[maroon_pos[0], maroon_pos[1]] = 0  # Remove from original position
        output_grid[output_grid.shape[0] - 1, maroon_pos[1]] = 9  # Place in new position

    # move azure pixel (color 8)
    contiguous_vertical = get_contiguous_vertical_objects(input_grid)
    exclude_positions = []
    for obj in contiguous_vertical:
      if obj['size'] > 1:
        for i in range(0,obj['size']):
          exclude_positions.append( (obj['position'][0] + i, obj['position'][1]) )

    azure_pos = find_object(input_grid, 8, exclude_positions)

    if azure_pos:
        output_grid[azure_pos[0], azure_pos[1]] = 0

        target_row = output_grid.shape[0] - 1
        target_col = azure_pos[1]
        
        if not is_cell_occupied(output_grid, target_row, target_col):
          output_grid[target_row, target_col] = 8
        else:
          #find next available row
          
          for r in range(target_row -1, -1, -1):
            if not is_cell_occupied(output_grid, r, target_col):
              output_grid[r, target_col] = 8
              break

    return output_grid