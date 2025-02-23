# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
Transforms an input grid by mirroring and expanding certain colored pixels (blue and red)
and adding adjacent pixels of other colors (orange and yellow) based on the mirrored pixel.
Azure pixels remain unchanged.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the mirroring and expansion rules.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Key Pixels (Blue and Red)
    key_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] in (1, 2):
                key_pixels.append((r, c, input_grid[r, c]))

    # 2. Process Key Pixels (Mirroring and Expansion)
    for r, c, color in key_pixels:
        #Mirror point
        mirror_c = cols - 1 - c

        # 3. Mirror/Expand, Blue(1)
        if color == 1:
            # Mirrored position
            if mirror_c < cols:
               output_grid[r, mirror_c] = 1

               # Add Orange (7) on either side of original blue
               if c > 0:
                   output_grid[r,c-1] = 7
               if c + 1 < cols:
                   output_grid[r, c+1] = 7
               #Add Orange (7) on either side of the mirrored blue.
               if mirror_c > 0:
                   output_grid[r, mirror_c - 1] = 7
               if mirror_c + 1 < cols:
                   output_grid[r, mirror_c + 1] = 7
        # 4. Mirror/Expand Red(2)
        elif color == 2:
            # Mirrored position
            if mirror_c < cols:
               output_grid[r, mirror_c] = 2

               # Add Yellow (4) on either side of the original red
               if c > 0:
                   output_grid[r,c-1] = 4
               if c + 1 < cols:
                   output_grid[r, c+1] = 4
               #Add Yellow (4) on either side of the mirrored red.
               if mirror_c > 0:
                   output_grid[r, mirror_c - 1] = 4
               if mirror_c + 1 < cols:
                   output_grid[r, mirror_c + 1] = 4

    return output_grid
```
