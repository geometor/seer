"""
Extracts a subgrid from the top-left corner of the input grid. The dimensions of
the subgrid are determined by the smaller of the input grid's dimensions and 4.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a subgrid from the top-left corner.  The output grid's dimensions
    are at most 4x4, but will be smaller if the input grid is smaller.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The extracted subgrid.
    """
    # Determine Output Dimensions:
    input_height = len(input_grid)
    input_width = len(input_grid[0]) if input_height > 0 else 0
    output_height = min(input_height, 4)
    output_width = min(input_width, 4)

    # Extract Subgrid:
    output_grid = []
    for i in range(output_height):
        row = []
        for j in range(output_width):
            row.append(input_grid[i][j])
        output_grid.append(row)

    return output_grid