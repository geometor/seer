# 28bf18c6 • 014 • example_3 • investigate_coder

---
```python
"""
Divide the input grid into 2x2 blocks. If a block contains any blue (1) pixels,
the corresponding output pixel is blue (1). Otherwise, the output pixel is white (0).
"""

import numpy as np

def transform(input_grid):
    input_height = len(input_grid)
    input_width = len(input_grid[0])
    output_height = input_height // 2
    output_width = input_width // 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through 2x2 blocks in the input grid
    for i in range(0, input_height, 2):
        for j in range(0, input_width, 2):
            # Extract the 2x2 block
            block = [row[j:j+2] for row in input_grid[i:i+2]]

            # Check if any blue pixel exists in the block
            has_blue = False
            for row in block:
                for pixel in row:
                    if pixel == 1:
                        has_blue = True
                        break
                if has_blue:
                    break

            # Set the corresponding output pixel
            output_row = i // 2
            output_col = j // 2
            if has_blue:
                output_grid[output_row][output_col] = 1
            # else, leave as 0 (initialized to 0)

    return output_grid
```
