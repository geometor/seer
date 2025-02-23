"""
1. **Identify the Gray Object:** In the input grid, locate the contiguous gray (color 5) object. This object is the primary focus of the transformation.
2. **Change all Gray to Azure:** For all locations where the original object (gray) was, now all will be azure (color 8).
3. **Change central-connected pixels to Red:** Inside of the gray object, now azure, there are some locations where a pixel has four neighbors (up, down, left, and right). If that is the case, and it creates a connected component inside the azure shape, change it to red (color 2).
"""

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

    # Change all gray (5) to azure (8)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                output_grid[r, c] = 8

    # Change central-connected pixels to red (2)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 8:
                neighbors = get_neighbors(output_grid, r, c)
                neighbor_colors = [output_grid[nr, nc] for nr, nc in neighbors]
                if all(color == 8 for color in neighbor_colors) and len(neighbors) == 4:
                    output_grid[r,c] = 2

    return output_grid