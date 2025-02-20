"""
1. **Initialization:** Create a new output grid, initially identical to the input grid.
2. **Iterate through Input Grid:** Process each cell of the input grid, row by row, and column by column.
3. **Identify Red Pixels:** If a cell in the input grid is red (color code 2):
    - Examine its diagonal neighbors: top-left, top-right, bottom-left, and bottom-right.
    - For each diagonal neighbor, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a diagonal neighbor in the input grid is white, change the color of the same diagonal neighbor cell in the *output* grid to yellow (color code 4).
4. **Identify Blue Pixels:** If a cell in the input grid is blue (color code 1):
    - Consider all eight neighbors: top, bottom, left, right, top-left, top-right, bottom-left, and bottom-right.
    - For each neighbor, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor in the input grid is white, change the color of the same neighbor cell in the *output* grid to orange (color code 7).
5. **Maintain Original Pixels:** The original red and blue pixels in the input grid remain unchanged in the output grid. Pixels that are not neighbors of red or blue pixels, or whose neighbors in the input were not white, are also unchanged.
6. **Unaffected Magenta Pixels:** Pixels of magenta color (color code 6) and their neighbors are not affected by this transformation and remain as they were in the input grid.
7. **Output:** The final output grid is the result of applying these transformations.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid based on the proximity of red and blue pixels to white pixels."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    def is_valid(r, c):
        """Checks if the given row and column are within the grid boundaries."""
        return 0 <= r < rows and 0 <= c < cols

    def get_diagonal_neighbors(r, c):
        """Returns the diagonal neighbors of a cell."""
        neighbors = []
        for dr in [-1, 1]:
            for dc in [-1, 1]:
                neighbors.append((r + dr, c + dc))
        return neighbors

    def get_all_neighbors(r, c):
        """Returns all 8 neighbors of a cell."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                neighbors.append((r + dr, c + dc))
        return neighbors

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # Process red pixels
            if input_grid[r, c] == 2:
                neighbors = get_diagonal_neighbors(r, c)
                for nr, nc in neighbors:
                    if is_valid(nr, nc) and input_grid[nr, nc] == 0:
                        output_grid[nr, nc] = 4  # Change to yellow
            # Process blue pixels
            elif input_grid[r, c] == 1:
                neighbors = get_all_neighbors(r, c)
                for nr, nc in neighbors:
                    if is_valid(nr, nc) and input_grid[nr, nc] == 0:
                        output_grid[nr, nc] = 7  # Change to orange

    return output_grid