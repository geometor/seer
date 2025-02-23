"""
1.  **Identify Barrier Rows:** Examine each row in the input grid. A barrier row is a row where *all* pixels have the *same* color. There should be two barrier rows, and the color of these rows should be present in the example's color palette.
2. **Barrier Color:** Note the color of the barrier row - this color does not change between input and output.
3.  **Propagate Color:** For each pixel *not* in a barrier row, check its immediate neighbors (up, down, left, right - not diagonally).
4. If a pixel is adjacent to *any* pixel that is part of a barrier row, set its
   color to the color of that barrier row.
5.  **Barrier Rows Unchanged:** The pixels in the barrier rows do not change their color.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """Gets directly adjacent pixels (up, down, left, right)."""
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

def find_barrier_rows(grid):
    """Identifies barrier rows based on uniform color."""
    rows, cols = grid.shape
    barrier_rows = []
    for r in range(rows):
        if np.all(grid[r] == grid[r, 0]):  # Check if all pixels in row are the same
            barrier_rows.append(r)
    return barrier_rows

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    
    # Identify barrier rows dynamically
    barrier_rows = find_barrier_rows(input_grid)

    # Iterate through all pixels
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is NOT on a barrier row
            if r not in barrier_rows:
                # Get adjacent pixels
                adjacent_pixels = get_adjacent_pixels(input_grid, r, c)
                # Apply influence from barrier pixels
                for ar, ac in adjacent_pixels:
                    if ar in barrier_rows:
                        barrier_color = input_grid[ar, ac]
                        output_grid[r, c] = barrier_color
    return output_grid