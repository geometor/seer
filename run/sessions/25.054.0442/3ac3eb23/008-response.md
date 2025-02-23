# 3ac3eb23 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Locate the Trigger:** Find the single yellow (4) pixel in the input grid.
2.  **Vertical Oscillation:** In the original trigger's column and a column directly to its left, duplicate that pixel value vertically.
3. **Alternation** Yellow pixels now fill alternating rows in these columns.
"""

import numpy as np

def find_trigger_pixel(grid, trigger_color=4):
    # Find the coordinates of the trigger pixel (color 4).
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == trigger_color:
                return (r, c)
    return None  # Trigger pixel not found

def transform(input_grid):
    # Initialize output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find the trigger pixel.
    trigger_coords = find_trigger_pixel(input_grid)
    
    if trigger_coords is None:
        return output_grid # No trigger pixel, return input grid
    
    trigger_row, trigger_col = trigger_coords

    # Apply vertical oscillation in the trigger column and the column to its left.
    for col in [trigger_col, trigger_col - 1]:
        if 0 <= col < output_grid.shape[1]:  # Ensure column index is within bounds
            for row in range(output_grid.shape[0]):
                if row % 2 == 0:
                  output_grid[row, col] = 4
                else:
                  output_grid[row, col] = 4 if col == trigger_col -1 else 0

    return output_grid
```
