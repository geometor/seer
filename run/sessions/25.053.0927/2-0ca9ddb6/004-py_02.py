"""
Transforms an input grid based on these rules:

1.  **Identify Key Pixels:** Locate all blue (1), red (2), and azure (8) pixels. These pixels do not change their color or position. They are *anchors*.
2.  **Orange Fill:** Any white (0) pixel that is directly adjacent (horizontally, vertically, *or diagonally*) to a blue (1) or a red(2) pixel changes to orange (7).
3.  **Yellow Fill:**
    *   Locate the center row and center column of the grid.
    *   White pixels at positions that are mirrored across *both* center axes change to Yellow.
"""

import numpy as np

def get_neighbors(grid, row, col, include_diagonal=True):
    """Gets the neighbors of a cell in a grid."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i != row or j != col):  # Exclude the cell itself
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # Find anchor pixels (blue, red, and azure)
    blue_pixels = np.where(input_grid == 1)
    red_pixels = np.where(input_grid == 2)
    azure_pixels = np.where(input_grid == 8)

    anchor_pixels = []
    for r, c in zip(blue_pixels[0], blue_pixels[1]):
        anchor_pixels.append((r,c))
    for r, c in zip(red_pixels[0], red_pixels[1]):
        anchor_pixels.append((r,c))
    for r, c in zip(azure_pixels[0], azure_pixels[1]):
        anchor_pixels.append((r,c))

    # Orange Fill: Change white pixels adjacent to blue or red pixels to orange
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0:  # Check only white pixels
                neighbors = get_neighbors(input_grid, r, c)
                for nr, nc in neighbors:
                    if input_grid[nr, nc] == 1 or input_grid[nr, nc] == 2:
                        output_grid[r, c] = 7
                        break  # Once changed, no need to check other neighbors

    # Yellow Fill: Change white pixels mirrored across center axes to yellow
    center_row = rows // 2
    center_col = cols // 2

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0: # check only white
                mirrored_row = rows - 1 - r
                mirrored_col = cols - 1 - c
                if (r != mirrored_row and c != mirrored_col and output_grid[mirrored_row,mirrored_col] == 0):
                  output_grid[r,c] = 4

    return output_grid