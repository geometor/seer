"""
The input grid is tiled 3x3. Then, a condition is checked: If the center pixel of the input grid is equal to 3, 
the border of the entire output grid is set to 0. Otherwise, the border of each individual tile is set to 0.
"""

import numpy as np

def transform(input_grid):
    # Tile the input grid 3x3
    input_array = np.array(input_grid)
    tiled_array = np.tile(input_array, (3, 3))

    # Get dimensions of the original input grid and the tiled array
    input_rows, input_cols = input_array.shape
    tiled_rows, tiled_cols = tiled_array.shape

    # Check the condition: if the center pixel of input grid is 3
    if input_array[input_rows // 2, input_cols // 2] == 3:
        # Set the border of the entire tiled array to 0
        tiled_array[0, :] = 0
        tiled_array[tiled_rows - 1, :] = 0
        tiled_array[:, 0] = 0
        tiled_array[:, tiled_cols - 1] = 0
    else:
        # Iterate through each tile and set its border to 0
        for i in range(3):
            for j in range(3):
                start_row = i * input_rows
                start_col = j * input_cols

                tiled_array[start_row, start_col:start_col + input_cols] = 0
                tiled_array[start_row + input_rows - 1, start_col:start_col + input_cols] = 0
                tiled_array[start_row:start_row + input_rows, start_col] = 0
                tiled_array[start_row:start_row + input_rows, start_col + input_cols - 1] = 0

    output_grid = tiled_array.tolist()
    return output_grid