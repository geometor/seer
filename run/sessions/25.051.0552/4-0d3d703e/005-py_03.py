"""
The transformation rule is a simple color mapping:
- Color 5 (gray) becomes color 1 (blue).
- Color 8 (azure) becomes color 9 (maroon).
- Color 6 (magenta) becomes color 2 (red).
The structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a color mapping:
    - 5 (gray) -> 1 (blue)
    - 8 (azure) -> 9 (maroon)
    - 6 (magenta) -> 2 (red)
    Maintains the original grid structure.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply the color mapping
    output_grid[input_grid == 5] = 1  # Replace all occurrences of 5 with 1
    output_grid[input_grid == 8] = 9  # Replace all occurrences of 8 with 9
    output_grid[input_grid == 6] = 2  # Replace all occurrences of 6 with 2

    return output_grid