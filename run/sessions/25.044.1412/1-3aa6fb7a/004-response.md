# 25.044.1412 • 1-3aa6fb7a • 004 Response

---

*text:*

```python
"""
1. Identify Connected Regions: Detect all distinct, connected regions formed by cells with value '8' in the input grid.
2. Determine Bounding Boxes: For each of these regions, calculate the smallest bounding box that encloses all cells of the region.
3. Order Regions: Order the regions based primarily on the top row index of their bounding boxes, and secondarily on the left column index in case of a tie in top row indices, to determine the first, second, and subsequent regions.
4. Modify First Region: For the first ordered region, locate the cell diagonally down and to the left from the top-right corner of its bounding box. Specifically, if the top-right corner is at row `r` and column `c`, examine the cell at `(r+1, c-1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
5. Modify Second Region: For the second ordered region, locate the cell diagonally up and to the right from the bottom-left corner of its bounding box. Specifically, if the bottom-left corner is at row `r` and column `c`, examine the cell at `(r-1, c+1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
6. Modify Third Region: For the third ordered region, locate the cell diagonally up and to the left from the bottom-right corner of its bounding box. Specifically, if the bottom-right corner is at row `r` and column `c`, examine the cell at `(r-1, c-1)`. If this cell exists within the grid boundaries and its value is '0', change its value to '1'.
7. Preserve Unchanged Cells: All cells in the grid that are not modified in steps 4, 5, and 6 retain their original values from the input grid.
"""

import numpy as np
from collections import deque

input_grid = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

expected_output = [
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
]

def transform(input_grid):
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0
    grid = np.array(input_grid).copy() # Create a copy to avoid modifying the input

    regions = []
    visited = np.zeros_like(grid, dtype=bool)

    # Function to perform BFS for finding connected regions
    def find_region(r, c):
        region_cells = []
        q = deque([(r, c)])
        visited[r, c] = True
        while q:
            row, col = q.popleft()
            region_cells.append((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # Explore neighbors
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == 8 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    q.append((nr, nc))
        return region_cells

    # Identify all regions
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8 and not visited[r, c]:
                regions.append(find_region(r, c))

    region_bounding_boxes = []
    for region in regions:
        min_r = min(r for r, c in region)
        max_r = max(r for r, c in region)
        min_c = min(c for r, c in region)
        max_c = max(c for r, c in region)
        region_bounding_boxes.append(((min_r, min_c), (max_r, max_c), region)) # Store bounding box coordinates and region cells

    # Order regions
    def get_sort_key(bbox_data):
        (min_r, min_c), _, _ = bbox_data
        return (min_r, min_c)
    region_bounding_boxes.sort(key=get_sort_key)

    # Modify regions
    if len(region_bounding_boxes) >= 1:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[0]
        tr_r, tr_c = min_r, max_c # Top-right corner
        diag_r, diag_c = tr_r + 1, tr_c - 1
        if 0 <= diag_r < rows and 0 <= diag_c < cols and grid[diag_r, diag_c] == 0:
            grid[diag_r, diag_c] = 1 # Diagonally down and to the left

    if len(region_bounding_boxes) >= 2:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[1]
        bl_r, bl_c = max_r, min_c # Bottom-left corner
        diag_r, diag_c = bl_r - 1, bl_c + 1
        if 0 <= diag_r < rows and 0 <= diag_c < cols and grid[diag_r, diag_c] == 0:
            grid[diag_r, diag_c] = 1 # Diagonally up and to the right

    if len(region_bounding_boxes) >= 3:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[2]
        br_r, br_c = max_r, max_c # Bottom-right corner
        diag_r, diag_c = br_r - 1, br_c - 1
        if 0 <= diag_r < rows and 0 <= diag_c < cols and grid[diag_r, diag_c] == 0:
            grid[diag_r, diag_c] = 1 # Diagonally up and to the left


    return grid.tolist()


if __name__ == '__main__':

    output = transform(input_grid)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."
```
