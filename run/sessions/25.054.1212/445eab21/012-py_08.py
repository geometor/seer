"""
1.  **Identify 2x2 Squares:** Examine the input grid and identify if there are any 2x2 squares present, for any colors.
2.  **Prioritize Colors:** If one or more 2x2 squares are present, select the first square encountered, moving row-by-row from the top left. If there is a 2x2 square of color 8, output a 2x2 square of color 8. If there isn't one, but there is a 2x2 square of color 7, output it, etc.
3.  **Output:** Create a 2x2 output grid. Fill the output grid with the color of the selected 2x2 square.
"""

import numpy as np

def extract_2x2_square(grid):
    """
    Extracts the first 2x2 square of any color.
    Returns coordinates of the 2x2 square as a list of tuples and the color.
    """
    for r in range(grid.shape[0] - 1):
        for c in range(grid.shape[1] - 1):
            color = grid[r,c]
            if (grid[r + 1, c] == color and
                grid[r, c + 1] == color and
                grid[r + 1, c + 1] == color):
                return [[r, c], [r + 1, c], [r, c + 1], [r + 1, c + 1]], color
    return [], None

def transform(input_grid):
    """
    Transforms the input grid according to the described rules.
    """
    # initialize output_grid
    output_grid = np.full((2, 2), 0, dtype=int)

    # Find the first 2x2 square
    square_coords, color = extract_2x2_square(input_grid)

    # If a square is found, fill the output grid with its color
    if square_coords:
        output_grid[:] = color

    return output_grid