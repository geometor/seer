# 00d62c1b • 002 • example_1 - CODE

---
```python
"""
Identifies adjacent green pixels in a grid and changes the color of appropriate pixel in the output to yellow.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the observed rule:  If two green
    pixels are adjacent, change the color of the pixel from the input green to
    yellow for the output.

    Args:
        input_grid (list of lists): The input grid of pixel values.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is green
            if input_grid[r, c] == 3:
                # Check for adjacent green pixels
                if r > 0 and input_grid[r-1, c] == 3:  # Up
                    output_grid[r,c] = 4
                if r < rows - 1 and input_grid[r+1, c] == 3:  # Down
                    output_grid[r,c] = 4
                if c > 0 and input_grid[r, c-1] == 3:  # Left
                    output_grid[r,c] = 4
                if c < cols - 1 and input_grid[r, c+1] == 3:  # Right
                    output_grid[r,c] = 4

    return output_grid.tolist()
```
