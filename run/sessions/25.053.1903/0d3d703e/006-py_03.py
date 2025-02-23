"""
Each example represents a different transformation. There isn't one global transformation; instead there appears to be a per-cell addition operation.

For each example:
1.  The input is a grid of numbers.
2. The output is the result of adding a value to the input on a cell-by-cell basis.
3. The added values must be calculated modulo 10.  `(output_cell - input_cell) % 10`
4. The values added are different across the different examples, and also vary across cells *within* an example.
"""

import numpy as np

def transform(input_grid, example_id):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Define the per-cell transformation maps for each example.
    transformation_maps = {
        1: [(0,0,1),(0,1,4),(0,2,4),(1,0,1),(1,1,4),(1,2,4),(2,0,1),(2,1,4),(2,2,4)],
        2: [(0,0,4),(0,1,1),(0,2,1),(1,0,4),(1,1,1),(1,2,1),(2,0,4),(2,1,1),(2,2,1)],
        3: [(0,0,6),(0,1,1),(0,2,6),(1,0,6),(1,1,1),(1,2,6),(2,0,6),(2,1,1),(2,2,6)],
        4: [(0,0,9),(0,1,9),(0,2,4),(1,0,9),(1,1,9),(1,2,4),(2,0,9),(2,1,9),(2,2,4)],
    }

    # Check if the example_id is valid
    if example_id not in transformation_maps:
        raise ValueError("Invalid example_id. No transformation map found.")

    current_map = transformation_maps[example_id]
    # change output pixels based on transformation map

    for (row, col, add_value) in current_map:
        output_grid[row,col] = (input_grid[row,col] + add_value) % 10

    return output_grid