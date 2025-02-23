"""
1. Identify Key Coordinates: The transformation involves the following coordinates: (0, 0), (0, 1), (0, 2), (2, 0) and (2, 2).
2. Circular Value Shift:
    *   The value at (0, 0) moves to (0, 1).
    *   The value at (0, 1) moves to (0, 2)
    *   The value at (0, 2) moves to (2, 2)
    *   The value at (2, 2) moves to (2, 0)
    *   The value at (2, 0) moves to (0, 0)
3. All other grid cells remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by circularly shifting the values of cells (0, 0), (0, 1), (0, 2), (2,0) and (2,2).
    """
    output_grid = np.copy(input_grid)

    # Store original values
    val_0_0 = input_grid[0, 0]
    val_0_1 = input_grid[0, 1]
    val_0_2 = input_grid[0, 2]
    val_2_0 = input_grid[2, 0]
    val_2_2 = input_grid[2, 2]

    # Perform circular shift
    output_grid[0, 1] = val_0_0  # (0,1) <- (0,0)
    output_grid[0, 2] = val_0_1  # (0,2) <- (0,1)
    output_grid[2, 2] = val_0_2  # (2,2) <- (0,2)
    output_grid[2, 0] = val_2_2  # (2,0) <- (2,2)
    output_grid[0, 0] = val_2_0  # (0,0) <- (2,0)
    
    return output_grid