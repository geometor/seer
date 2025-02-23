# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The task is to modify the input grid by identifying connected regions of azure color (color 8) and adding a blue cell (color 1) adjacent to each region. The placement of the blue cell depends on whether the azure region is "left-leaning" or "right-leaning" based on its shape.

Here's the step-by-step transformation rule:

1.  **Identify Azure Regions:** Find all connected components of cells with color 8 in the input grid. Each connected component is considered an independent azure region.
2.  **Analyze Each Region:** For each identified azure region, perform the following steps:
    a. **Determine Bounding Box:** Find the smallest rectangle that encloses the azure region. This is defined by the minimum row (min_r), minimum column (min_c), maximum row (max_r), and maximum column (max_c) indices of the cells in the region.
    b. **Calculate Centroid Column:** Calculate the average column index of all cells in the azure region.
    c. **Calculate Bounding Box Center Column:** Calculate the average of the minimum column (min_c) and maximum column (max_c) of the bounding box.
    d. **Compare Centroid Column and Bounding Box Center Column:**
        - **If the Centroid Column is greater than the Bounding Box Center Column:** The region is considered "right-leaning". Place a blue cell (color 1) at the position with row index equal to the minimum row of the bounding box (min_r) and column index equal to the minimum column of the bounding box (min_c).
        - **If the Centroid Column is less than or equal to the Bounding Box Center Column:** The region is considered "left-leaning" or centered. Place a blue cell (color 1) at the position with row index equal to the minimum row of the bounding box (min_r) and column index immediately to the right of the maximum column of the bounding box (max_c + 1).
    e. **Preserve Azure Region:** Ensure that the azure region itself remains unchanged in the output grid.
3.  **Maintain Background:** All cells in the input grid that are not part of any azure region and are not modified by step 2.d, remain white (color 0) in the output grid.

This process is applied independently to each connected azure region in the input grid to produce the final output grid.
"""

import numpy as np
from collections import deque

def find_objects(grid, color):
    """Find connected regions of a specific color."""
    visited = set()
    objects = []

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        region = []

        while queue:
            r, c = queue.popleft()
            region.append((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and grid[nr, nc] == color and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return region

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(bfs(r, c))
    return objects

def bounding_box(region):
    """Calculate the bounding box of a region."""
    min_r, min_c = float('inf'), float('inf')
    max_r, max_c = float('-inf'), float('-inf')
    for r, c in region:
        min_r = min(min_r, r)
        min_c = min(min_c, c)
        max_r = max(max_r, r)
        max_c = max(max_c, c)
    return min_r, min_c, max_r, max_c

def centroid_column(region):
    """Calculate the average column index of a region."""
    sum_c = 0
    for _, c in region:
        sum_c += c
    return sum_c / len(region)

def bounding_box_center_column(bbox):
    """Calculate the center column of the bounding box."""
    _, min_c, _, max_c = bbox
    return (min_c + max_c) / 2

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for region in azure_objects:
        # Calculate bounding box
        bbox = bounding_box(region)
        # Calculate centroid column
        cen_c = centroid_column(region)
        # Calculate bounding box center column
        bbox_center_c = bounding_box_center_column(bbox)

        # Compare centroid column and bounding box center column
        if cen_c > bbox_center_c:  # Right-leaning
            # Place blue cell at (min_r, min_c)
            output_grid[bbox[0], bbox[1]] = 1
        else:  # Left-leaning or centered
            # Place blue cell at (min_r, max_c + 1)
             # Ensure we don't go out of bounds
            if bbox[0] < output_grid.shape[0] and bbox[3] + 1 < output_grid.shape[1]:
                output_grid[bbox[0], bbox[3] + 1] = 1

    return output_grid
```
