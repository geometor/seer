"""
1.  Find the 2x2 Block: Locate the single 2x2 block of non-zero pixels within the input grid.
2.  Identify the Origin: Within the 2x2 block, examine the four pixels. Determine which pixel is the *expansion origin*. This is the pixel that does *not* form a diagonal pair of the same color within the 2x2 box.
3.  Determine Expansion Color: The color of the expansion origin pixel is the expansion color.
4.  Expand Diagonally: Starting from the expansion origin, extend the expansion color outwards. The expansion occurs diagonally.
5.  Bound the Expansion:** The expansion stops when it hits:
      * The edges of the input grid.
      * Imaginary diagonals drawn at 45 degrees to the edge from the origin pixel outwards.
6.  Fill with Background:** All other pixels in the output grid remain 0 (background color).
"""

import numpy as np

def find_2x2_block(grid):
    """Finds the single 2x2 block of non-zero pixels."""
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            block = grid[i:i+2, j:j+2]
            if np.all(block != 0):
                #check if it the *only* 2x2 block
                is_unique = True
                for other_i in range(rows - 1):
                  for other_j in range(cols - 1):
                     if (other_i != i or other_j !=j):
                       other_block = grid[other_i:other_i+2, other_j:other_j+2]
                       if np.all(other_block != 0) and np.any(other_block):
                         is_unique = False
                         break
                  if not is_unique:
                    break
                if is_unique:
                  return (i, j), block
    return None, None

def identify_origin(block_coords, block):
    """Identifies the expansion origin within the 2x2 block."""
    top_left = block[0, 0]
    top_right = block[0, 1]
    bottom_left = block[1, 0]
    bottom_right = block[1, 1]

    if top_left != bottom_right and top_right != bottom_left:
        if top_left == top_right or top_left == bottom_left:
            return block_coords, top_left  # Top-left
        elif bottom_right == top_right or bottom_right == bottom_left:
            return (block_coords[0] + 1, block_coords[1] + 1), bottom_right  # Bottom-right
        elif top_right == bottom_left:
          return (block_coords[0], block_coords[1] + 1), top_right # Top-right

    #check for unique
    if top_left != top_right and top_left != bottom_left and top_left != bottom_right:
      return block_coords, top_left
    elif top_right != bottom_left and top_right != bottom_right:
      return (block_coords[0], block_coords[1]+1), top_right
    elif bottom_left != bottom_right:
      return (block_coords[0]+1, block_coords[1]), bottom_left
    else:
        return (block_coords[0] + 1, block_coords[1] + 1), bottom_right  # Bottom-right

def transform(input_grid):
    """Transforms the input grid according to the 2x2 block expansion rule."""
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Find the 2x2 Block
    block_coords, block = find_2x2_block(input_grid)
    if block_coords is None:
        return output_grid  # No 2x2 block found

    # 2. Identify the Origin
    origin_coords, expansion_color = identify_origin(block_coords, block)

    # 3. Determine Expansion Color (already done in identify_origin)

    # 4. & 5. Expand Diagonally and Bound the Expansion
    o_row, o_col = origin_coords

    for i in range(rows):
        for j in range(cols):
            delta_row = i - o_row
            delta_col = j - o_col

            # Determine the quadrant and apply bounding rules
            if o_row == block_coords[0] and o_col == block_coords[1]:  # Top-left origin
                if delta_row >= 0 and delta_col >= 0 and delta_row >= delta_col:
                    output_grid[i, j] = expansion_color
            elif o_row == block_coords[0] and o_col == block_coords[1] + 1:  # Top-right origin
                if delta_row >= 0 and delta_col <= 0 and delta_row >= -delta_col:
                    output_grid[i, j] = expansion_color
            elif o_row == block_coords[0] + 1 and o_col == block_coords[1]:  # Bottom-left origin
              if delta_row <= 0 and delta_col >= 0 and -delta_row >= delta_col:
                  output_grid[i,j] = expansion_color
            elif o_row == block_coords[0] + 1 and o_col == block_coords[1] + 1:  # Bottom-right origin
                if delta_row <= 0 and delta_col <= 0 and -delta_row >= -delta_col:
                    output_grid[i, j] = expansion_color


    return output_grid