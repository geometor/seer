"""
The transformation involves two main actions: The inner orange square expands into a cross-like shape, and the outer red rectangle expands and reshapes to fit and to surround the expanded orange object.
"""
import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the orange object
    orange_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 7:
                orange_coords.append((r, c))

    # Expand the orange object into cross shape
    if orange_coords:
      min_or = min(r for r,c in orange_coords)
      max_or = max(r for r,c in orange_coords)
      min_oc = min(c for r,c in orange_coords)
      max_oc = max(c for r,c in orange_coords)

      center_r = (min_or + max_or) //2
      center_c = (min_oc + max_oc) //2

      #central square
      for r in range(rows):
        for c in range(cols):
          if input_grid[r,c] == 7:
            output_grid[r,c] = 7
      #vertical arm
      output_grid[center_r -1, center_c] = 7
      output_grid[center_r -1, center_c + 1] = 7

    # find red object
    red_coords = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 2:
              red_coords.append((r,c))
    if red_coords:
      min_rr = min(r for r, c in red_coords)
      max_rr = max(r for r, c in red_coords)
      min_rc = min(c for r, c in red_coords)
      max_rc = max(c for r, c in red_coords)
      # copy first and last rows
      for c in range(min_rc, max_rc+1):
        if min_rr > 0:
            output_grid[min_rr-1, c] = 2
        if max_rr < rows -1:
            output_grid[max_rr+1,c] = 2
      # add columns
      for r in range(min_rr-1, max_rr + 2):

          if min_oc > 0:
              output_grid[r,min_oc-1] = 2
          if max_oc < cols-1:
              output_grid[r,max_oc+2] = 2

          if 0 <= r < rows:
              if min_rc>0:
                  output_grid[r,min_rc-1] = 2
              if max_rc < cols -1:
                  output_grid[r,max_rc+1] = 2

    return output_grid