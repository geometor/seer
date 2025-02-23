# AboveBelow2 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Colored Regions:** Locate all contiguous regions of red (2), green (3), and yellow (4) pixels in the input grid.

2.  **Check for Red/Green Adjacency :** Examine whether or not any red(2) regions and green(3) regions touch.

3.  **Conditional Removal (Red and Green):** If there are no touching red and green regions, the input equals the output, and no further action must be taken.

4. **Conditional Removal(Yellow):** If there is yellow(4) region near either the red or green, remove it.

5.  **Output:** The output grid is the result of applying these removal rules to the input grid.
"""

import numpy as np
from scipy.ndimage import label, find_objects

def find_regions(grid, color):
    """Finds contiguous regions of a specific color in the grid."""
    mask = (grid == color)
    labeled_array, num_features = label(mask)
    return labeled_array, num_features

def are_adjacent(grid, labeled_array1, region_index1, labeled_array2, region_index2):
    """Checks if two regions in labeled arrays are adjacent."""
    # Expand the first region by one pixel in all directions
    region1_mask = (labeled_array1 == region_index1)
    expanded_region1 = np.zeros_like(region1_mask)
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if region1_mask[r, c]:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
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
    yellow_labeled_array, yellow_num = find_regions(grid, 4)

    red_green_adjacent = False

    if red_num > 0 and green_num > 0:
        for i in range(1, red_num+1):
            for j in range(1, green_num+1):
                if are_adjacent(grid, red_labeled_array, i, green_labeled_array, j):
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

       #remove yellow
        for k in range(1, yellow_num + 1):
           output_grid[yellow_labeled_array == k] = 0

    return output_grid.tolist()
```
