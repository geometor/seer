# 0a938d79 • 026 • example_4 - CODE

---
```python
"""
1.  **Identify Key Rows:** In the input grid, locate the rows containing the non-zero colored pixels. In this case, find the row with the yellow pixel (4) and the row with the blue pixel (1).
2.  **Expand:** Expand the non zero values across the entire row.
3.  **Replicate and Position:**
    *   Copy the expanded yellow row and repeat the expanded row every 8 rows, starting at its original row index.
    *   Copy the expanded blue row and repeat it every 8 rows starting with the original row.
4.  **Fill Remaining Rows:** All other rows in the output grid remain unchanged from the input (filled with 0s).
"""

import numpy as np

def find_colored_rows(grid):
    # Find rows with non-zero (colored) pixels.
    colored_rows = {}
    for i, row in enumerate(grid):
        for pixel in row:
            if pixel != 0:
                colored_rows[i] = pixel  # Store row index and color
                break  # Only need the first color in the row
    return colored_rows

def expand_row(row, color):
    # replace all 0 with the non zero color
    return np.array([color if pixel !=0 else 0 for pixel in row])

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find the rows with colors and their respective colors.
    colored_rows = find_colored_rows(input_grid)

    # Iterate through the colored rows and perform expansion and replication.
    for row_index, color in colored_rows.items():
        # expand the row
        expanded = expand_row(input_grid[row_index], color)
        
        # Replicate and position the expanded row.
        current_index = row_index
        while current_index < rows:
            output_grid[current_index] = expanded
            current_index += 8

    return output_grid
```

