# 73251a56 • 010 • refine_coder

---
```python
"""
Identifies and removes contiguous regions of black pixels (value 0) in the input grid, replacing them with the most frequent neighboring non-black color, while preserving other pixels.
"""

import numpy as np
from scipy.ndimage import label

def get_neighboring_color(grid, r, c):
    """
    Finds the most frequent neighboring color around a given pixel, excluding black (0).
    """
    neighbors = []
    rows, cols = grid.shape
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i != r or j != c) and grid[i, j] != 0:  # Exclude the pixel itself and black pixels
                neighbors.append(grid[i, j])

    if not neighbors:
      return 5
      
    # return most common neighbor
    return max(set(neighbors), key=neighbors.count)

def transform(input_grid):
    """
    Transforms the input grid by removing black regions and replacing them with the most frequent neighboring non-black color.

    Args:
        input_grid: A 2D numpy array representing the input grid.

    Returns:
        A 2D numpy array representing the transformed output grid.
    """
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Black Regions: Use scipy.ndimage.label to find connected components.
    labeled_grid, num_labels = label(input_grid == 0)

    # 2. & 3. Replace Black Regions with the surrounding color.
    for r in range(rows):
        for c in range(cols):
            if labeled_grid[r, c] != 0:  # If the pixel is part of a black region
                output_grid[r,c] = get_neighboring_color(input_grid,r,c)

    # 4. Preserve Other Pixels (already handled by initializing output_grid as a copy).
    return output_grid
```
