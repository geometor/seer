# 4-0d3d703e • 006 • example_2 - CODE

---
```python
"""
The transformation rule can be summarized by the following process.
If the input color $c$ is equal to 2, then the new color is $c + 4 \mod 10$.
If the input color $c$ is not equal to 2, then the new color is $c + 1 \mod 10$.

if input[x,y] == 2:
  output[x,y] = (input[x,y] + 4) % 10
else:
  output[x,y] = (input[x,y] + 1) % 10
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
                # Add 4 to the color value, apply modulo 10.
                output_grid[x, y] = (output_grid[x, y] + 4) % 10
            else:
                # Add 1 to the color value, apply modulo 10.
                output_grid[x, y] = (output_grid[x, y] + 1) % 10

    return output_grid
```

