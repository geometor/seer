"""
The transformation preserves two 2x2 squares (blue and red) from the input grid. 
It then adds a diagonal line of blue pixels starting near the top-left corner and going down, stopping when it encounters existing blue pixels. 
A diagonal line of red pixels is added starting to the right and down, stopping when it encounter a red pixel.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)  # Start with a copy of the input

    # Find the 2x2 squares (for generalization)
    def find_squares(grid):
      squares = []
      for r in range(grid.shape[0] - 1):
        for c in range(grid.shape[1] - 1):
          if grid[r, c] == grid[r+1, c] == grid[r, c+1] == grid[r+1, c+1] != 0:
            squares.append((r, c, grid[r,c])) # row, col, color
      return squares

    squares = find_squares(input_grid)


    # Add diagonal blue pixels
    r, c = 0, 0
    while r < input_grid.shape[0] and c < input_grid.shape[1] and output_grid[r,c] == 0:
        output_grid[r,c] = 1
        r += 1
        c += 1

    # Add diagonal red pixels
    red_squares = [(r, c) for r, c, color in squares if color == 2]

    #Find the first red square from top-left
    red_squares.sort()

    if red_squares:
        start_r, start_c = red_squares[0]
        start_c += 2
        start_r -= 1
        r, c = start_r, start_c
        while r < input_grid.shape[0] and c < input_grid.shape[1] and r >=0:
            if output_grid[r,c]==0:
                output_grid[r, c] = 2
            elif output_grid[r,c]==2:
                break;
            r += 1
            c += 1


    return output_grid