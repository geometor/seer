# c1d99e64 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Starting Points:** Locate all white (0) pixels that are directly adjacent (above, below, left, or right) to a green (3) pixel.
2. **Horizontal Replacement - Row by row:**
      - Every row which contain the green color, change every 0 to 2 in the same row starting from the top.
3.  **Leave Other Pixels Unchanged:** All green (3) pixels, and any white(0) that do not satisfy conditions from horizontal replacement, remain the same.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Finds the valid neighbors of cell.
    """
    rows, cols = grid.shape
    neighbors = []
    
    # Define possible neighbor coordinates
    possible_neighbors = [
        (row - 1, col),  # Above
        (row + 1, col),  # Below
        (row, col - 1),  # Left
        (row, col + 1)   # Right
    ]
    
    # Check validity
    for r, c in possible_neighbors:
      if 0 <= r < rows and 0 <= c < cols:
        neighbors.append((r,c))

    return neighbors
        

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid
    for row in range(rows):
        has_green = False  # Flag to check for the presence of green in each row
        for col in range(cols):
            if output_grid[row, col] == 3:  # Found green pixel
               has_green = True
               break # We only need to check green pixel on each row.

        if (has_green):
            # Replace the 0 to 2 in the same row.
            for col_2 in range(cols):
                if output_grid[row,col_2] == 0:
                    output_grid[row,col_2] = 2
    return output_grid
```
