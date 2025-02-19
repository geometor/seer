"""
This program transforms the input grid to the output grid by applying the following color mapping:
- Color 5 (gray) in the input grid is changed to color 1 (blue) in the output grid.
- Color 8 (azure) in the input grid is changed to color 9 (maroon) in the output grid.
- Color 6 (magenta) in the input grid is changed to color 2 (red) in the output grid.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid to the output grid by applying a color mapping.
    
    Args:
        input_grid (numpy.ndarray): A 2D numpy array representing the input grid.
    
    Returns:
        numpy.ndarray: A 2D numpy array representing the output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Define the color mapping.
    color_map = {
        5: 1,  # Gray to Blue
        8: 9,  # Azure to Maroon
        6: 2   # Magenta to Red
    }

    # Iterate over all cells in the grid using nested loops.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            # Apply color transformation based on the color map.
            if output_grid[i, j] in color_map:
                output_grid[i, j] = color_map[output_grid[i, j]]

    return output_grid