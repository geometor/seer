# 00d62c1b • 010 • example_5 - CODE

---
```python
"""
The transformation identifies a contiguous object composed of green (3) cells.
It then changes the color of any green cell that is surrounded on all four
cardinal directions (up, down, left, right) by other green cells to yellow (4).
"""

import numpy as np

def find_object(grid, color):
    """Finds the positions of cells of a specific color."""
    positions = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color:
                positions.append((i, j))
    return positions

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the positions of the green (3) cells
    green_positions = find_object(input_grid, 3)

    # Iterate through green positions to check for surrounded cells
    for pos in green_positions:
      i, j = pos
      
      # Check boundaries to avoid index errors
      if (i > 0 and i < input_grid.shape[0] - 1) and \
          (j > 0 and  j < input_grid.shape[1] - 1) :
          
        # Check if the cell is surrounded by green cells
        if input_grid[i-1,j] == 3 and input_grid[i+1, j] == 3 and \
          input_grid[i,j-1] == 3 and input_grid[i, j+1] == 3:
            output_grid[i,j] = 4
            

    return output_grid
```

