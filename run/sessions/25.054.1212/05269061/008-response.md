# 05269061 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid with a diagonal sequence of numbers (1, 2, 4) and 0s into an output grid with a repeating checkerboard-like pattern of 1, 2, and 4, maintaining the original positions of 1, 2, and 4 from the input.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid with the same dimensions as input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    
    # Initialize the starting value for the sequence
    prev_val = 4

    # Iterate through each cell of the grid
    for i in range(rows):
        for j in range(cols):
            # If the input cell is 0, fill with the repeating pattern
            if input_grid[i, j] == 0:
                if (i + j) % 2 == 0:  # Even sum of indices
                    if prev_val == 1:
                        output_grid[i,j] = 2
                        prev_val = 2
                    elif prev_val == 2:
                        output_grid[i,j] = 4
                        prev_val = 4
                    elif prev_val == 4:
                        output_grid[i,j] = 1
                        prev_val = 1
                else:  # Odd sum of indices
                    if prev_val == 1:
                        output_grid[i,j] = 2
                        prev_val = 2
                    elif prev_val == 2:
                        output_grid[i,j] = 4
                        prev_val = 4
                    elif prev_val == 4:
                        output_grid[i,j] = 1
                        prev_val = 1

            else:
                prev_val = input_grid[i,j] # set sequence start based on input



    return output_grid
```
