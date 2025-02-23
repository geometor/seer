"""
The transformation rule is a consistent color mapping across all examples:
- 1 (blue) -> 5 (gray)
- 2 (red) -> 6 (magenta)
- 3 (green) -> 4 (yellow)
- 5 (gray) -> 1 (blue)
- 6 (magenta) -> 2 (red)
- 8 (azure) -> 9 (maroon)
The structure of the grid remains unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a comprehensive color mapping derived from all examples:
    - 1 (blue) -> 5 (gray)
    - 2 (red) -> 6 (magenta)
    - 3 (green) -> 4 (yellow)
    - 5 (gray) -> 1 (blue)
    - 6 (magenta) -> 2 (red)
    - 8 (azure) -> 9 (maroon)
    Maintains the original grid structure.
    """
    # Initialize the output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Apply the color mapping
    output_grid[input_grid == 1] = 5  # Replace all occurrences of 1 with 5
    output_grid[input_grid == 2] = 6  # Replace all occurrences of 2 with 6
    output_grid[input_grid == 3] = 4  # Replace all occurrences of 3 with 4
    output_grid[input_grid == 5] = 1  # Replace all occurrences of 5 with 1
    output_grid[input_grid == 6] = 2  # Replace all occurrences of 6 with 2
    output_grid[input_grid == 8] = 9  # Replace all occurrences of 8 with 9

    return output_grid