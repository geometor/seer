def find_repeating_tile_height(input_grid, output_grid):
    """
    Finds the height of the repeating tile in the input grid that corresponds
    to the repeating pattern.
    """
    input_height = input_grid.shape[0]
    output_height = output_grid.shape[0]

    # Iterate through possible tile heights (up to half the input height)
    for tile_height in range(1, input_height // 2 + 1):
        # Check if the input height is divisible by the tile height
        if input_height % tile_height == 0:
            # Extract the potential tile
            tile = input_grid[:tile_height, :]

            # Reconstruct the input grid using the tile
            reconstructed_input = np.tile(tile, (input_height // tile_height, 1))

            # If the reconstructed input matches the original, we've found a repeating pattern
            if np.array_equal(reconstructed_input, input_grid):
                
                #check output
                
                #replace 1 with 2
                tile[tile == 1] = 2

                #reconstruct the output using the tile
                reconstructed_output = np.tile(tile, (output_height // tile_height, 1))
                if np.array_equal(reconstructed_output, output_grid):

                    return tile_height

    return None  # No repeating tile found

# Find and print tile heights for each example set
for i in range(1, 4):
    input_grid = grids[f"example_{i}_input"]
    output_grid = grids[f"example_{i}_expected"]
    tile_height = find_repeating_tile_height(input_grid, output_grid)
    print(f"Example {i} repeating tile height: {tile_height}")