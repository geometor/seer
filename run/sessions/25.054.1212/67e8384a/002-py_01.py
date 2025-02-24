"""
The input grid is replicated four times to create a 2x2 grid. Each quadrant of the 2x2 grid is a mirrored version of the input:

- Top-left: Original input grid.
- Top-right: Horizontally mirrored input grid.
- Bottom-left: Vertically mirrored input grid.
- Bottom-right: Diagonally mirrored (both horizontally and vertically) input grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid by replicating and mirroring it."""

    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = np.zeros((2 * rows, 2 * cols), dtype=int)

    # Top-left: Original
    output_grid[:rows, :cols] = input_grid

    # Top-right: Horizontal flip
    output_grid[:rows, cols:] = np.fliplr(input_grid)

    # Bottom-left: Vertical flip
    output_grid[rows:, :cols] = np.flipud(input_grid)

    # Bottom-right: Both flips (horizontal + vertical)
    output_grid[rows:, cols:] = np.fliplr(np.flipud(input_grid))

    return output_grid.tolist()