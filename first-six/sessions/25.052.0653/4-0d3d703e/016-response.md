# 4-0d3d703e • 016 • refine_code - CODE

---
```python
"""
The transformation rule can be summarized by the following process.
Iterate through each cell of the input grid.
If the color value is 2, set the corresponding cell in the output grid to 6.
Otherwise, decrease the input color by 1, except if the input color is 0.
If the input color is 0, keep the output color as 0.

if input[x,y] == 2:
  output[x,y] = 6
else:
  output[x,y] = max(0, input[x,y] - 1)
"""

import numpy as np

def transform(input_grid):
    # Initialize the output grid with the same dimensions as the input grid.
    output_grid = np.copy(input_grid)

    # Iterate through each cell in the grid.
    for x in range(output_grid.shape[0]):
        for y in range(output_grid.shape[1]):
            # Check if the color value is 2.
            if output_grid[x, y] == 2:
                # Set to 6
                output_grid[x, y] = 6
            else:
                # Subtract 1 from the color, except if the original color is 0.
                output_grid[x, y] = max(0, output_grid[x, y] - 1)

    return output_grid
```

