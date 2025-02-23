"""
The transformation rule identifies maroon (9) pixels in the input grid and changes a corresponding number of white (0) pixels to red (2) in the output grid. The output grid is 3x3. The selection of which white pixels to change to red appears to follow a specific pattern related to the position of the maroon pixels within each 3x3 block of the input, prioritizing top-left to bottom-right within those blocks. If a maroon pixel exists in a row in input grid, change a white pixel in same row in output grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid)
    
    # Count the number of maroon pixels in the input grid.
    maroon_count = np.sum(input_grid == 9)
    red_placed = 0

    # Iterate through input rows and change the output grid.
    for i in range(min(input_grid.shape[0], output_grid.shape[0])): # Iterate up to the smaller dimension
        if 9 in input_grid[i, :]:
                if red_placed < maroon_count :
                    for j in range(output_grid.shape[1]):
                         if output_grid[i,j] == 0:
                            output_grid[i,j] = 2
                            red_placed+=1
                            break # move to the next row

    # Iterate through input cols
    if (red_placed < maroon_count):
      for j in range(min(input_grid.shape[1], output_grid.shape[1])):
          if 9 in input_grid[:, j]:
              if red_placed < maroon_count:
                    for i in range(output_grid.shape[0]):
                        if output_grid[i, j] == 0:
                            output_grid[i,j] = 2;
                            red_placed += 1
                            break;

    #If still more to place
    if (red_placed < maroon_count):
        for i in range(output_grid.shape[0]):
             for j in range(output_grid.shape[1]):
                if output_grid[i,j] == 0:
                    output_grid[i,j] = 2
                    red_placed += 1
                    if red_placed >= maroon_count:
                        break
             if red_placed >= maroon_count:
                break

    return output_grid