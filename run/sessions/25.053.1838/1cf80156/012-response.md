# 1cf80156 • 012 • refine_coder

---
```python
"""
1.  **Identify the Target Object:** Find the largest connected component (contiguous block of pixels) of a single, non-white (non-zero) color within the input grid. The color of the object varies from example.
2.  **Precise Cropping:** Determine the smallest rectangular region that *exactly* encloses the target object identified in step 1. This bounding box should not include any extra rows or columns of white (0) pixels that are not part of the object itself. It seems that in cases where there are multiple connected components of the target color, we want to find the largest.
3.  **Extract:**  Create the output grid by extracting the pixels within the determined bounding box from the input grid.
"""

import numpy as np
from scipy.ndimage import label

def find_largest_connected_component(grid):
    """Finds the largest connected component in a grid."""
    labeled_grid, num_features = label(grid)
    if num_features == 0:
        return np.zeros_like(grid), 0  # Return empty grid if no features

    component_sizes = np.bincount(labeled_grid.ravel())
    largest_component_label = np.argmax(component_sizes[1:]) + 1  # +1 because 0 is background
    largest_component = (labeled_grid == largest_component_label).astype(int)
    return largest_component, np.max(largest_component)

def get_bounding_box(grid):
    """Calculates the bounding box of a non-zero region in a grid."""
    rows = np.any(grid, axis=1)
    cols = np.any(grid, axis=0)
    if not np.any(rows) or not np.any(cols):
        return 0, 0, 0, 0  # Handle empty grid case
    min_row, max_row = np.where(rows)[0][[0, -1]]
    min_col, max_col = np.where(cols)[0][[0, -1]]
    return min_row, max_row, min_col, max_col
    

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # 1. Identify the Target Object (find largest connected component of each color)
    non_white_colors = [color for color in np.unique(input_grid) if color != 0]
    largest_component = np.zeros_like(input_grid)
    largest_size = 0

    for color in non_white_colors:
      colored_grid = (input_grid == color).astype(int)
      component, component_size = find_largest_connected_component(colored_grid)

      if component_size > largest_size:
        largest_size = component_size
        largest_component = component * color

    
    # 2. Precise Cropping
    min_row, max_row, min_col, max_col = get_bounding_box(largest_component)
    
    # 3. Extract
    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]
    output_grid = np.where(output_grid != 0, output_grid, 0)
    
    # handle all zero outputs
    if output_grid.size == 0:
        return []

    return output_grid.tolist()
```
