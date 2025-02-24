"""
1.  **Identify Blue Pixels:** Locate all blue pixels (value 1) within the input grid.
2.  **Mirror Positions:** For each blue pixel, determine its mirrored position across the vertical axis of the grid. The vertical axis is the middle column. If the grid has an odd number of columns, the axis is the center column. If even, we imagine it between two center columns.
3. **Create Red Pixels:** In the output grid, change the pixels at the mirrored positions to red (value 2).
4. **Blank Canvas:** The output grid starts as all black/empty (all 0).
5.  **Ignore Other Colors:** Only blue pixels in the input are considered for transformation.
"""

import numpy as np

def get_mirrored_position(row, col, num_cols):
    """Calculates the mirrored position across the vertical axis."""
    mirrored_col = num_cols - 1 - col
    return row, mirrored_col

def transform(input_grid):
    """Transforms the input grid by mirroring blue pixels as red pixels."""
    input_grid = np.array(input_grid)
    num_rows, num_cols = input_grid.shape
    output_grid = np.zeros((num_rows, num_cols), dtype=int)  # Blank canvas

    # Identify Blue Pixels
    blue_pixels = np.where(input_grid == 1)
    blue_pixel_coords = list(zip(blue_pixels[0], blue_pixels[1]))

    # Mirror and Create Red Pixels
    for row, col in blue_pixel_coords:
        mirrored_row, mirrored_col = get_mirrored_position(row, col, num_cols)
        output_grid[mirrored_row, mirrored_col] = 2

    return output_grid