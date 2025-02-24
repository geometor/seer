# 9dfd6313 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify Key Pixels:** Locate all azure (8) pixels in the input grid.
2.  **Horizontal Shift:** Move the azure (8) pixels to the top row, starting from the third column, and preserving the relative positions.
3. **Identify Second key pixels:** Locate all red (2) pixels.
4. **Horizontal Shift and expansion:** Move the red (2) pixels to the right end of the row where the azure pixels are placed, but expand if the red pixels were vertically adjacent by filling two columns on right.
5.  **Retain Other Pixels:** All other pixels retain their original positions in the grid.
"""

import numpy as np

def find_pixels(grid, color):
    """Finds the coordinates of pixels of a specific color."""
    return np.argwhere(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    input_grid_rows, input_grid_cols = input_grid.shape
    output_grid_rows, output_grid_cols = output_grid.shape

    # 1. & 2. Find and move azure (8) pixels
    azure_pixels = find_pixels(input_grid, 8)
    for i, (row, col) in enumerate(azure_pixels):
        output_grid[0, 2 + i] = 8
        if (row,col) != (0, 2 + i): #check for no move
            output_grid[row, col] = 0

    # 3. & 4. Find and move/expand red (2) pixels
    red_pixels = find_pixels(input_grid, 2)
    
    #check if they are vertically aligned
    vertically_aligned = False
    if len(red_pixels) > 1:
        
        first = red_pixels[0]
        for second in red_pixels[1:]:
            if first[1] == second[1] and abs(first[0] - second[0]) == 1:
               vertically_aligned = True
            first = second #move window
        
    if vertically_aligned:
      output_grid[0,output_grid_cols-2] = 2
      output_grid[0,output_grid_cols-1] = 2

      for row, col in red_pixels:
          output_grid[row,col] = 0
    else:
      for i, (row, col) in enumerate(red_pixels):
        output_grid[0, 3 + i] = 2 #will overwrite if 8 is there, will fix
        if (row, col) != (0,3+i): #check for no move
          output_grid[row,col] = 0

    # 5. Retain other pixels (already handled by copying input_grid initially)

    return output_grid
```
