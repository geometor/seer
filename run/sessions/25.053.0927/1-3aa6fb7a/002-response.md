# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
1.  **Identify** all pixels with the value `8` (azure) in the input grid.
2.  **Preserve** all of these azure pixels in their original positions in the output grid.
3. **Introduce** a blue pixel (value 1) to the right of the azure pixel
4. **Introduce** a blue pixel to the left of the azure pixel.
5.  **Fill** all other positions in the output grid with `0` (white).
"""

import numpy as np

def get_positions(grid, value):
    return np.argwhere(grid == value)

def transform(input_grid):
    # Initialize output_grid with zeros (white)
    output_grid = np.zeros_like(input_grid)
    
    # Get positions of azure pixels (value 8)
    azure_positions = get_positions(input_grid, 8)
    
    # Preserve azure pixels in the output grid
    for pos in azure_positions:
        output_grid[pos[0], pos[1]] = 8

    # Introduce blue pixels (value 1) adjacent to azure pixels
    for pos in azure_positions:
        # to the right
        if pos[1] + 1 < output_grid.shape[1]:
          output_grid[pos[0],pos[1] + 1] = 1
        # to the left
        if pos[1] - 1 >= 0:
          output_grid[pos[0], pos[1] - 1] = 1
    
    return output_grid
```

