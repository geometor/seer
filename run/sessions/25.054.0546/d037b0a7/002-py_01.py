"""
1.  **Identify Key Pixels:** Find the pixel with the value 6 (magenta) in the input grid.
2.  **Magenta Propagation:**  Propagate the value '6' downwards and to the left, replacing any '0' (white) pixels encountered. Stop propagation in a direction when a non-zero pixel is met.
3. **Yellow propogation** Propogate the value '4' downwards.
4. Ignore other non-zero pixels.
"""

import numpy as np

def get_top_right_nonzero(grid):
    for j in range(grid.shape[1] - 1, -1, -1):
        for i in range(grid.shape[0]):
            if grid[i, j] != 0:
                return (i, j)
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # find top right non zero
    top_right_coords = get_top_right_nonzero(input_grid)
    if top_right_coords is None:
        return output_grid

    top_right_value = input_grid[top_right_coords]

    # propogate magenta
    i, j = top_right_coords
    # Propagate left
    for k in range(j, -1, -1):
        if input_grid[i,k] == 0:
            output_grid[i, k] = top_right_value
        else:
          if (i,k) != (i,j):
            break

    # Propagate down
    for k in range(i, rows):
        if input_grid[k, j] == 0:
            output_grid[k, j] = top_right_value
        else:
          if (k,j) != (i,j):
            break
          

    # propogate 4 downwards

    for row_index in range(rows):
        for col_index in range(cols):
          if output_grid[row_index,col_index] == 4:
              for k in range(row_index + 1, rows):
                  if output_grid[k,col_index] == 0:
                      output_grid[k,col_index] = 4
                  else:
                      break
    return output_grid