"""
The transformation rule is to identify the smallest repeating vertical unit (tile) of white (0) and blue (1) pixels in the input grid. 
Within this tile, replace all blue pixels (1) with red pixels (2). White pixels (0) remain unchanged. 
Repeat this modified tile vertically three times to create the output grid, resulting in an output height of 9.
"""

import numpy as np

def find_repeating_tile_height(input_grid):
    """
    Finds the height of the repeating tile in the input grid.
    """
    input_height = input_grid.shape[0]

    # Iterate through possible tile heights (up to half the input height)
    for tile_height in range(1, input_height // 2 + 1):
        if input_height % tile_height == 0:
            tile = input_grid[:tile_height, :]
            reconstructed_input = np.tile(tile, (input_height // tile_height, 1))
            if np.array_equal(reconstructed_input, input_grid):
                return tile_height
    return None

def transform(input_grid):
    # Find the height of the repeating tile.
    tile_height = find_repeating_tile_height(input_grid)
    
    # Extract the repeating tile.
    tile = input_grid[:tile_height, :]

    # Create a copy of the tile to modify.
    modified_tile = np.copy(tile)

    # Substitute blue (1) with red (2) in the modified tile.
    modified_tile[modified_tile == 1] = 2

    # Repeat the modified tile three times vertically.
    output_grid = np.tile(modified_tile, (3, 1))
    
    return output_grid