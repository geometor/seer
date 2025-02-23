# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
1.  **Identify Azure Pixels:** Locate all pixels with the value 8 (azure) in the input grid.
2.  **Mark Adjacent Cells:** For each identified azure pixel, examine its neighboring cells (up, down, left, and right).
    - if an azure pixel is to the right of another azure pixel, place a blue pixel to its immediate right
    - if an azure pixel is to the left of another azure pixel, place a blue pixel to its immediate left
3.  **Output:** Create the output grid with the original azure pixels and the newly placed blue (1) pixels. All other cells remain white (0).
"""

import numpy as np

def find_pixels_by_color(grid, color):
    return np.argwhere(grid == color)

def transform(input_grid):
    # initialize output_grid as a copy of the input grid
    output_grid = input_grid.copy()
    
    # Find the locations of all azure (8) pixels
    azure_pixels = find_pixels_by_color(input_grid, 8)
    
    # Iterate and mark adjacent cells based on the rules
    for row, col in azure_pixels:
        #check to right
        if col + 1 < input_grid.shape[1] and input_grid[row, col + 1] == 8:
            if col+2 < input_grid.shape[1]:
                output_grid[row,col+2] = 1
        #check to left
        if col - 1 >= 0 and input_grid[row, col - 1] == 8:
            if col - 2 >= 0:
                output_grid[row,col-2] = 1


    return output_grid
```
