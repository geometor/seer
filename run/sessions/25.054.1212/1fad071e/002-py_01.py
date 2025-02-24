"""
Divides the input grid into five vertical regions and checks for the presence of blue (1) in each region.
Outputs a 1x5 grid where each cell is blue (1) if the corresponding input region contained blue, and white (0) otherwise.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_height, input_width = input_grid.shape
    output_width = 5
    output_grid = np.zeros((1, output_width), dtype=int)  # Initialize output grid with white (0)

    # Calculate region width.  Handle cases where the width is not perfectly divisible.
    region_width = input_width // output_width
    extra_pixels = input_width % output_width
    
    start_col = 0
    for i in range(output_width):
        # Distribute any extra pixels across the regions, one at a time.
        current_region_width = region_width + (1 if i < extra_pixels else 0)
        end_col = start_col + current_region_width

        # Extract the current region
        region = input_grid[:, start_col:end_col]

        # Check for the presence of blue (1) in the region
        if np.any(region == 1):
            output_grid[0, i] = 1  # Set output pixel to blue (1)

        start_col = end_col # move to the next region

    return output_grid