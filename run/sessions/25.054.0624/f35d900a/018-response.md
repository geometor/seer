# f35d900a • 018 • refine_coder

---
```python
"""
1.  **Mirroring:** Copy each non-white pixel from the input grid to its corresponding mirrored positions in the output grid. These positions are:
    *   Original position (x, y)
    *   Horizontal mirror (x, width - 1 - y)
    *   Vertical mirror (height - 1 - x, y)
    *   Diagonal mirror (height - 1 - x, width - 1 - y)
    *   If a mirrored position is already occupied by a non-white pixel from a *previous* placement, do not overwrite it.

2.  **Color Expansion (in order):**  After *all* mirroring operations are complete, expand specific colors in the *following* order, *one step* at a time:
    *   **Red (2):**  Replace any white (0) pixel that is directly adjacent (up, down, left, or right) to a red pixel with red.
    *   **Yellow (4):** Replace any white (0) pixel that is directly adjacent to a yellow pixel with yellow.
    *   **Green (3):** Replace any white (0) pixel that is directly adjacent to a green pixel with green.
    *   **Azure (8):** Replace any white (0) pixel that is directly adjacent to an azure pixel with azure.
    * **Blue (1):** Replace any white (0) pixel that is directly adjacent to an azure pixel with blue.

3.  **Gray Filling:** After color expansion, for any remaining white (0) pixels, check for direct adjacency (up, down, left, right) to at least two pixels of *different* non-white colors.  If this condition is met, replace the white pixel with gray (5).
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets the coordinates of adjacent pixels (up, down, left, right)."""
    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent.append((row + 1, col))  # Down
    if col > 0:
        adjacent.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent.append((row, col + 1))  # Right
    return adjacent

def expand_color(grid, color):
    """Expands a specific color in the grid."""
    rows, cols = grid.shape
    new_grid = np.copy(grid)
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                adjacent_coords = get_adjacent_pixels(grid, r, c)
                for ar, ac in adjacent_coords:
                    if 0 <= ar < rows and 0 <= ac < cols and new_grid[ar,ac] == 0: # only expand into white pixels
                        new_grid[ar, ac] = color
    return new_grid

def transform(input_grid):
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # 1. Mirroring
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != 0:
                positions = [(i, j), (i, cols - 1 - j), (rows - 1 - i, j), (rows - 1 - i, cols - 1 - j)]
                for r, c in positions:
                    if 0 <= r < rows and 0 <= c < cols:
                        output_grid[r, c] = input_grid[i, j]

    # 2. Color Expansion (in order)
    output_grid = expand_color(output_grid, 2)  # Red
    output_grid = expand_color(output_grid, 4)  # Yellow
    output_grid = expand_color(output_grid, 3)  # Green
    output_grid = expand_color(output_grid, 8)  # Azure
    output_grid = expand_color(output_grid, 1)  # Blue


    # 3. Gray Filling
    temp_grid = np.copy(output_grid) # copy to avoid changing during iteration
    for i in range(rows):
        for j in range(cols):
            if output_grid[i, j] == 0:
                adjacent_coords = get_adjacent_pixels(output_grid, i, j)
                adjacent_colors = set()
                for r, c in adjacent_coords:
                    if 0 <= r < rows and 0 <= c < cols:
                        adjacent_colors.add(output_grid[r, c])

                adjacent_colors.discard(0)  # Remove white
                if len(adjacent_colors) >= 2:
                    temp_grid[i, j] = 5
    output_grid = temp_grid

    return output_grid
```

