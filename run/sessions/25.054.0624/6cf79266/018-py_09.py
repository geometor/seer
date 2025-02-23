"""
1.  **Identify the Target Color:** Examine all input/output pairs. The target color is the color that *changes* to blue (1) in the output grids, forming contiguous 1x3 or 3x1 blocks in the *input* grids.
2.  **Locate Target Blocks:** In the input grid, find all contiguous 1x3 or 3x1 blocks (horizontal or vertical) of the target color.
3. **Replacement:** If at least three such blocks are found in Step 2, change exactly three of them to blue (color 1). If fewer than three such blocks are found, do not change the input.
4.  **Preserve Other Pixels:** All other pixels in the grid that are not part of the three replaced blocks remain unchanged.
"""

import numpy as np

def find_target_color(input_grids, output_grids):
    """
    Identifies the target color based on input/output pairs.
    """
    for i in range(len(input_grids)):
        diff = np.where(input_grids[i] != output_grids[i])
        if len(diff[0]) > 0:  # Check if there are any differences
            #The color that changes to blue is our target
            return input_grids[i][diff[0][0], diff[1][0]]
    return None  # Should never happen if there is a valid transformation

def find_blocks(grid, target_color):
    """
    Finds all 1x3 and 3x1 blocks of the target color in the grid.
    Returns a list of (row, col, is_horizontal) tuples.
    """
    height, width = grid.shape
    blocks = []
    for r in range(height):
        for c in range(width):
            # Check for 1x3
            if (c + 2 < width and
                grid[r, c] == target_color and
                grid[r, c+1] == target_color and
                grid[r, c+2] == target_color):
                blocks.append((r, c, True))
            # Check for 3x1
            if (r + 2 < height and
                grid[r, c] == target_color and
                grid[r+1, c] == target_color and
                grid[r+2, c] == target_color):
                blocks.append((r, c, False))
    return blocks

def transform(input_grid, input_grids=None, output_grids=None):

    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find the target color using training examples
    target_color = find_target_color(input_grids, output_grids)
    if target_color is None:
        return output_grid #If target color is not found, return input grid
    
    #Locate Target Blocks
    blocks = find_blocks(input_grid, target_color)

    # Replacement
    count = 0
    for r, c, is_horizontal in blocks:
      if count >= 3:
          break
      if is_horizontal:
        output_grid[r,c:c+3] = 1
      else:
        output_grid[r:r+3,c] = 1
      count += 1

    # return the output_grid
    return output_grid