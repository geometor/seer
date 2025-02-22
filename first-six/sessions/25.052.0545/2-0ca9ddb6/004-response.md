# 2-0ca9ddb6 • 004 • refine_code - CODE

---
```python
"""
1. Identify Objects: Find all single-cell red (color 2) objects and all single-cell blue (color 1) objects within the input grid.

2. Red Object Transformation: For *each* red object:
    *   Place yellow (color 4) cells in an "L" shape, like a mirrored "L", at the diagonally adjacent positions around the red cell. Specifically, place a yellow cell above and to the left, above and to the right, below and to the left, and below and to the right.

3. Blue Object Transformation: For *each* blue object:
    *   Place orange (color 7) cells in a "cross" shape around the blue cell. This means placing orange cells directly above, below, to the left, and to the right of the blue cell.

4.  Other colors: Any cells that are not the red object or the blue object will stay the same.
"""

import numpy as np

def find_all_objects(grid, color):
    # Find the positions of all single-cell objects with the given color.
    positions = np.argwhere(grid == color)
    return positions

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all red objects (color 2).
    red_positions = find_all_objects(input_grid, 2)
    for red_pos in red_positions:
        # Create yellow "L" shapes around each red object.
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_r, new_c = red_pos[0] + dr, red_pos[1] + dc
            if 0 <= new_r < rows and 0 <= new_c < cols: # Boundary check
                output_grid[new_r, new_c] = 4
        

    # Find all blue objects (color 1).
    blue_positions = find_all_objects(input_grid, 1)
    for blue_pos in blue_positions:
        # Create orange crosses around each blue object.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = blue_pos[0] + dr, blue_pos[1] + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:  # Boundary check
                output_grid[new_r, new_c] = 7

    return output_grid
```

