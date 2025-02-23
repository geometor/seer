# 1-3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Lines:** Find all horizontal, contiguous lines of azure (8) pixels. A line is defined by its starting row, starting column, and ending column.
2.  **Check for Edge Contact:** For each azure line:
    *   If the line's ending column is *not* the last column of the grid (right edge), place a single blue (1) pixel immediately to the right of the line's last pixel.
    *   If the line's starting column is *not* the first column of the grid (left edge), place a single blue (1) pixel immediately to the left of the line's first pixel.
3. **All other pixels:** should be set to 0 (white).
4.  **Output Grid:** Create a new grid containing only the azure lines and any newly placed blue pixels, all other cells are zero.
"""

import numpy as np

def find_azure_lines(grid):
    azure_lines = []
    for row_index, row in enumerate(grid):
        start = -1
        for col_index, pixel in enumerate(row):
            if pixel == 8:
                if start == -1:
                    start = col_index
            elif start != -1:
                azure_lines.append((row_index, start, col_index - 1))
                start = -1
        if start != -1:  # Check for line at the end of the row
            azure_lines.append((row_index, start, len(row) - 1))
    return azure_lines

def transform(input_grid):
    # initialize output_grid as all zeros
    output_grid = np.zeros_like(input_grid)

    # Find all horizontal azure lines
    azure_lines = find_azure_lines(input_grid)
    
    # Iterate through the lines and place blue pixels
    for row, start_col, end_col in azure_lines:
        # Place azure pixels
        output_grid[row, start_col:end_col+1] = 8
        
        # Check right edge
        if end_col < input_grid.shape[1] - 1:
            output_grid[row, end_col + 1] = 1
        # Check left edge
        if start_col > 0:
            output_grid[row, start_col - 1] = 1

    return output_grid
```

