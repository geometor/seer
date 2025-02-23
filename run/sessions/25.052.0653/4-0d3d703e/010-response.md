# 4-0d3d703e • 010 • example_3 - CODE

---
```python
"""
The transformation rule can be summarized by the following process.
If the input color $c$ is equal to 5, then the new color is $(c + 6) \mod 10$.
If the input color $c$ is equal to 6, then the new color is $(c - 4) \mod 10$.
Otherwise, the new color is $(c + 1) \mod 10$.

if input[x,y] == 5:
  output[x,y] = (input[x,y] + 6) % 10
else if input[x,y] == 6:
  output[x,y] = (input[x,y] - 4)
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
            # Check if the color value is 5.
            if output_grid[x, y] == 5:
                # Add 6 to the color value, apply modulo 10.
                output_grid[x, y] = (output_grid[x, y] + 6) % 10
            # Check if the color value is 6.
            elif output_grid[x,y] == 6:
                output_grid[x,y] = (output_grid[x,y] + 6) % 10
            else:
                # Add 1 to the color value, apply modulo 10.
                output_grid[x, y] = (output_grid[x, y] + 1) % 10

    return output_grid
```

