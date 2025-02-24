# 99b1bc43 • 014 • example_3 • investigate_coder

---
```python
"""
The input grid is divided into 2x2 blocks. If a block contains any blue (1), red(2), or yellow(4) pixels, it's replaced by a green (3) pixel in the output grid. Otherwise, it's replaced by a white (0) pixel.
"""

import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    input_height, input_width = input_array.shape
    
    # Calculate output grid dimensions, handling only complete 2x2 blocks
    output_height = input_height // 2
    output_width = input_width // 2
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # Iterate through 2x2 blocks
    for i in range(output_height):
        for j in range(output_width):
            # Extract the 2x2 block
            block = input_array[i*2:(i+1)*2, j*2:(j+1)*2]
            
            # Check for the presence of 1, 2, or 4 in the block and set output pixel accordingly
            if 1 in block or 2 in block or 4 in block:
                output_grid[i, j] = 3
            else:
                output_grid[i, j] = 0

    return output_grid.tolist()
```
