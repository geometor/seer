"""
Crops and overlays colored rectangular regions (objects) from the input grid onto an output grid,
maintaining relative positions and scaling them to the output size. The first colored object forms
the background, and subsequent objects are overlaid on top, with the earlier object appearing
in front in case of overlaps.
"""

import numpy as np

def find_objects(grid):
    """
    Identifies distinct rectangular regions of non-zero color.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, color, object_coords):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        object_coords.append((r, c))
        dfs(r + 1, c, color, object_coords)
        dfs(r - 1, c, color, object_coords)
        dfs(r, c + 1, color, object_coords)
        dfs(r, c - 1, color, object_coords)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                object_coords = []
                dfs(r, c, grid[r, c], object_coords)
                # Find min and max row/col to define the rectangle
                min_r = min(object_coords, key=lambda x: x[0])[0]
                max_r = max(object_coords, key=lambda x: x[0])[0]
                min_c = min(object_coords, key=lambda x: x[1])[1]
                max_c = max(object_coords, key=lambda x: x[1])[1]
                objects.append({
                    'color': grid[r, c],
                    'position': (min_r, min_c, max_r, max_c)  # (min_row, min_col, max_row, max_col)
                })
    return objects

def transform(input_grid, output_grid_shape):
    # initialize output_grid
    output_grid = np.zeros(output_grid_shape, dtype=int)

    # find objects
    objects = find_objects(np.array(input_grid))

    # Scale and overlay objects onto the output grid
    output_rows, output_cols = output_grid.shape

    for obj in objects:
      min_r, min_c, max_r, max_c = obj['position']
      color = obj['color']

      # Scale object dimensions to output grid size, maintaining aspect ratio
      input_height = max_r - min_r + 1
      input_width = max_c - min_c + 1

      output_height = int(input_height * output_rows / input_grid.shape[0])
      output_width = int(input_width *  output_cols / input_grid.shape[1])

      # output can not be zero, at least size 1
      output_height = max(1,output_height)
      output_width = max(1, output_width)

      # compute starting position on output
      out_r_start = int(min_r * output_rows / input_grid.shape[0])
      out_c_start = int(min_c * output_cols / input_grid.shape[1])

      # overlay section on to output
      for r in range(output_height):
          for c in range(output_width):
            output_row = out_r_start + r
            output_col = out_c_start + c

            if 0 <= output_row < output_rows and 0 <= output_col < output_cols:
              output_grid[output_row, output_col] = color

    return output_grid