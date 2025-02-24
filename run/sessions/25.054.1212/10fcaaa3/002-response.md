# 10fcaaa3 • 002 • example_1 • investigate_coder

---
```python
"""
Expands the input grid, populates it with a pattern of azure and white columns, and replicates the gray pixels from the input, adjusting their position in the expanded grid.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with doubled dimensions
    input_height, input_width = input_grid.shape
    output_height = input_height * 2
    output_width = input_width * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Populate Azure: Fill even columns with azure (8)
    for x in range(0, output_width, 2):
        output_grid[:, x] = 8

    # Populate Gray: Replicate and position gray pixels
    for y in range(input_height):
        for x in range(input_width):
            if input_grid[y, x] == 5:
                output_grid[y * 2 + 1, x * 2 + 1] = 5
                output_grid[y*2 + 1 +1, x * 2 + 1] = 5 # duplicate down

    # Remaining cells are already initialized to 0 (white), so no further action needed.

    return output_grid
```

