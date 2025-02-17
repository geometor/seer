# 2-0ca9ddb6 • 002 • Response

---

*text:*

```python
"""
This script implements the transformation rule described as follows:

1. **Identify Key Objects:** Locate the single red (color 2) pixel and the single blue (color 1) pixel in the input grid.
2. **Red Surroundings:** For the red pixel, change the color of the pixels immediately above, below, to the left, and right to the color yellow (value 4).
3. **Blue Surroundings:** For the blue pixel, change the color of the pixels immediately above, below, to the left, and right to the color orange (value 7).
4. **Preservation:** The positions of the original red and blue pixel are preserved.
5. **Background:** All other pixels remain unchanged (color 0).
"""

import numpy as np

def find_pixel(grid, color):
    """Finds the coordinates of a single pixel of the specified color."""
    coords = np.where(grid == color)
    if len(coords[0]) > 0:  # Check if any pixels of the color were found
        return (coords[0][0], coords[1][0])  # Return first occurrence
    return None

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    
    output_grid = np.copy(input_grid)
    
    # Find the red pixel (color 2)
    red_pixel = find_pixel(input_grid, 2)
    if red_pixel:
        row, col = red_pixel
        # Change surrounding pixels to yellow (color 4)
        if row > 0:
            output_grid[row - 1, col] = 4  # Above
        if row < input_grid.shape[0] - 1:
            output_grid[row + 1, col] = 4  # Below
        if col > 0:
            output_grid[row, col - 1] = 4  # Left
        if col < input_grid.shape[1] - 1:
            output_grid[row, col + 1] = 4  # Right
            
    # Find the blue pixel (color 1)
    blue_pixel = find_pixel(input_grid, 1)
    if blue_pixel:
        row, col = blue_pixel
       # Change surrounding pixels to orange (color 7)
        if row > 0:
            output_grid[row - 1, col] = 7  # Above
        if row < input_grid.shape[0] - 1:
            output_grid[row + 1, col] = 7  # Below
        if col > 0:
            output_grid[row, col - 1] = 7  # Left
        if col < input_grid.shape[1] - 1:
            output_grid[row, col + 1] = 7  # Right

    return output_grid
```
