# ce4f8723 • 018 • refine_coder

---
```python
"""
1.  **Extract Subgrid:** Extract the top-left 4x4 subgrid from the input grid.
2.  **Recolor Blue Pixels:** Within the extracted subgrid, locate all blue (1) pixels. Change these pixels to green (3). *Crucially*, record the original locations of these blue pixels *before* they were changed.
3.  **Propagate Green Conditionally:** Iterate through the *original* locations of the blue pixels (now green). For *each* of these locations:
    *   Check its four immediate neighbors (up, down, left, and right).
    *   If a neighboring pixel is white (0), change it to green (3).
    *   If a neighbor is any other color, do *not* change it.
4.  **Output:** The resulting 4x4 subgrid, after the recoloring and conditional propagation, is the output.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of the 4x4 subgrid
    output_grid = np.copy(input_grid[:4, :4])

    # store the original locations of blue pixels
    original_blue_locations = []
    for r in range(4):
        for c in range(4):
            if output_grid[r, c] == 1:
                original_blue_locations.append((r, c))

    # change blue pixels to green
    for r, c in original_blue_locations:
        output_grid[r, c] = 3

    # propagate green to adjacent white pixels of originally blue pixels
    for r, c in original_blue_locations:
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            if 0 <= nr < 4 and 0 <= nc < 4 and output_grid[nr, nc] == 0:
                output_grid[nr, nc] = 3

    return output_grid
```
