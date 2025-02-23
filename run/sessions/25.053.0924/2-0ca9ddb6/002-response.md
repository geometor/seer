# 2-0ca9ddb6 • 002 • example_1 - CODE

---
```python
"""
Transforms an input grid based on the color and position of specific pixels.

1.  **Initialization:** Start with an output grid that is the same size as the input grid, and initially filled with zeros.

2.  **Red Pixel (Color 2) Rule:** For every red pixel (value 2) found in the input grid:
    *   Copy the red pixel to the same location in the output grid.
    *   Place a yellow pixel (value 4) directly above the red pixel in the output grid.
    *   Place another yellow pixel (value 4) directly below the red pixel in the output grid.

3.  **Blue Pixel (Color 1) Rule:** For every blue pixel (value 1) found in the input grid:
    *   Copy the blue pixel to the same location in the output grid.
    *   Place an orange pixel (value 7) directly to the left of the blue pixel.
    *   Place an orange pixel (value 7) directly to the right of the blue pixel.
    *   Place an orange pixel (value 7) directly above the blue pixel.
    *   Place an orange pixel (value 7) directly below the blue pixel.
4. **All Other Pixels:** all other pixels remain unchanged (value 0)
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Iterate through each cell of the input grid
    for y in range(input_grid.shape[0]):
        for x in range(input_grid.shape[1]):
            # Red Pixel Rule
            if input_grid[y, x] == 2:
                #output_grid[y, x] = 2 # keep the red pixel (already done by copying)
                if y > 0:
                    output_grid[y - 1, x] = 4  # Yellow above
                if y < input_grid.shape[0] - 1:
                    output_grid[y + 1, x] = 4  # Yellow below

            # Blue Pixel Rule
            elif input_grid[y, x] == 1:
                #output_grid[y,x] = 1 # keep the blue pixel
                if x > 0:
                    output_grid[y, x - 1] = 7  # Orange to the left
                if x < input_grid.shape[1] - 1:
                    output_grid[y, x + 1] = 7  # Orange to the right
                if y > 0:
                    output_grid[y - 1, x] = 7  # Orange above
                if y < input_grid.shape[0] - 1:
                    output_grid[y + 1, x] = 7  # Orange below

    return output_grid
```

