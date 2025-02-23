# 2-0ca9ddb6 • 018 • example_3 - CODE

---
```python
"""
1.  **Identify original objects**: Find all contiguous non-white pixels in the input grid. These are the original colored objects.
2.  **Determine expansion colors**:
    *   If an original object is red (2), add adjacent pixels colored yellow (4).
    *   If an original object is blue (1), add adjacent pixels colored orange (7).
    *   If an original object is magenta (6) add adjacent pixels, but they will have yellow and orange nearby, so they will not be extended
3.  **Expand objects**: For each original colored object:
    *   For each pixel in the original object, check its four immediate neighbors (up, down, left, right).
    *   If a neighbor is white (0), change it to the designated expansion color based on the original pixel's color. Do *not* extend diagonally.
4. output the final grid
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell (up, down, left, right)."""
    rows, cols = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))  # Up
    if row < rows - 1:
        neighbors.append((row + 1, col))  # Down
    if col > 0:
        neighbors.append((row, col - 1))  # Left
    if col < cols - 1:
        neighbors.append((row, col + 1))  # Right
    return neighbors

def transform(input_grid):
    """Transforms the input grid according to the expansion rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each cell in the input grid
    for row in range(rows):
        for col in range(cols):
            pixel_color = input_grid[row, col]

            # Determine expansion color based on original pixel color
            expansion_color = 0  # Default to white (no expansion)
            if pixel_color == 2:  # Red
                expansion_color = 4  # Yellow
            elif pixel_color == 1:  # Blue
                expansion_color = 7  # Orange
            #elif pixel_color == 6: #Magenta, no expansion color specified

            # If there's an expansion color, check neighbors
            if expansion_color != 0:
                neighbors = get_neighbors(input_grid, row, col)
                for n_row, n_col in neighbors:
                    if output_grid[n_row, n_col] == 0:  # If neighbor is white
                        output_grid[n_row, n_col] = expansion_color  # Expand

    return output_grid
```
