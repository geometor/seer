# 1e0a9b12 • 012 • refine_coder

---
```python
"""
1.  **Identify Objects:** Treat each individual pixel in the input grid as a separate object.

2.  **Iterative Shift Down:** For each object (pixel), attempt to move it down one row at a time. Continue moving the object down until it reaches the bottom row or encounters another object (any non-empty cell) directly below it.

3. **Bottom-Right (Maroon):** If a maroon colored object (value 9) exists in the grid, move it to the bottom-right cell of the grid. Any object that had that location is removed. The maroon object is removed from its previous position.
"""

import numpy as np

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterative Shift Down
    for c in range(cols):
        for r in range(rows - 1, -1, -1):
            if output_grid[r,c] != 0: # if not empty
                current_row = r
                while current_row < rows - 1 and output_grid[current_row + 1, c] == 0:
                    # Move down as long as the space below is empty.
                    output_grid[current_row + 1, c] = output_grid[current_row, c]
                    output_grid[current_row, c] = 0
                    current_row += 1


    # Bottom Right (Maroon 9)
    maroon_present = False
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 9:
                maroon_present = True
                output_grid[r, c] = 0  # Clear the original maroon position
                break
        if maroon_present:
            break

    if maroon_present:
        output_grid[rows - 1, cols - 1] = 9

    return output_grid
```
