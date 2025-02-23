# 6-0520fde7 • 010 • example_2 - CODE

---
```python
"""
1.  **Locate:** Find the single vertical line of gray (5) pixels in the input grid.
2.  **Extract:** take the values directly to the left and right of the center line of the input
3.  **Translate**: translate all the 1s (blue) to 2s (red). all other numbers become 0
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the x-coordinate of a vertical line of the specified color."""
    height, width = grid.shape
    for x in range(width):
        is_line = True
        for y in range(height):
            if grid[y, x] != color:
                is_line = False
                break
        if is_line:
            return x
    return -1  # Return -1 if no line is found

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    height, width = input_grid.shape
    output_grid = np.zeros((height, 3), dtype=int)

    # Find the vertical line of gray (5) pixels
    center_x = find_vertical_line(input_grid, 5)

    # Extract the columns to the left and right of the center
    if center_x != -1:
        # change output pixels 
        for y in range(height):
            if center_x > 0 :
                output_grid[y, 0] = input_grid[y, center_x -1]
            output_grid[y, 1] = input_grid[y, center_x] #this should stay 0
            if center_x < width -1:
                output_grid[y, 2] = input_grid[y, center_x + 1]
    
    # Translate 1s to 2s, and other non-zero to 0
    for y in range(height):
        for x in range(3):
            if output_grid[y,x] == 1:
                output_grid[y,x] = 2
            elif output_grid[y,x] != 0:
                output_grid[y, x] = 0

    return output_grid.tolist()
```
