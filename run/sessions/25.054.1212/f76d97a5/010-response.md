# f76d97a5 • 010 • refine_coder

---
```python
"""
1.  **Initial Scan:** Find all gray (5) pixels.
2.  **Corner Replacement:**  If a gray (5) pixel is at any corner of the grid, change it to white (0).
3.  **Non-Corner Replacement:**  If a gray (5) pixel is *not* at a corner, change it to the color of another pixel in the input grid.
4.  **Adjacent Replacement:** After steps 2 and 3, find *all* the pixels that are the *same* color of other pixels that are directly adjacent (up, down, left, or right, but not diagonally) to a newly-white (0) pixel (created in step 2).  Change these adjacent pixels to white (0) as well.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Find non-gray colors
    other_colors = [color for color in np.unique(input_grid) if color != 5]
    if len(other_colors) == 0: # Handle edge case where input is all gray.
        other_color = 0
    else:
        other_color = other_colors[0]

    # Corner and Non-Corner Replacement of Gray (5)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 5:
                if (r == 0 and c == 0) or \
                   (r == 0 and c == cols - 1) or \
                   (r == rows - 1 and c == 0) or \
                   (r == rows - 1 and c == cols - 1):
                    output_grid[r, c] = 0  # Corner replacement
                else:
                    output_grid[r, c] = other_color # Non-corner replacement

    # Adjacent Replacement (create a copy to avoid modifying during iteration)
    new_output_grid = np.copy(output_grid)
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] == 0: #check neighbors
                if r > 0 and output_grid[r-1,c] == other_color: #up
                    new_output_grid[r-1,c] = 0
                if r < rows-1 and output_grid[r+1,c] == other_color: #down
                    new_output_grid[r+1,c] = 0
                if c > 0 and output_grid[r,c-1] == other_color: #left
                    new_output_grid[r,c-1] = 0
                if c < cols-1 and output_grid[r,c+1] == other_color: #right
                    new_output_grid[r,c+1] = 0
    
    return new_output_grid
```

