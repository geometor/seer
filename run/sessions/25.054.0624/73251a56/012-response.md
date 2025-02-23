# 73251a56 • 012 • refine_coder

---
```python
"""
Identifies and removes contiguous regions of black pixels (value 0) in the input grid, replacing them with the most frequent color in the entire grid, excluding black.
"""

import numpy as np
from scipy.ndimage import label

def get_most_frequent_non_black_color(grid):
    """
    Finds the most frequent color in the grid, excluding black (0).
    """
    colors, counts = np.unique(grid, return_counts=True)
    color_counts = dict(zip(colors, counts))
    
    if 0 in color_counts:
        del color_counts[0]  # Remove black

    if not color_counts:
        return 5 # Default to gray if no other colors exist
        
    # Find the color with the maximum count.
    most_frequent_color = max(color_counts, key=color_counts.get)
    return most_frequent_color

def transform(input_grid):
    """
    Transforms the input grid by removing black regions and replacing them with the most frequent non-black color in the entire grid.

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

    # 2. Determine the most frequent non-black color in the *entire* grid.
    replacement_color = get_most_frequent_non_black_color(input_grid)

    # 3. Replace all black pixels with replacement_color
    for r in range(rows):
        for c in range(cols):
            if labeled_grid[r, c] != 0:  # If the pixel is part of a black region
                output_grid[r,c] = replacement_color

    # 4. Preserve Other Pixels (already handled by initializing output_grid as a copy).
    return output_grid
```
