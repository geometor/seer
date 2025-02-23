"""
1.  **Identify Key Pixels:** Locate all red (2) and blue (1) pixels within the input grid.
2.  **Preserve Existing Colors:** Maintain the original colors of the input grid.
3. **Place Yellow Pixels Diagonally:** For each red (2) pixel, place yellow (4) pixels in the four diagonally adjacent cells (upper-left, upper-right, lower-left, lower-right), *only if those cells are currently black (0)*.
4.  **Place Orange Pixels Orthogonally:** For each blue (1) pixel, place orange (7) pixels in the four orthogonally adjacent cells (left, right, up, down), *only if those cells are currently black(0)*.
5. **Preserve Other Pixels** All the other pixels that are not red, blue, yellow, or orange must remain with the color they had originally.
"""

import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all occurrences of a specific color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid according to the refined rule."""
    output_grid = np.copy(input_grid)  # Preserve original colors
    rows, cols = output_grid.shape

    red_positions = find_all_pixels(input_grid, 2)  # Find all red pixels
    blue_positions = find_all_pixels(input_grid, 1)  # Find all blue pixels

    # Place yellow (4) pixels diagonally around red (2) pixels
    for r, c in red_positions:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Diagonal offsets
            nr, nc = r + dr, c + dc
            # Check boundaries and if the cell is black (0)
            if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 4

    # Place orange (7) pixels orthogonally around blue (1) pixels
    for r, c in blue_positions:
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Orthogonal offsets
            nr, nc = r + dr, c + dc
            # Check boundaries and if the cell is black (0)
            if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 7

    return output_grid