"""
1.  **Grid Expansion:** Create an output grid with dimensions double that of the input grid (twice the rows and twice the columns).
2.  **Pixel Block Replication:** For *each* pixel in the input grid, replicate its color value to a 2x2 block of pixels in the output grid. The top-left corner of this 2x2 block has the following coordinates:
    *   Row: Input pixel's row index * 2
    *   Column: Input pixel's column index * 2
3.  **Block Population:** The entire 2x2 block in the output grid receives the same color as the original input pixel. This means:
    *   `output_grid[input_row * 2, input_col * 2] = input_grid[input_row, input_col]`
    *   `output_grid[input_row * 2 + 1, input_col * 2] = input_grid[input_row, input_col]`
    *   `output_grid[input_row * 2, input_col * 2 + 1] = input_grid[input_row, input_col]`
    *   `output_grid[input_row * 2 + 1, input_col * 2 + 1] = input_grid[input_row, input_col]`
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    input_rows, input_cols = input_grid.shape
    output_rows = input_rows * 2
    output_cols = input_cols * 2
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # change output pixels 
    for row in range(input_rows):
        for col in range(input_cols):
            color = input_grid[row, col]
            # Corrected pixel replication
            output_grid[row*2, col*2] = color
            output_grid[row*2 + 1, col*2] = color
            output_grid[row*2, col*2 + 1] = color
            output_grid[row*2 + 1, col*2 + 1] = color
    
    return output_grid