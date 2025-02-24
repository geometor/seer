"""
The input grid is replaced with a 3x3 magenta grid, and the background is preserved as white in a single pixel.
"""

import numpy as np

def transform(input_grid):
    # Initialize a 3x3 output grid filled with magenta (6).
    output_grid = np.full((3, 3), 6, dtype=int)

    # Preserve the background color (white, 0) in the top-left cell.
    output_grid[0, 0] = 0

    return output_grid