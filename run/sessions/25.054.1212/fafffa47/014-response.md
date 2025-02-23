# fafffa47 • 014 • example_3 • investigate_coder

---
```python
"""
Divides the input grid into 2x1 subgrids and maps each subgrid to a single cell in the output grid. 
If a 2x1 subgrid contains any maroon (9) or blue (1) pixels, the corresponding output cell becomes red (2). 
Otherwise, the output cell remains white (0).
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid as a 3x3 numpy array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through the input grid in 2x1 blocks.
    for i in range(3):  # Iterate through rows of blocks (0, 1, 2)
        for j in range(3):  # Iterate through columns of blocks (0, 1, 2)
            # Define the starting row and column indices for the current 2x1 block.
            start_row = i * 2
            start_col = j * 1

            # Extract the current 2x1 block from the input grid.
            block = input_grid[start_row:start_row + 2, start_col:start_col + 1]

            # Check if the block contains any maroon (9) or blue (1) pixels.
            if (block == 9).any() or (block == 1).any():
                # If it does, set the corresponding output cell to red (2).
                output_grid[i, j] = 2

    return output_grid
```
