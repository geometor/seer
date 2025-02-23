"""
Copy the azure colored pixels from input to output grid. For the top-left L-shape,
add a blue (1) pixel to the right of the azure pixel in its first row.  For the
bottom-right L-shape, locate the azure pixel in the last row where this shape appears.
Then add the blue pixel to the left of its rightmost pixel.
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the azure L-shapes
    azure_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8:
                azure_pixels.append((r, c))

    #find top-left L shape
    top_left_l_shape = []
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 8:
          if r+1 < rows and input_grid[r+1,c] == 8:
            if c+1 < cols and input_grid[r+1,c+1] == 8:
              top_left_l_shape.append((r,c))
              top_left_l_shape.append((r+1,c))
              top_left_l_shape.append((r+1,c+1))
              break
      if len(top_left_l_shape) > 0:
        break

    # Add blue pixel for top-left L-shape
    if len(top_left_l_shape) >0:
          first_row_azure = top_left_l_shape[0]
          output_grid[first_row_azure[0], first_row_azure[1] + 1] = 1

    # Find bottom-right L shape
    bottom_right_l_shape = []
    for r in range(rows -1, -1, -1):
        for c in range(cols -1, -1, -1):
            if input_grid[r, c] == 8:
                if r-1 >= 0 and input_grid[r-1,c] == 8 :
                   if c-1>=0 and input_grid[r,c-1] == 8:
                        bottom_right_l_shape.append((r,c))
                        bottom_right_l_shape.append((r-1,c))
                        bottom_right_l_shape.append((r,c-1))
                        break
        if len(bottom_right_l_shape) >0:
          break

    # Add blue pixel for the second L-shape
    if len(bottom_right_l_shape) > 0:
      last_row = bottom_right_l_shape[0][0]
      rightmost = 0

      for pixel in bottom_right_l_shape:
        if pixel[0] == last_row:
          rightmost = max(rightmost,pixel[1])
      output_grid[last_row,rightmost-1] = 1
    return output_grid.tolist()


if __name__ == '__main__':

    input_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    expected_output_grid = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0],
        [0, 8, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    output_grid = transform(input_grid)

    if output_grid == expected_output_grid:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output_grid)
        print("Transformed Output:", output_grid)

    print()
    assert output_grid == expected_output_grid, "Transformed output does not match expected output."