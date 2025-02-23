import numpy as np

def find_all_pixels(grid, color):
    """Finds the coordinates of all occurrences of a specific color."""
    coords = np.where(grid == color)
    return list(zip(coords[0], coords[1]))

def transform(input_grid):
    """Transforms the input grid according to the refined rule."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    red_positions = find_all_pixels(input_grid, 2)
    blue_positions = find_all_pixels(input_grid, 1)

    # Place yellow pixels diagonally around red pixels
    for r, c in red_positions:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 4

    # Place orange pixels orthogonally around blue pixels
    for r, c in blue_positions:
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 7

    return output_grid