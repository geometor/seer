# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
1. **Initialization:** Create a new output grid that is initially identical to the input grid.
2. **Iterate through Input Grid:** Examine each cell in the input grid, row by row, and column by column.
3. **Identify Red Pixels:** If a cell in the input grid contains the color red (color code 2):
    - Consider its horizontal and diagonal neighbors: top-left, top-right, left, right, bottom-left, and bottom-right.
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to yellow (color code 4).
4. **Identify Blue Pixels:** If a cell in the input grid contains the color blue (color code 1):
    - Consider all eight neighbors: top, bottom, left, right, top-left, top-right, bottom-left, and bottom-right.
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to orange (color code 7).
5. **Maintain Original Pixels:** The original red and blue pixels in the input grid remain unchanged in the output grid. All other pixels that are not neighbors of red or blue pixels (or whose neighbors in input were not white) also remain unchanged from the input to the output grid.
6. **Output:** The resulting output grid after processing all red and blue pixels in the input grid is the final transformed grid.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the specified rules for red and blue pixels."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    def is_valid(r, c):
        """Checks if the given row and column are within the grid boundaries."""
        return 0 <= r < rows and 0 <= c < cols

    def get_neighbors(r, c, diagonal=False):
        """Returns the neighbors of a cell. Includes diagonal neighbors if specified."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                if not diagonal and abs(dr) + abs(dc) == 2:
                    continue
                neighbors.append((r + dr, c + dc))
        return neighbors

    # Iterate through each cell in the input grid
    for r in range(rows):
        for c in range(cols):
            # Process red pixels
            if input_grid[r, c] == 2:
                neighbors = get_neighbors(r, c, diagonal=True)
                for nr, nc in neighbors:
                    if is_valid(nr, nc) and input_grid[nr, nc] == 0:
                        output_grid[nr, nc] = 4  # Change to yellow
            # Process blue pixels
            elif input_grid[r, c] == 1:
                neighbors = get_neighbors(r, c, diagonal=False)  # include diagonals here for "all directions"
                for nr, nc in neighbors:
                     if is_valid(nr, nc) and input_grid[nr, nc] == 0:
                        output_grid[nr, nc] = 7 #change to orange

    return output_grid
```
