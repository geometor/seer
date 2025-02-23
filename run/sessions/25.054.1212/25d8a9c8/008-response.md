# 25d8a9c8 • 008 • example_2 • investigate_coder

---
```python
"""
Iterates through each cell of the input grid.
Checks if the cell is in the middle row.
If the cell is in the middle row, sets its value to 5 (gray).
Otherwise, sets the cell's value to 0 (white).
The output grid has the same dimensions as the input grid.
"""

import numpy as np

def transform(input_grid):
    # Create an output grid with the same dimensions as the input, filled with zeros (white).
    output_grid = np.zeros_like(input_grid)
    
    # Get the number of rows in the grid.
    rows = input_grid.shape[0]
    
    # Calculate the index of the middle row.
    middle_row_index = rows // 2

    # Iterate through each cell of the input grid.
    for i in range(rows):
        for j in range(input_grid.shape[1]):
            # Check if the current cell is in the middle row.
            if i == middle_row_index:
                # Set the corresponding cell in the output grid to 5 (gray).
                output_grid[i, j] = 5
            # else leave as zero (which is the initialization)
            
    return output_grid
```

