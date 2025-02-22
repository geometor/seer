import numpy as np

def get_neighbors(grid, r, c):
    """ Return 4 neighbors of the cell in grid"""

    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Create a temporary grid to track the original positions of gray pixels
    temp_grid = np.copy(input_grid)

    # 1. & 2. Change all gray (5) to azure (8)
    output_grid[output_grid == 5] = 8

    # 3. Change central-connected pixels to red (2)
    for r in range(rows):
        for c in range(cols):
            if temp_grid[r, c] == 5:
                neighbors = get_neighbors(temp_grid, r, c)
                # Count only neighbors that were originally gray (5)
                gray_neighbors = 0
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols and temp_grid[nr, nc] == 5:
                        gray_neighbors += 1
                if gray_neighbors == 4:  # Check for exactly 4 gray neighbors
                    output_grid[r, c] = 2

    return output_grid