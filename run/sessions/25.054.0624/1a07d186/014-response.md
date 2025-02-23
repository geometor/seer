# 1a07d186 • 014 • example_3 • investigate_coder

---
```python
"""
1. **Identify Key Feature:** Locate the horizontal line of azure (8) pixels that spans the entire width of the grid. This line appears to be constant between input and output and is on row index 5 (counting starts with zero).

2. **Preserve Line:** Keep all pixels on this horizontal line unchanged.

3. **Conditional Removal Above:** For all rows *above* the identified line, any azure (8) or blue (1) pixel which is not within the azure line, is removed (changed to white/0).

4. **Conditional Removal Below:** For rows *below* the identified line, any blue(1) pixels is removed. Azure(8) is removed unless it is directly above or below the azure line of pixels

5. Leave all white(0) pixels as they are.
"""

import numpy as np

def find_azure_line(grid):
    # Find the row index of the horizontal line of azure (8) pixels.
    rows, cols = grid.shape
    for r in range(rows):
        if np.all(grid[r, :] == 8):
            return r
    return -1  # Should not happen in a well-formed case, based on description.


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid.
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find the azure line.
    azure_line_row = find_azure_line(output_grid)

    # Iterate through the grid and apply the rules.
    for r in range(rows):
        for c in range(cols):
            if r == azure_line_row:
                # Preserve the azure line.
                continue
            elif r < azure_line_row:
                # Conditional removal above the line.
                if output_grid[r, c] != 0:
                    output_grid[r,c] = 0
            else:
                # Conditional removal below the line
                if output_grid[r,c] == 1:
                    output_grid[r,c] = 0
                elif output_grid[r,c] == 8:
                    if r != azure_line_row + 1:
                        output_grid[r,c] = 0
    return output_grid
```
