# d4469b4b • 020 • example_4 • investigate_coder

---
```python
"""
Condenses a 5x5 grid into a 3x3 grid. Each cell in the output grid represents a 3x3 region in the input. If a 3x3 region in the input contains at least one blue pixel (1), the corresponding output cell is gray (5). Otherwise, it's white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms a 5x5 input grid into a 3x3 output grid based on the presence of '1's in 3x3 subgrids.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros((3, 3), dtype=int)

    # Iterate through each cell of the output grid
    for row in range(3):
        for col in range(3):
            # Define the corresponding 3x3 region in the input grid
            start_row = row
            end_row = row + 3
            start_col = col
            end_col = col + 3

            # Extract the 3x3 region
            region = input_grid[start_row:end_row, start_col:end_col]

            # Check if at least one '1' (blue pixel) exists in the region
            if 1 in region:
                output_grid[row, col] = 5  # Set to gray (5)
            else:
                output_grid[row, col] = 0  # Set to white (0)

    return output_grid.tolist()
```
