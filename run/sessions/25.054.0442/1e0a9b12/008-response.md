# 1e0a9b12 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule is as follows:
1. Identify the maroon (9) pixel and the azure (8) pixel in the input grid.
2. Move the maroon (9) pixel to the bottom right corner of the grid.
3. Move the azure (8) pixel to the position that was vacated by the maroon (9) pixel.
4. All other object locations remain in the original input.
"""

import numpy as np

def find_pixel_by_color(grid, color):
    # Find the coordinates of a pixel with a specific color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    
    # Find the maroon (9) pixel
    maroon_pixel_pos = find_pixel_by_color(input_grid, 9)
    
    # Find the azure (8) pixel
    azure_pixel_pos = find_pixel_by_color(input_grid, 8)

    # Move maroon (9) to bottom right
    if maroon_pixel_pos:
        output_grid[maroon_pixel_pos] = input_grid[input_grid.shape[0]-1, input_grid.shape[1]-1]  #put whatever was in bottom corner where 9 was
        output_grid[input_grid.shape[0]-1, input_grid.shape[1]-1] = 9

    # Move azure (8) to original maroon (9) position.
    if maroon_pixel_pos and azure_pixel_pos:
        output_grid[azure_pixel_pos] = input_grid[maroon_pixel_pos] #put the value of old 9 location into 8 location in output
        output_grid[maroon_pixel_pos] = 8 # place 8 in old 9 location

    return output_grid
```
