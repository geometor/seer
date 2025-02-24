# 10fcaaa3 • 006 • refine_coder

---
```python
"""
Transforms the input grid by mirroring non-zero and non-eight pixels horizontally and vertically,
and filling the background with a checkerboard pattern of azure (8) and white (0).
The height is doubled unless input height is 3, then 2 is added. The width is always doubled.
"""

import numpy as np

def transform(input_grid):
    # 1. Determine Output Dimensions:
    input_height, input_width = input_grid.shape
    output_width = input_width * 2
    output_height = input_height + 2 if input_height == 3 else input_height * 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # 2. Mirror Non-Background Pixels:
    for y in range(input_height):
        for x in range(input_width):
            pixel_value = input_grid[y, x]
            if pixel_value != 0 and pixel_value != 8:
                # Calculate base position
                base_y = y if input_height == 3 else y * 2
                base_x = x * 2

                # Place pixel at base position
                output_grid[base_y, base_x] = pixel_value

                # Calculate mirrored position
                mirrored_x = output_width - 1 - base_x
                mirrored_y = output_height - 1 - base_y if (base_y*2 + 1) < output_height else base_y

                # Place mirrored pixel
                output_grid[mirrored_y, mirrored_x] = pixel_value


    # 3. Fill Background:
    for y in range(output_height):
        for x in range(output_width):
            if output_grid[y, x] == 0:
                if x % 2 == 0:
                    output_grid[y, x] = 8  # Azure (8) for even x positions

    return output_grid
```
