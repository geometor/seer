"""
The transformation involves two main actions. The first action replaces the color `2` object with the color `6`. It effectively overlaps or merges the red object's location with the color magenta. The second is that the entire background, which was originally white (color 0), is changed to green (color 3), except for the final magenta shape.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)

    # Replace all instances of color 2 with color 6
    output_grid[output_grid == 2] = 6

    # Create a new grid filled with color 3 (green).
    new_output_grid = np.full(input_grid.shape, 3)

    # Copy the magenta (color 6) object from output_grid to new_output_grid.
    new_output_grid[output_grid == 6] = 6

    return new_output_grid