"""
1.  **Identify Key Pixels:** Find all blue (1), red (2), and magenta (6) pixels in the input grid.

2.  **Mirror Red and Blue:** For *each* red and *each* blue pixel located at (row, col), place a yellow pixel (4) at the diagonally mirrored position (`height - 1 - row`, `width - 1 - col`). If the mirrored position falls outside the grid boundary, do *not* place a pixel.

3.  **Orange L Around Blue:** For *each* blue pixel at (row, col):
    *   Place an orange pixel (7) one position to the left: (row, col - 1).
    *   Place an orange pixel (7) one position below: (row + 1, col).
    *   Place an orange pixel (7) one position to the right: (row, col + 1).
    *   Place an orange pixel (7) one position down and one to the left: (row + 1, col - 1).
    *   If any of these positions fall outside the grid, do not place the orange pixel.

4.  **Preservation:** All other pixels, including magenta (6) and any others present, should retain their original color and position, unless they are overwritten by steps 2 or 3. Empty/black pixels stay empty/black, unless overwritten by previous steps.

5.  **Boundaries:** Strictly enforce grid boundaries. Do *not* attempt to place any pixels outside the original grid dimensions.
"""

import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all pixels of a given color."""
    rows, cols = np.where(grid == color)
    return list(zip(rows, cols))

def mirror_position(row, col, height, width):
    """Calculates the mirrored position and checks boundaries."""
    mirrored_row = height - 1 - row
    mirrored_col = width - 1 - col
    return mirrored_row, mirrored_col

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = input_grid.copy()
    height, width = output_grid.shape

    # Find key pixels
    blue_pixels = find_all_pixels(input_grid, 1)
    red_pixels = find_all_pixels(input_grid, 2)

    # Mirror red and blue with yellow
    for row, col in blue_pixels + red_pixels:
        mirrored_row, mirrored_col = mirror_position(row, col, height, width)
        if 0 <= mirrored_row < height and 0 <= mirrored_col < width:
          output_grid[mirrored_row , mirrored_col] = 4

    # Orange L around blue
    for row, col in blue_pixels:
        # Left
        if col > 0:
            output_grid[row, col - 1] = 7
        # Below
        if row < height - 1:
            output_grid[row + 1, col] = 7
        # Right
        if col < width - 1:
            output_grid[row, col + 1] = 7
        # Diagonal below and left
        if row < height - 1 and col > 0:
            output_grid[row + 1, col - 1] = 7

    return output_grid