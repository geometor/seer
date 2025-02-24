"""
1.  **Identify Objects:** Locate all red (2) and black (0) pixels in the input grid.
2.  **Red Pixel Preservation:**  The red pixels remain unchanged in their original positions in the output grid.
3.  **Yellow Pixel Generation:** For each black pixel in the input grid, check for adjacency to any red pixel. "Adjacency" here means directly above, below, left, or right (not diagonal). If a black pixel is adjacent to *any* red pixel, change it to a yellow (4) pixel in the output grid. If a black pixel has red pixels both horizontally adjacent AND vertically adjacent, it still changes only to ONE yellow pixel in the corresponding output grid.
4.  **Black Pixel Update:** Any black pixel that is *not* adjacent to a red pixel remains black in the output grid.

The transformation can be described as "spreading" yellow from the red pixels to any directly adjacent black pixels, replacing those black pixels with yellow ones.
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
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)  # Start with a copy to preserve red pixels
    rows, cols = input_grid.shape

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 0:  # Check if it's a black pixel
                neighbors = get_neighbors(input_grid, row, col)
                for r, c in neighbors:
                    if input_grid[r, c] == 2:  # Check for adjacent red pixel
                        output_grid[row, col] = 4  # Change to yellow
                        break  # Only change once, even if multiple red neighbors
            # Implicitly, if it's a red pixel (2), it remains unchanged

    return output_grid