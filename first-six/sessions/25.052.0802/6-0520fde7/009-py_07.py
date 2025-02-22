"""
The transformation rule is as follows:
1. Identify the vertical line of color 5 in the input grid.
2. Create a 3x3 output grid filled with color 0s.
3. Change the color of the topmost and bottommost cells of the identified vertical line from 5 to 2.
4. Place the modified top cell at [1, 0] and the modified bottom cell at [2, 2] in the output grid.
5. Ensure all other cells in the output grid remain color 0.
"""

import numpy as np

def find_vertical_line(grid, color):
    # Find contiguous vertical lines of the specified color
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                 if r + 2 < rows and grid[r+2,c] == color:
                    return [(r,c), (r+1, c), (r+2, c)]  # Return all cells in vertical line.
    return None

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Convert input grid to numpy array
    input_grid = np.array(input_grid)

    # Find the vertical line of color 5
    line_cells = find_vertical_line(input_grid, 5)

    # Initialize the output grid as a 3x3 array filled with 0s
    output_grid = np.zeros((3, 3), dtype=int)

    # If a vertical line of color 5 is found:
    if line_cells:
        # Place the modified top cell at [1, 0]
        output_grid[1, 0] = 2
        # Place the modified bottom cell at [2, 2]
        output_grid[2, 2] = 2

    return output_grid