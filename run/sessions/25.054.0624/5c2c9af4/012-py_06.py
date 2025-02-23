"""
1. Identify Trigger Color: Find the most prominent non-black, non-zero color in the input grid. This is the "trigger" color.
2. Create Output Grid: Initialize an output grid of the same dimensions as the input grid, initially filled with black (0).
3. Fill based on inferred shape. Fill parts of the grid based on the trigger color and where its pixels exist in the input. If the trigger color appears, consider its presence to be a filled pixel. If it does not exist, it might still need to be filled if it is forming part of the larger output shape being outlined. Pixels which form the border are not filled.
"""

import numpy as np

def get_trigger_color(grid):
    """
    Finds the non-zero, non-black color in the grid.
    """
    colors = np.unique(grid)
    for color in colors:
        if color != 0:
            return color
    return 0  # Default to black if no trigger color is found

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # get trigger color
    trigger_color = get_trigger_color(input_grid)

    # if no trigger color, return blank grid
    if trigger_color == 0:
      return output_grid

    # Iterate through each cell and decide whether to fill
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is on the border
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                # Check neighbors to see if it should be filled, but not along border
                if (0 < r < rows -1 and input_grid[r,c] == trigger_color) or \
                (0 < c < cols -1 and input_grid[r,c] == trigger_color):
                  output_grid[r,c] = trigger_color
            else: # interior cell
                if input_grid[r, c] == trigger_color:
                    output_grid[r, c] = trigger_color
                else:
                    # if a cell is surrounded it is filled
                    if (0 < r < rows - 1) and (0 < c < cols - 1) :

                        num_neighbors = 0

                        # check all eight neighbors
                        for i in range(-1,2):
                          for j in range(-1,2):
                            if not (i==0 and j==0):
                              if input_grid[r+i,c+j] == trigger_color:
                                num_neighbors+=1

                        # if surrounded on > half the sides, fill
                        if num_neighbors >=3 :
                           output_grid[r,c] = trigger_color


    return output_grid