"""
The transformation inverts the input grid along the main diagonal (top-left to bottom-right), but the pixel in the center of each edge of the input moves to the center of the opposite edge in the output. The other pixels, the corners and center, are mirrored.

1.  **Mirror the Grid:** Create a mirrored version of the input grid by reflecting it across the main diagonal (transposing rows and columns).
2.  **Center Edge Pixel Swap:** The central pixel on the edge moves to the opposite edge.
"""

import numpy as np

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation.
    input_array = np.array(input_grid)
    height, width = input_array.shape

    # 1. Mirror the Grid (Transpose)
    output_array = np.transpose(input_array)

    # 2. Center Edge Pixel Swap (Conditional Logic)
    if height == width and height % 2 != 0 :  # Only for square, odd-sized grids
        mid = height // 2
        
        # Top edge center to Bottom Edge Center
        output_array[height - 1, mid] = input_array[0, mid]

        # Bottom edge center to Top Edge Center
        output_array[0, mid] = input_array[height-1, mid]

        # Left edge center to right edge center
        output_array[mid, width - 1] = input_array[mid, 0]

        # right edge center to left edge center
        output_array[mid, 0] = input_array[mid, width-1]
    
    # Convert the NumPy array back to a list of lists.
    output_grid = output_array.tolist()
    return output_grid