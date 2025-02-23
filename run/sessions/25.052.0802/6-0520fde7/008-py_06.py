"""
1. Identify a Vertical Line: Search the input grid for a contiguous vertical line composed of three cells of color 5 (gray).
2. Create Output Grid: Initialize a 3x3 output grid filled entirely with color 0 (white).
3. Transform and Place Line: If a vertical line of color 5 is found in the input:
    *   Change the color of this line to color 2 (red).
    *   Place the now red-colored, 3-cell vertical line in the *center* column of the output grid.  The row position is preserved.
4. No Line Found: If no such vertical line is found, the output remains a 3x3 grid of color 0.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find contiguous vertical lines of the specified color
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 2):
            if grid[r, c] == color and grid[r+1, c] == color and grid[r+2, c] == color:
                return r, c  # Return starting row and col
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Find the vertical line of color 5
    line_start = find_vertical_line(input_grid, 5)

    # Initialize the output grid as a 3x3 array filled with 0s
    output_grid = np.zeros((3, 3), dtype=int)

    # If a vertical line of color 5 is found
    if line_start:
        row_start, _ = line_start
        # Place the transformed line in the center column of output, preserving the row
        for i in range(3):
            if row_start + i < output_grid.shape[0] :
                output_grid[row_start + i, 1] = 2

    return output_grid