# 1-3aa6fb7a • 002 • Response

---

*text:*

```python
"""
The task is to identify connected regions of color '8' in the input grid. For each such region, a transformation is applied based on its vertical position in the grid.

1. **Identify Connected Regions:** Find all groups of connected cells that have the color '8'. Connectivity is defined as being adjacent horizontally or vertically.
2. **Calculate Average Row Index for Each Region:** For each connected region, calculate the average row index of all cells belonging to that region.
3. **Determine Transformation Rule based on Average Row Index:**
    - Calculate a threshold row index as the integer division of the grid height by 2. In this case, grid height is 7, so the threshold is 7 // 2 = 3.
    - **If the average row index of a region is less than the threshold (3):**
        a. Find the topmost row that contains any cell of this region.
        b. Within this topmost row, find the cell with the smallest column index that belongs to the region. Let's call this cell the "top-leftmost" cell.
        c. Change the color of the cell immediately to the right of this "top-leftmost" cell to '1', provided that this neighbor is within the grid boundaries.
    - **Otherwise (if the average row index is greater than or equal to the threshold 3):**
        a. Find the bottommost row that contains any cell of this region.
        b. Within this bottommost row, find the cell with the largest column index that belongs to the region. Let's call this cell the "bottom-rightmost" cell.
        c. Change the color of the cell immediately to the left of this "bottom-rightmost" cell to '1', provided that this neighbor is within the grid boundaries.
"""

import numpy as np
from scipy.ndimage import measurements

def find_connected_regions(grid, color):
    """
    Finds connected regions of a specific color in the grid.

    Args:
        grid: The input grid.
        color: The color to find connected regions for.

    Returns:
        A list of coordinates, where each coordinate set represents a connected region.
    """
    labeled_grid, num_labels = measurements.label(grid == color)
    regions = []
    for label in range(1, num_labels + 1):
        regions.append(np.array(np.where(labeled_grid == label)).T)
    return regions

def calculate_average_row_index(region):
    """
    Calculates the average row index of a region.

    Args:
        region: A list of coordinates representing the region.

    Returns:
        The average row index.
    """
    return np.mean(region[:, 0])

def transform(input_grid):
    """
    Transforms the input grid according to the specified rules.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    regions = find_connected_regions(input_grid, 8)
    threshold = input_grid.shape[0] // 2

    for region in regions:
        avg_row_index = calculate_average_row_index(region)

        if avg_row_index < threshold:
            # Topmost row
            topmost_row = np.min(region[:, 0])
            # Top-leftmost cell in the topmost row
            top_leftmost_col = np.min(region[region[:, 0] == topmost_row, 1])
            # Change the cell to the right to '1' if within bounds
            if top_leftmost_col + 1 < output_grid.shape[1]:
                output_grid[topmost_row, top_leftmost_col + 1] = 1
        else:
            # Bottommost row
            bottommost_row = np.max(region[:, 0])
            # Bottom-rightmost cell in the bottommost row
            bottom_rightmost_col = np.max(region[region[:, 0] == bottommost_row, 1])
            # Change the cell to the left to '1' if within bounds
            if bottom_rightmost_col - 1 >= 0:
                output_grid[bottommost_row, bottom_rightmost_col - 1] = 1

    return output_grid
```
