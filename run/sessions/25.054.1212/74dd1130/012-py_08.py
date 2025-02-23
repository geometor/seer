"""
1. Transpose: Transpose the input grid. This means swapping rows and columns: the element at `input[i][j]` will move to the position `output[j][i]`.
2. Apply Original Row Values: Construct the output grid by taking the elements *from the original input grid*, but placing them at their *transposed* locations in the output grid.  Crucially, *do not sort the rows before transposition*.
"""

import numpy as np

def _transpose(grid):
    """Transposes a grid (swaps rows and columns)."""
    return [list(row) for row in zip(*grid)]

def transform(input_grid):
    """
    Transforms the input grid by transposing it. The element at input_grid[i][j]
    moves to output_grid[j][i].
    """
    # Transpose the original input grid.
    transposed_grid = _transpose(input_grid)

    # Initialize the output grid with zeros - using numpy for easier handling,
    # and with the dimensions of the transposed grid.
    output_grid = np.zeros_like(transposed_grid)

    # Apply the original values to their transposed positions.
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            output_grid[j][i] = input_grid[i][j]

    return output_grid.tolist()  # Convert back to list of lists