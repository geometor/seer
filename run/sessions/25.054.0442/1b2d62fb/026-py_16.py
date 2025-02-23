"""
1. **Extract Columns:** From the input grid, extract the first three columns (index 0, 1, and 2).
2.  **Locate and transform central area**: In the extracted portion, two last elements of the last column (index 2).
3.  **Color Replacement**: Change the color of the azure region to 8.
4  **Construct output**: combine first three columns and the modified region.
5.  **Output** The final result should be 5x3.
"""

import numpy as np

def transform(input_grid):
    # Extract the first three columns
    output_grid = input_grid[:, :3].copy()

    # Replace the last two elements of the last column (now index 2) with 8.
    output_grid[-2, 2] = 8
    output_grid[-1, 2] = 8
    

    return output_grid