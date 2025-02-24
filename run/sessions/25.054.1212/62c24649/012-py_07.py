"""
1.  **Scale Up:** Create an intermediate grid where each pixel from the input grid is expanded into a 2x2 block of the same color. This doubles the dimensions of the grid.
2.  **Horizontal Mirroring:** Create a new intermediate grid by mirroring the scaled-up grid horizontally. Copy each column from left to right on the left, and its mirror on the right.
3.  **Vertical Mirroring:** Mirror the horizontally-mirrored grid vertically. Copy each row from the horizontally mirrored result. Copy rows from top to bottom on top and mirrored at the bottom.
4. **Output**: The final, vertically mirrored grid is the output.
"""

import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # 1. Scale Up
    scaled_array = np.zeros((rows * 2, cols * 2), dtype=int)
    for i in range(rows):
        for j in range(cols):
            scaled_array[2*i:2*i+2, 2*j:2*j+2] = input_array[i, j]

    # 2. Horizontal Mirroring
    horizontally_mirrored_array = np.copy(scaled_array)
    for i in range(rows * 2):
        for j in range(cols):
            horizontally_mirrored_array[i, 2*cols - 1 - j] = scaled_array[i, j]

    # 3. Vertical Mirroring
    output_array = np.copy(horizontally_mirrored_array)
    for i in range(rows):
        for j in range(2 * cols):
            output_array[2*rows - 1 - i, j] = horizontally_mirrored_array[i, j]
    
    return output_array.tolist()