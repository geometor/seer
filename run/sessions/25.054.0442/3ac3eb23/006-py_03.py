"""
The transformation identifies non-zero pixels in the input grid and creates an alternating pattern of the original pixel's color and white (0) in the corresponding column, centered on the original pixel's row.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by creating alternating patterns of original color and white in columns with non-zero pixels.
    
    Args:
        input_grid (list of lists): The input grid.
    
    Returns:
        list of lists: The transformed output grid.
    """
    
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)  # Initialize with all zeros
    rows, cols = input_grid.shape

    # Iterate through each cell to find trigger pixels (non-zero)
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                # Initiate alternating pattern for this column
                original_color = input_grid[r, c]
                
                # Fill the center pixel
                output_grid[r, c] = original_color

                # Extend upwards
                for i in range(1, rows):
                    if r - i >= 0:
                        if i % 2 == 0:
                            output_grid[r - i, c] = original_color
                        else:
                            output_grid[r - i, c] = 0
                    else:
                        break

                # Extend downwards
                for i in range(1, rows):
                    if r + i < rows:
                        if i % 2 == 0:
                            output_grid[r + i, c] = original_color
                        else:
                             output_grid[r + i, c] = 0
                    else:
                        break

    return output_grid.tolist()