"""
The transformation involves changing solid colored rectangles into checkered patterns of the respective object's color (yellow and azure). Every other cell within each rectangle, starting with the first cell for yellow and the second cell for azure, changes to 0, creating the checkerboard pattern.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by applying a checkerboard pattern to the yellow and azure rectangles.
    
    Args:
        input_grid (numpy.ndarray): The input grid.
    
    Returns:
        numpy.ndarray: The transformed output grid.
    """
    output_grid = np.copy(input_grid)  # Initialize output_grid
    
    # Find the boundaries of the yellow rectangle
    yellow_rows, yellow_cols = np.where(input_grid == 4)
    yellow_min_row, yellow_max_row = np.min(yellow_rows), np.max(yellow_rows)
    yellow_min_col, yellow_max_col = np.min(yellow_cols), np.max(yellow_cols)

    # Apply checkerboard pattern to the yellow rectangle
    for i in range(yellow_min_row, yellow_max_row + 1):
        for j in range(yellow_min_col, yellow_max_col + 1):
            if (i + j) % 2 != 0:  # classic way
                output_grid[i, j] = 0

    # Find the boundaries of the azure rectangle
    azure_rows, azure_cols = np.where(input_grid == 8)
    azure_min_row, azure_max_row = np.min(azure_rows), np.max(azure_rows)
    azure_min_col, azure_max_col = np.min(azure_cols), np.max(azure_cols)

    # Apply checkerboard pattern to the azure rectangle
    for i in range(azure_min_row, azure_max_row + 1):
        for j in range(azure_min_col, azure_max_col + 1):
            if (i+j) % 2 != 0: # classic way
                output_grid[i, j] = 0

    return output_grid