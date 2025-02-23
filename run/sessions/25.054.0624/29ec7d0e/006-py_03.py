"""
The transformation identifies blue (1) regions and selectively fills in white (0) pixels between blue regions,
only if doing so connects two separate blue regions, and that no other non-white, non-blue pixels are changed. Other
colored pixels are left untouched.
"""

import numpy as np
from scipy.ndimage import label, find_objects

def get_neighbors(r, c, rows, cols):
    """
    Returns the valid neighbors of a cell (r, c) in a grid of size (rows, cols).
    """
    neighbors = []
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i, j) != (r, c):
                neighbors.append((i, j))
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Preserve non-blue and non-white pixels (implicit by copying and only modifying 0s).

    # 2. Conditional Blue Expansion and Connection
    while True:
        changes_made = False
        labeled_grid, num_features = label(output_grid == 1)
        slices = find_objects(labeled_grid)
        white_pixels = np.argwhere(output_grid == 0)

        for r, c in white_pixels:
            neighbors = get_neighbors(r, c, rows, cols)
            neighboring_labels = set()
            for nr, nc in neighbors:
                if output_grid[nr, nc] == 1:
                    neighboring_labels.add(labeled_grid[nr, nc])

            # Check if connecting different blue regions
            if len(neighboring_labels) > 1:
                temp_grid = np.copy(output_grid)
                temp_grid[r,c] = 1
                new_labeled_grid, new_num_features = label(temp_grid == 1)

                if new_num_features < num_features:
                    output_grid[r,c] = 1
                    changes_made = True

        if not changes_made:
            break

    return output_grid