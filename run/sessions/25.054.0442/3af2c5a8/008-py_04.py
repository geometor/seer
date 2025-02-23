"""
The input grid's dimensions (height and width) are doubled to determine the output grid's dimensions. The input grid is then replicated four times, creating a 2x2 grid of the original pattern, to form the output grid.
"""

import numpy as np

def transform(input_grid):
    # Get input grid dimensions
    input_height, input_width = input_grid.shape

    # Calculate output grid dimensions
    output_height = 2 * input_height
    output_width = 2 * input_width

    # Initialize output grid with zeros
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Replicate the input grid to fill the output grid
    for i in range(2):
        for j in range(2):
            output_grid[i * input_height:(i + 1) * input_height, j * input_width:(j + 1) * input_width] = input_grid
    
    return output_grid