"""
Transforms the input grid based on a specific value mapping.  The
transformation replaces each pixel's value with a corresponding value from
a predefined lookup table.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to a predefined mapping.

    Args:
        input_grid: A 3x3 numpy array of integers.

    Returns:
        A 3x3 numpy array representing the transformed grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the value mapping (lookup table).
    value_mapping = {
        1: 5,
        2: 6,
        3: 4,
        4: 3,
        5: 1,
        6: 2,
        8: 9,
        9: 8,
    }

    # Iterate through each cell of the output grid.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Get the original pixel value.
            original_value = output_grid[i, j]
            
            # Apply the mapping if the value exists in the mapping
            if original_value in value_mapping:
                output_grid[i, j] = value_mapping[original_value]
            # else leave alone, to accommodate cases where the transform is unknown

    return output_grid