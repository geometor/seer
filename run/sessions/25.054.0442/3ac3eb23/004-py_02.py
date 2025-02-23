"""
The transformation identifies non-zero pixels in the input grid and replicates their values downwards in an alternating pattern with white (0) pixels.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by replicating non-zero pixels downwards in an alternating pattern with white.
    
    Args:
        input_grid (list of lists): The input grid.
    
    Returns:
        list of lists: The transformed output grid.
    """
    
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell of the input grid
    for r in range(rows):
        for c in range(cols):
            # Check if the pixel is non-zero
            if input_grid[r, c] != 0:
                # Replicate the non-zero pixel's value downwards in an alternating pattern
                for i in range(r + 1, rows):
                    # Calculate the vertical distance
                    distance = i - r
                    # Alternate between the pixel's color and white (0)
                    if distance % 2 != 0:
                        output_grid[i, c] = input_grid[r, c]  # Odd distance: Set to the original color
                    else:
                        output_grid[i, c] = 0 # Even distance, set to white.
    return output_grid.tolist()