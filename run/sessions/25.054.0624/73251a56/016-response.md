# 73251a56 • 016 • refine_coder

---
```python
"""
The transformation rule involves changing white background pixels (color 0) based on their adjacency to non-white pixels. Specifically:

1.  Iterate through each pixel in the input grid.
2.  If a pixel is white (color 0), check its immediate neighbors (up, down, left, and right).
3.  If a white pixel has a non-white neighbor, change the white pixel's value, copying value of neighbor
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Gets the valid neighbors (up, down, left, right) of a pixel.
    """
    rows, cols = grid.shape
    neighbors = []
    
    # Up
    if row > 0:
        neighbors.append(grid[row-1, col])
    # Down
    if row < rows - 1:
        neighbors.append(grid[row+1, col])
    # Left
    if col > 0:
        neighbors.append(grid[row, col-1])
    # Right
    if col < cols - 1:
        neighbors.append(grid[row, col+1])

    return neighbors
    

def transform(input_grid):
    """
    Transforms the input grid by changing white pixels based on neighbors.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # If the pixel is white
            if output_grid[r, c] == 0:
                # Get its neighbors
                neighbors = get_neighbors(input_grid, r, c)
                # Check for non-white neighbors
                for neighbor_val in neighbors:
                    if neighbor_val != 0:
                        output_grid[r,c] = neighbor_val
                        break #stop after finding the first colored neighbor

    return output_grid
```
