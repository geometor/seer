# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
1.  **Identify Seed Pixels:** Locate all non-black pixels (pixels with values 1-9) in the input grid. These are the "seed" pixels.

2.  **Process Each Seed:** For each seed pixel:
    *   **Preserve Original:** Keep the original seed pixel in the output grid at the same location and with the same color.

3.  **Conditional Spawning:**
        *   If the seed pixel is azure (8), spawn two yellow (4) pixels: one 2 steps right and 1 down, the second 4 steps right and 1 down.
        *   If the seed pixel is red (2), spawn an orange (7) pixel: 4 steps to the left on the same row (if that position is outside of the grid, do not create it).
        *   If the seed pixel is blue (1) and on an odd numbered row, create an orange (7) pixel to the left, and to the right. If on an even row, create an orange (7) one step above and below.
        *   If the seed pixel is blue (1) and y > 5 and an even number, spawn yellow (4) at x=0 and x=2 on rows above and below seed.

4.  **Boundaries:** Ensure new pixels do not go outside the bounds of the 9x9 grid. If a calculated position is outside the grid, do not create that pixel.
"""

import numpy as np

def find_seed_pixels(grid):
    # Find coordinates and colors of non-black pixels
    seed_pixels = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                seed_pixels.append({'color': grid[y, x], 'x': x, 'y': y})
    return seed_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    seed_pixels = find_seed_pixels(input_grid)

    # change output pixels
    for seed in seed_pixels:
        x = seed['x']
        y = seed['y']
        color = seed['color']

        # Preserve Original - already done by copying input_grid

        # Conditional Spawning
        if color == 8:  # Azure
            new_x1 = x + 2
            new_y1 = y + 1
            new_x2 = x + 4
            new_y2 = y + 1
            if 0 <= new_x1 < 9 and 0 <= new_y1 < 9:
                output_grid[new_y1, new_x1] = 4
            if 0 <= new_x2 < 9 and 0 <= new_y2 < 9:
                output_grid[new_y2, new_x2] = 4

        elif color == 2:  # Red
            new_x = x - 4
            new_y = y
            if 0 <= new_x < 9 and 0 <= new_y < 9:
                output_grid[new_y, new_x] = 7

        elif color == 1:  # Blue
            if y % 2 != 0: # Odd row
                new_x1 = x -1
                new_y1 = y
                new_x2 = x + 1
                new_y2 = y

                if 0 <= new_x1 < 9 and 0 <= new_y1 < 9:
                    output_grid[new_y1,new_x1] = 7
                if 0 <= new_x2 < 9 and 0 <= new_y2 < 9:
                    output_grid[new_y2,new_x2] = 7

            else:
                new_x1 = x
                new_y1 = y - 1
                new_x2 = x
                new_y2 = y + 1

                if 0 <= new_x1 < 9 and 0 <= new_y1 < 9:
                    output_grid[new_y1,new_x1] = 7
                if 0 <= new_x2 < 9 and 0 <= new_y2 < 9:
                    output_grid[new_y2,new_x2] = 7

            if y > 5 and y % 2 == 0: # Blue and on even, >5 row

                new_y1 = y - 1
                new_y2 = y + 1

                if 0 <= new_y1 < 9:
                    output_grid[new_y1, 0] = 4
                    output_grid[new_y1, 2] = 4
                if 0 <= new_y2 < 9:
                    output_grid[new_y2, 0] = 4
                    output_grid[new_y2, 2] = 4

    return output_grid
```
