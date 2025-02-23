"""
1. Find a 2x2 block in the input.
2. Determine the expansion color and origin corner based on this block.
3. Starting from the identified origin, expand the expansion color into the output grid, bounded by diagonals and edges.
4. All other pixels are 0.
"""

import numpy as np

def find_2x2_block(grid):
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Return top-left coordinates and the 2x2 block itself
            return (i, j), grid[i:i+2, j:j+2]
    return None, None

def determine_expansion_color_and_origin(block_coords, block):
    if block is None:
      return None, None

    top_left = block[0, 0]
    top_right = block[0, 1]
    bottom_left = block[1, 0]
    bottom_right = block[1, 1]
    
    # Prioritize top-left if it matches any other corner
    if top_left == top_right or top_left == bottom_left or top_left == bottom_right:
        return top_left, block_coords #top left corner

    # check bottom right
    if bottom_right == top_right or bottom_right == bottom_left:
      return bottom_right, (block_coords[0]+1, block_coords[1]+1) #bottom right
    # If the top left isn't duplicated, check for diagonal matches for other colors:
    if top_right == bottom_left:
      return top_right, (block_coords[0], block_coords[1]+1)
    if top_left == bottom_right:
      return top_left, block_coords
      
    unique_colors = np.unique(block)
    if len(unique_colors) == 2:
       color_counts = [np.sum(block == color) for color in unique_colors]
       expansion_color = unique_colors[np.argmax(color_counts)]

       # Find the first occurrence of expansion color in block to define origin.
       for i in range(2):
        for j in range(2):
          if block[i,j] == expansion_color:
            return expansion_color, (block_coords[0] + i, block_coords[1] + j)

    return None, None #should not get here


def transform(input_grid):
    # Initialize output_grid with zeros
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Find the 2x2 block
    block_coords, block = find_2x2_block(input_grid)

    # Determine expansion color and origin
    expansion_color, origin_coords = determine_expansion_color_and_origin(block_coords, block)
    
    if expansion_color is not None:
      #expand from origin
      o_row, o_col = origin_coords

      for i in range(rows):
        for j in range(cols):
            # Calculate row and col deltas relative to origin
            delta_row = i - o_row
            delta_col = j - o_col

            # Determine if point is within the bounds of expansion based on origin corner
            if o_row == block_coords[0] and o_col == block_coords[1]: # top-left
              if delta_row >=0 and delta_col >= 0:
                output_grid[i,j] = expansion_color
            elif o_row == block_coords[0] and o_col == block_coords[1] + 1: #top-right
              if delta_row >= 0 and delta_col <= 0:
                output_grid[i,j] = expansion_color
            elif o_row == block_coords[0] + 1 and o_col == block_coords[1]: #bottom left
              if delta_row <= 0 and delta_col >= 0:
                output_grid[i,j] = expansion_color
            elif o_row == block_coords[0] + 1 and o_col == block_coords[1] + 1: #bottom right
              if delta_row <=0 and delta_col <= 0:
                output_grid[i,j] = expansion_color
    return output_grid