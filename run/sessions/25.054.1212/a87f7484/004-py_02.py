"""
1.  **Identify 3x3 Blocks:** Examine the input grid and identify all 3x3 square blocks of pixels where all pixels have the same color.

2.  **Find the Uppermost Block with a Block Below:** Among the identified blocks, find the block that has another identified block directly below it, and is the highest block that does so.

3.  **Extract the Block:** Extract the identified block as a 3x3 grid.

4. **Output:** If no such block is found, return None.
"""

import numpy as np

def find_blocks(grid):
    """Finds all 3x3 blocks of the same color in a grid."""
    blocks = []
    rows, cols = grid.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            color = grid[i, j]
            if (grid[i:i+3, j:j+3] == color).all():
                blocks.append(((i, j), color))
    return blocks

def find_uppermost_block_with_block_below(blocks, grid_shape):
    """Finds the uppermost block that has another block directly below it."""
    grid_height = grid_shape[0]
    
    # Create a dictionary to store blocks by their starting row
    blocks_by_row = {}
    for (row, col), color in blocks:
        if row not in blocks_by_row:
            blocks_by_row[row] = []
        blocks_by_row[row].append(((row, col), color))


    for row in sorted(blocks_by_row.keys()): # Check in order of which one is highest
      for (block_row, block_col), color in blocks_by_row[row]:          
          if block_row + 3 < grid_height:  # Make sure we don't go out of bounds
            # Check for a block directly below.
            found_below = False;
            for (other_row, other_col), other_color in blocks:
                if other_row == block_row + 3 and other_col == block_col:
                    return (block_row, block_col), color
    return None, None

def transform(input_grid):
    # Convert input grid to numpy array
    grid = np.array(input_grid)

    # Find all 3x3 blocks
    blocks = find_blocks(grid)
    
    # Find the uppermost block with another block below it
    top_block_coords, top_block_color = find_uppermost_block_with_block_below(blocks, grid.shape)

    # Extract the identified block
    if top_block_coords:
        row, col = top_block_coords
        output_grid = grid[row:row+3, col:col+3]
        return output_grid.tolist()
    else:
        return None  # Return None if no such block is found