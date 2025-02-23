"""
1.  **Identify Seed Pixels:** Find all pixels in the input grid that are not white (0). These are the "seed" pixels.

2.  **Conditional Expansion - Seed Pixel Rules**
    *   If a seed pixel is Blue (1): Add Orange (7) pixels to its immediate left, right, and below positions, *but only if* those positions are currently White (0) in the *output* grid.
    *   If a seed pixel is Red (2): Add Yellow (4) pixels to its immediate top, left, and right positions, *but only if* those positions are currently White (0) in the *output* grid.
    *   If a seed pixel is Magenta (6) or Azure (8): Do nothing.

3. **Iterative Expansion:**
   * After applying the seed pixel rules above, extend around the *newly added* colors as follows:
   * If extending a blue(1) -> orange(7) area: add orange (7) to any *newly added* orange pixel's immediate left, right, and below positions, *but only if* those positions are currently White(0). Do not extend orange(7) up.
   * If extending a red(2) -> yellow(4) area: add yellow(4) to any *newly added* yellow pixel's immediate top, left and right, *but only if* those positions are currently White (0). Do not extend yellow(4) down.

4. **Do not extend colors onto other colors**
    *   All pixels that are added must extend on to an existing white (0) space.
    *   Do not extend a color onto a space if another color is present, either in the original grid or placed as an extension.

5.  All other White (0) pixels in the original input should remain White (0) if not modified by the above rule.
"""

import numpy as np

def get_seed_pixels(grid):
    """Finds all non-zero pixels and returns their coordinates and values."""
    seed_pixels = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value != 0:
                seed_pixels.append(((r, c), value))
    return seed_pixels

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    seed_pixels = get_seed_pixels(input_grid)

    # Conditional Expansion - Seed Pixel Rules
    new_pixels = []
    for (row, col), value in seed_pixels:
        if value == 1:  # Blue
            # Add Orange (7) to the left, right, and below
            neighbors = [(row, col - 1), (row, col + 1), (row + 1, col)]
            for r, c in neighbors:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1] and output_grid[r, c] == 0:
                    output_grid[r, c] = 7
                    new_pixels.append(((r,c),7)) # track newly added pixel
        elif value == 2:  # Red
            # Add Yellow (4) to the top, left, and right
            neighbors = [(row - 1, col), (row, col - 1), (row, col + 1)]
            for r, c in neighbors:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1] and output_grid[r, c] == 0:
                    output_grid[r, c] = 4
                    new_pixels.append(((r,c), 4)) # track newly added pixel

    # Iterative Expansion
    for (row,col), value in new_pixels:
        if value == 7: # newly added orange
            neighbors = [(row, col - 1), (row, col + 1), (row + 1, col)]
            for r, c in neighbors:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1] and output_grid[r, c] == 0:
                    output_grid[r,c] = 7
        elif value == 4:  # newly added yellow
            neighbors = [(row - 1, col), (row, col - 1), (row, col + 1)]
            for r, c in neighbors:
                if 0 <= r < output_grid.shape[0] and 0 <= c < output_grid.shape[1] and output_grid[r, c] == 0:
                    output_grid[r, c] = 4


    return output_grid