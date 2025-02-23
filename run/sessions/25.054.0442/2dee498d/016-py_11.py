"""
Extracts the smallest repeating horizontal sequence from the input grid to form the output grid, allowing for interruptions.
"""

import numpy as np

def find_repeating_unit(grid):
    """Finds the smallest repeating unit in a grid along the horizontal axis, allowing interruptions."""
    height, width = grid.shape
    for unit_width in range(1, width + 1):
        unit = grid[:, :unit_width]
        # Check if the unit appears at least once anywhere in the grid
        for start_col in range(width - unit_width + 1):
            if np.array_equal(unit, grid[:, start_col:start_col + unit_width]):
                return unit  # Return the unit if found
    return grid  # If no repeating unit is found, return the original grid

def transform(input_grid):
    """
    Extracts the fundamental repeating unit from the input grid, handling potential interruptions.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The output grid, which is the repeating unit.
    """
    # Find the repeating unit, allowing for interruptions
    repeating_unit = find_repeating_unit(np.array(input_grid))

    # The repeating unit is the output grid
    output_grid = repeating_unit

    return output_grid.tolist()