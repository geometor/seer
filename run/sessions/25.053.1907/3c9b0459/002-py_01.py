"""
The transformation rule is a 180-degree rotation of the grid. Each pixel in the input grid is mapped to a new position in the output grid such that its row and column indices are reversed relative to the maximum indices. For example, pixel at (0,0) in input goes to (2,2) in output, and pixel at (1,0) goes to (1,2).
"""

import numpy as np

def transform(input_grid):
    """
    Rotates the input grid by 180 degrees.
    """
    # Convert input_grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)
    
    # Get the dimensions of the input grid
    rows, cols = input_array.shape
    
    # Initialize the output grid with zeros
    output_array = np.zeros_like(input_array)
    
    # Iterate through each cell of the input grid and map it to the corresponding
    # cell in the output grid based on the 180-degree rotation rule.
    for i in range(rows):
        for j in range(cols):
            output_array[rows - 1 - i, cols - 1 - j] = input_array[i, j]
            
    return output_array.tolist()