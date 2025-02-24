"""
Copies the input grid and iteratively adds a pixel of the same color below each colored pixel, alternating with background color, until the bottom of the grid is reached.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each column
    for col in range(cols):
        # Find the starting (top-most) non-background pixel in the column
        for row in range(rows):
            if output_grid[row, col] != 0:
                source_color = output_grid[row, col]
                
                # Start dripping below the found pixel
                current_row = row + 1
                use_source_color = True # Flag to alternate colors
                
                while current_row < rows:
                    if use_source_color:
                        output_grid[current_row, col] = source_color
                    else:
                        output_grid[current_row, col] = 0  # Background color
                    
                    use_source_color = not use_source_color # Toggle the flag
                    current_row += 1
                
                break  # Move to the next column after processing a source pixel

    return output_grid