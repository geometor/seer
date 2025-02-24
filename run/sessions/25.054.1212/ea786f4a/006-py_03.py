"""
Forms a cross shape on the output grid and inverts the colors along the cross based on the input grid's colors.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by forming a cross shape and inverting colors along the cross.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
        
    Returns:
        numpy.ndarray: A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = input_grid.copy()
    
    # Get the dimensions of the grid.
    rows, cols = output_grid.shape
    
    # Find the non-zero color in the input grid (foreground color).
    non_zero_colors = np.unique(input_grid[input_grid != 0])
    other_color = non_zero_colors[0] if non_zero_colors.size > 0 else 0

    # Find the center row and column indices.
    center_row = rows // 2
    center_col = cols // 2

    # Iterate through each pixel on central row and column
    for i in range(rows):
        for j in range(cols):
            if i == center_row or j == center_col:
                # Keep center value
                if i == center_row and j == center_col:
                    output_grid[i,j] = other_color
                # Invert other pixels on the cross
                elif output_grid[i, j] == 0:
                    output_grid[i, j] = other_color
                elif output_grid[i,j] == other_color:
                    output_grid[i, j] = 0
                
    return output_grid