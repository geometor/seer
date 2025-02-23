# AboveBelow8 • 010 • refine_coder

---
```python
"""
The transformation preserves only interior azure (color 8) pixels. An interior pixel is defined as a pixel that has azure neighbors on all four cardinal directions (up, down, left, and right). All other pixels, including non-interior azure pixels and pixels of any other color, are set to white (0).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid, keeping only interior azure pixels and setting others to white.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the input grid
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is azure
            if input_grid[row, col] == 8:
                # Check if it's an interior pixel
                is_interior = True
                # Check neighbors (up, down, left, right)
                if row <= 0 or input_grid[row - 1, col] != 8:  # Up
                    is_interior = False
                if row >= rows - 1 or input_grid[row + 1, col] != 8:  # Down
                    is_interior = False
                if col <= 0 or input_grid[row, col - 1] != 8:  # Left
                    is_interior = False
                if col >= cols - 1 or input_grid[row, col + 1] != 8:  # Right
                    is_interior = False

                # Keep only interior azure pixels
                if is_interior:
                    output_grid[row, col] = 8

    return output_grid.tolist()
```
