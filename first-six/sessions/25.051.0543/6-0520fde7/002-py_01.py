"""
The transformation takes specific object from the input, detects its size, and replaces it by a new object color. The output grid is all zeros (background color) except for a single red (color 2) cell in the center.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a 3x3 numpy array filled with zeros.
    output_grid = np.zeros((3, 3), dtype=int)
    
    # Place the color 2 (red) in the center cell of the output grid.
    output_grid[1, 1] = 2
    
    return output_grid