# 8e5a5113 • 012 • refine_coder

---
```python
"""
1. Iterate through each row of the input grid.
2. For each row, iterate through each pixel.
3. If a grey pixel (value 5) is encountered:
    *   Extract the Pattern: Starting from the pixel *immediately* to the right of the grey pixel, record the color values of the following pixels.  Continue recording until another grey pixel (5) is encountered, or the end of the row is reached. This recorded sequence is the "pattern".
    *  Apply the Pattern: Starting with the first white (0) pixel after the initial grey pixel (5), start replacing the 0's with elements of the extracted pattern. If the pattern is exhausted, wrap around to its beginning.
   * Terminate Pattern Application: Stop applying the pattern if *either* another grey pixel (5) is encountered or the end of the row is reached.
4. If not after a 5 and filling, continue
5.  Return the modified grid.
"""

import numpy as np

def get_pattern(grid, row, col):
    """Extracts the pattern to the right of a grey (5) pixel."""
    rows, cols = grid.shape
    pattern = []
    for c in range(col + 1, cols):
        if grid[row, c] == 5:
            break
        pattern.append(grid[row, c])
    return pattern

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""

    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    for r in range(rows):
        pattern = []
        pattern_index = 0
        filling = False

        for c in range(cols):
            if input_grid[r, c] == 5:
                # Extract the pattern
                pattern = get_pattern(input_grid, r, c)
                pattern_index = 0
                filling = True
                continue  # Move to the next column

            if filling:
                # Apply the pattern to white pixels (0)
                if output_grid[r,c] == 0:
                    if pattern:  # Ensure pattern is not empty
                        output_grid[r, c] = pattern[pattern_index % len(pattern)]
                        pattern_index += 1
                elif output_grid[r,c] == 5:
                    filling = False
                #else, it's another non-white color, keep going

    return output_grid
```

