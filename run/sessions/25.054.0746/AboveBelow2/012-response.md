# AboveBelow2 • 012 • refine_coder

---
```python
"""
1.  **Identify Regions:** Find all contiguous regions of red (2), green (3), and any other colors present in the grid.

2.  **Check Red and Green Adjacency:** Determine if any red regions are directly adjacent (not diagonally) to any green regions.

3.  **Conditional Removal (Red and Green):** If any red region is directly adjacent to any green region, remove *both* the red and green regions entirely.

4.  **Conditional Removal (Other Colors):** If *no* red regions are directly adjacent to any green regions, remove all regions of colors other than green(3) and black(0).

5.  **Output:** The output grid contains: black (0), the green regions if no red and green are adjacent, and the other regions if red and green are adjacent.
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

    # Find red and green regions
    red_labeled_array, red_num = find_regions(grid, 2)
    green_labeled_array, green_num = find_regions(grid, 3)

    red_green_adjacent = False

    # check for red and green adjacency
    if red_num > 0 and green_num > 0:
        for i in range(1, red_num+1):
            for j in range(1, green_num+1):
                if are_adjacent_directly(grid, red_labeled_array, i, green_labeled_array, j):
                    red_green_adjacent = True
                    break
            if red_green_adjacent:
               break

    # Conditional removal based on adjacency
    if red_green_adjacent:
       #remove red
        for i in range(1, red_num + 1):
          output_grid[red_labeled_array == i] = 0

       #remove green
        for j in range(1, green_num + 1):
           output_grid[green_labeled_array == j] = 0
    else:
        # Remove all colors other than green and black
        for color in np.unique(grid):
            if color != 3 and color !=0:
                output_grid[grid == color] = 0

    return output_grid.tolist()
```
