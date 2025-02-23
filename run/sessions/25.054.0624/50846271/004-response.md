# 50846271 • 004 • refine_coder

---
```python
"""
Identifies red (2) pixels in the input grid. Changes isolated red pixels (those not
part of a contiguous horizontal or vertical line of red pixels) and red pixels that form
a three-pixel L shape to azure (8). Other pixels remain unchanged.
"""

import numpy as np

def is_isolated(grid, row, col):
    """Checks if a red pixel at (row, col) is isolated."""
    rows, cols = grid.shape
    color = grid[row, col]

    # Check horizontal and vertical neighbors
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            return False  # Has a same-color neighbor
    return True

def is_l_shape(grid, row, col):
    """Checks if a red pixel at (row, col) is the center of a 3-pixel L-shape."""
    rows, cols = grid.shape
    color = grid[row, col]
    neighbors = 0
    
    #check the direct neighbors
    neighbor_coords = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            neighbors += 1
            neighbor_coords.append((nr,nc))

    if neighbors == 2:
        #check if the two neighbors create a vertical or horizontal line, if so it's a line and not an L
        if neighbor_coords[0][0] == neighbor_coords[1][0] or neighbor_coords[0][1] == neighbor_coords[1][1]:
          return False #it's a line of three, not an L
        return True
    
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is red (2)
            if input_grid[row, col] == 2:
                # Check if the red pixel is isolated or part of an L-shape
                if is_isolated(output_grid, row, col) or is_l_shape(output_grid, row, col):
                    # Change isolated red pixels and L-shape centers to azure (8)
                    output_grid[row, col] = 8

    return output_grid
```
