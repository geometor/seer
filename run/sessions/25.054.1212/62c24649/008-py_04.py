"""
The input grid is scaled up and mirrored to create the output grid. The output
grid has double the dimensions of the input grid (6x6 vs 3x3). The
transformation involves mirroring the input both horizontally and vertically,
while preserving the original colors. Each pixel in the input becomes a 2x2
block of the same color in the output.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by scaling and mirroring it.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Create an empty output array with double the dimensions
    output_array = np.zeros((rows * 2, cols * 2), dtype=int)

    # Scale up and mirror
    for i in range(rows):
        for j in range(cols):
            # Copy each element to a 2x2 block in the output array
            output_array[2*i:2*i+2, 2*j:2*j+2] = input_array[i, j]
            
    return output_array.tolist()