"""
Invert colors of the input grid and create a cross shape with the inverted colors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by inverting colors and forming a cross shape.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
        
    Returns:
        numpy.ndarray: A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = input_grid.copy()
    
    # Get the dimensions of the grid.
    rows, cols = output_grid.shape
    
    # Find the non-zero color in the input grid.
    non_zero_colors = np.unique(input_grid[input_grid != 0])
    # Use the first element of non_zero_color, and default color is set to 0 in case of empty non_zero_colors.
    other_color = non_zero_colors[0] if non_zero_colors.size > 0 else 0

    # Find the center row and column indices.
    center_row = rows // 2
    center_col = cols // 2

    # Iterate through each pixel in the grid.
    for i in range(rows):
        for j in range(cols):
            # Check if the pixel is on the center row or center column.
            if i == center_row or j == center_col:
                # Invert the pixel value. 0 becomes other_color, and other_color becomes 0.
                if output_grid[i, j] == 0:
                    output_grid[i, j] = other_color
                elif output_grid[i,j] == other_color:
                    output_grid[i, j] = 0
                
    return output_grid