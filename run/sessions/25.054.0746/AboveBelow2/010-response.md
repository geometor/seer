# AboveBelow2 • 010 • refine_coder

---
```python
"""
1.  **Identify Regions:** Locate all contiguous regions of red (2), green (3), and yellow (4) pixels, and any other color present in the grid.

2.  **Check for Red and Green Adjacency:** Determine if any red regions are directly adjacent (not diagonally) to any green regions.

3.  **Conditional Removal (Red and Green):** If a red region and a green region are directly adjacent, remove *both* the red and green regions. Do *not* remove the yellow region, if it is near the green or red.

4. **Conditional Removal (Yellow):** If all of the above regions have been remove, any other color different to black(0), keep.

5.  **Output:** The output grid is the input grid with the specified removals. If no red and green regions are adjacent, the output is the same as the input.
"""

import numpy as np
from scipy.ndimage import label, find_objects

def find_regions(grid, color):
    """Finds contiguous regions of a specific color in the grid."""
    mask = (grid == color)
    labeled_array, num_features = label(mask)
    return labeled_array, num_features

def are_adjacent_directly(grid, labeled_array1, region_index1, labeled_array2, region_index2):
    """Checks if two regions in labeled arrays are adjacent (not diagonally)."""
    # Expand the first region by one pixel in the cardinal directions
    region1_mask = (labeled_array1 == region_index1)
    expanded_region1 = np.zeros_like(region1_mask)
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if region1_mask[r, c]:
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Only cardinal directions
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        expanded_region1[r + dr, c + dc] = True

    # Check for overlap with the second region
    region2_mask = (labeled_array2 == region_index2)
    return np.any(expanded_region1 & region2_mask)

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    output_grid = np.copy(input_grid)
    grid = np.array(input_grid)  # work with numpy array

    # Find red, green and yellow regions
    red_labeled_array, red_num = find_regions(grid, 2)
    green_labeled_array, green_num = find_regions(grid, 3)

    red_green_adjacent = False

    if red_num > 0 and green_num > 0:
        for i in range(1, red_num+1):
            for j in range(1, green_num+1):
                if are_adjacent_directly(grid, red_labeled_array, i, green_labeled_array, j):
                    red_green_adjacent = True
                    break
            if red_green_adjacent:
               break

    if red_green_adjacent:
       #remove red
        for i in range(1, red_num + 1):
          output_grid[red_labeled_array == i] = 0

       #remove green
        for j in range(1, green_num + 1):
           output_grid[green_labeled_array == j] = 0

    return output_grid.tolist()
```

