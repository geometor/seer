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

# Example inputs (as lists of lists)
example_inputs = [
    [[6, 0, 6], [0, 6, 6], [6, 0, 6], [4, 0, 4], [0, 4, 4], [4, 0, 4], [8, 8, 8], [8, 0, 8], [8, 8, 8]],
    [[2, 0, 0, 3, 0, 0, 7, 0, 7, 1, 0, 0], [2, 0, 0, 3, 0, 0, 0, 7, 0, 1, 0, 0], [0, 2, 2, 0, 3, 3, 7, 0, 7, 0, 1, 1]],
    [[3, 0, 0, 4, 0, 4, 2, 0, 0, 8, 0, 0, 1, 0, 0], [0, 3, 3, 4, 4, 4, 0, 2, 2, 0, 8, 8, 0, 1, 1], [0, 3, 0, 4, 0, 4, 0, 2, 0, 0, 8, 0, 0, 1, 0]],
    [[0, 7, 7], [7, 7, 0], [7, 0, 7], [3, 0, 0], [0, 3, 3], [3, 0, 0], [2, 0, 0], [0, 2, 2], [2, 0, 0], [8, 0, 0], [0, 8, 8], [8, 0, 0]]
]

# Expected outputs
example_outputs = [
    [[8, 8, 8], [8, 0, 8], [8, 8, 8]],
    [[7, 0, 7], [0, 7, 0], [7, 0, 7]],
    [[4, 0, 4], [4, 4, 4], [4, 0, 4]],
    [[0, 7, 7], [7, 7, 0], [7, 0, 7]]
]
results = []
for i, input_grid in enumerate(example_inputs):
    # Convert input grid to numpy array
    grid = np.array(input_grid)
    blocks = find_blocks(grid)
    top_coords, top_color = find_uppermost_block_with_block_below(blocks, grid.shape)
    transformed = transform(input_grid)

    results.append({
        "input": input_grid,
        "expected_output": example_outputs[i],
        "blocks_found": blocks,
        "top_block_coords": top_coords,
        "top_block_color": top_color,
        "transformed_result": transformed
         })

for r in results:
    print(r)
