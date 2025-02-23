"""
The transformation rule can be described as follows:

1.  Direct Color Mapping: For each pixel in the input grid, determine its color value.
2.  Lookup Transformation: Use the following lookup table to map the input color to the output color:

    ```
    1 -> 5
    2 -> 6
    3 -> 4
    4 -> 3
    5 -> 1
    6 -> 2
    8 -> 9
    9 -> 8
    ```
3.  replace the input pixel with the output from the lookup table
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Create a lookup table (dictionary) for the transformation.
    lookup_table = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8,
    }

    # Iterate through each cell in the grid.
    for i in range(rows):
        for j in range(cols):
            # Get the original value of the cell.
            original_value = input_grid[i, j]

            # Check if the original value is in the lookup table.
            if original_value in lookup_table:
                # Assign the new value from the lookup table to the output grid.
                output_grid[i, j] = lookup_table[original_value]

    return output_grid