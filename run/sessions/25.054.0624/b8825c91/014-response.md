# b8825c91 • 014 • example_3 • investigate_coder

---
```python
"""
The transformation preserves everything outside a central diamond shape and selectively changes colors only *within* that diamond. 
It appears to be two different color changes, one affecting the inner cross, the other affecting the rest, including the border.
Specifically, the yellow (4) pixels in the original border are replaced with maroon (9).
The internal plus is recolored, orange (7) to blue (1) and yellow (4) to maroon (9).
"""

import numpy as np

def find_diamond_center(grid):
    # Find the center of the grid
    center_row, center_col = grid.shape[0] // 2, grid.shape[1] // 2
    return center_row, center_col

def is_inside_diamond(row, col, center_row, center_col, size):
    # Determine if a given cell is within the diamond, the size correlates with number of rings
    dist_row = abs(row - center_row)
    dist_col = abs(col - center_col)
    return dist_row + dist_col <= size

def get_diamond_size(grid):
    # for this specific type of problem where a well defined object has clear borders and can have multiple "rings",
    # the max size is useful to determine how big an object we need to look at
    # Find diamond center
    center_row, center_col = find_diamond_center(grid)

    # expand outward to estimate the size/radius
    max_size = min(center_row, center_col)
    
    return max_size

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    grid = input_grid
    # Find diamond center
    center_row, center_col = find_diamond_center(grid)

    # expand outward to estimate the size/radius
    size = get_diamond_size(grid)

    # Iterate through each cell of the grid
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            # Check if the cell is inside the diamond
            if is_inside_diamond(row, col, center_row, center_col, size):
                # Apply color transformations inside the diamond
                if (abs(row - center_row) + abs(col-center_col)) <= 2 :
                    if grid[row, col] == 7:
                        output_grid[row, col] = 1
                    elif grid[row, col] == 4:
                        output_grid[row, col] = 9
                elif grid[row,col] == 4:
                        output_grid[row,col] = 2

    return output_grid
```
