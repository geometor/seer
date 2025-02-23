"""
The transformation involves identifying isolated non-black pixels in the input grid and drawing either a horizontal or a vertical line of length 3, centered on the original pixel, based on its neighbors.

1. **Identify Primary Objects:** Find all non-black (non-zero) pixels.
2. **Determine Isolation and Orientation:** For each primary pixel, check for immediate neighbors (up, down, left, right) of the same color.
3. **Create Secondary Object (Line):**
   - If the pixel has no same-color horizontal neighbors, create a vertical line of length 3, of the same color, centered on the primary pixel.
   - If the pixel has no same-color vertical neighbors, create a horizontal line of length 3, of the same color, centered on the primary pixel.
   - A single pixel with no same color neighbors either way creates either a horizontal OR vertical line (the tests will reveal which is consistent).  Let's choose vertical for now.

"""

import numpy as np

def has_same_color_neighbor(grid, r, c, dr, dc, color):
    rows, cols = grid.shape
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        return grid[nr, nc] == color
    return False

def transform(input_grid):
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)

    for r in range(rows):
        for c in range(cols):
            color = input_grid[r, c]
            if color != 0:  # Non-black pixel
                has_horizontal_neighbor = (
                    has_same_color_neighbor(input_grid, r, c, 0, -1, color) or
                    has_same_color_neighbor(input_grid, r, c, 0, 1, color)
                )
                has_vertical_neighbor = (
                    has_same_color_neighbor(input_grid, r, c, -1, 0, color) or
                    has_same_color_neighbor(input_grid, r, c, 1, 0, color)
                )

                if not has_horizontal_neighbor:
                    # Draw vertical line
                    for i in range(max(0, r - 1), min(rows, r + 2)):
                        output_grid[i, c] = color
                elif not has_vertical_neighbor:
                    # Draw horizontal line
                    for j in range(max(0, c - 1), min(cols, c + 2)):
                        output_grid[r, j] = color
                # if both are false - then bias toward vertical
                elif not has_horizontal_neighbor and not has_vertical_neighbor:
                    # Draw vertical line
                    for i in range(max(0, r - 1), min(rows, r + 2)):
                        output_grid[i, c] = color


    return output_grid