"""
The transformation rule creates a 3x3 output grid based on the input grid's elements, particularly focusing on a vertical gray line and the pixel to its immediate left. The output grid is initialized with all white pixels (0). The placement of red pixels (2) within this output grid is determined by the color of the pixel directly to the left of the gray line. If there is no gray line, the output grid remains all white. If there's only the gray line, a single red pixel is placed at the center (1,1).  If the pixel to the left of the gray line is blue (1) and also the left pixel is white (0), red pixels are placed at (0,1), (1,2), and (2,1). If the pixel to the left of the gray line is white (0), red pixels are placed at (0,2), (1,0), and (2,1). If the pixel to the left is blue (1), red pixels are placed at (1,0) and (2,2).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to a 3x3 output grid, placing red pixels based on
    the pixel to the left of a vertical gray line.
    """
    output_grid = np.zeros((3, 3), dtype=int)
    rows, cols = input_grid.shape

    # Find the column index of the gray line (assuming only one exists)
    gray_col = -1
    for c in range(cols):
        if np.any(input_grid[:, c] == 5):
            gray_col = c
            break

    if gray_col == -1:  # No gray line found
        return output_grid # Return all white cells

    # Case 1: Only gray line
    if gray_col != -1 and not (np.any(input_grid == 1) or np.any(input_grid==0)):
          output_grid[1, 1] = 2
          return output_grid
          
    # Find the relevant blue pixel's row (if it exists)
    blue_row = -1
    if gray_col > 0:  # Ensure there's a column to the left of the gray line
        for r in range(rows):
            if input_grid[r, gray_col - 1] == 1:
                blue_row = r
                # Case 2: Blue pixel to the left of the gray line and white pixel on the left.
                if gray_col > 1 and input_grid[r,gray_col-2] == 0:
                  output_grid[0, 1] = 2
                  output_grid[1, 2] = 2
                  output_grid[2, 1] = 2
                  return output_grid
                # Case 4.
                else:
                  output_grid[1, 0] = 2
                  output_grid[2, 2] = 2
                  return output_grid
            elif input_grid[r, gray_col - 1] == 0: # Case 3
                output_grid[0, 2] = 2
                output_grid[1, 0] = 2
                output_grid[2, 1] = 2
                return output_grid

    return output_grid