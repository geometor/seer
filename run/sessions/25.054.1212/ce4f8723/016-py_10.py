"""
1.  **Extract Subgrid:** Extract the top-left 4x4 subgrid from the input grid.
2.  **Recolor:** Within the extracted subgrid, replace all occurrences of the value '1' (blue) with the value '3' (green).
3. **Identify Change Locations:** Store the coordinates (row, col) where the color change from 1 to 3 occurred.
4.  **Propagate Change**: Iterate through the changed locations. For each location, check its immediate neighbors (up, down, left, right). If a neighbor is white (0), change it to green (3).
5.  **Output:** The resulting 4x4 subgrid after the recoloring and propagation is the output.
"""

import numpy as np

def transform(input_grid):
    """Transforms an input grid to an output grid based on size reduction and color mapping,
    including propagation of color changes to adjacent white pixels."""

    # 1. Extract Subgrid: Top-left 4x4
    subgrid = input_grid[:4, :4]
    
    # 2. Recolor: 1 (blue) -> 3 (green)
    output_grid = np.copy(subgrid)
    change_locations = []
    for r in range(4):
        for c in range(4):
            if output_grid[r, c] == 1:
                output_grid[r, c] = 3
                change_locations.append((r, c))

    # 3. Propagate Change
    for r, c in change_locations:
        # Check neighbors (up, down, left, right)
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if 0 <= nr < 4 and 0 <= nc < 4 and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 3

    # 4. Output: The recolored 4x4 subgrid.
    return output_grid