# 25.044.1412 • 1-3aa6fb7a • 002 Response

---

*text:*

```python
"""
1. Identify Connected Regions: Detect the two distinct, connected regions formed by cells with value '8' in the input grid.
2. Determine Bounding Boxes: For each of these regions, calculate the smallest bounding box that encloses all cells of the region. This box is defined by its top row, bottom row, left column, and right column.
3. Order Regions: Compare the bounding boxes of the two regions. The region whose bounding box has a smaller top row index, or in case of a tie, a smaller left column index, is considered the "first" region. The other is the "second" region.
4. Modify First Region: For the "first" region, locate the cell at the intersection of the top row of its bounding box and the right column of its bounding box. Change the value of this cell to '1'.
5. Modify Second Region: For the "second" region, locate the cell at the intersection of the bottom row of its bounding box and the left column of its bounding box. Change the value of this cell to '1'.
6. Preserve Unchanged Cells: All cells in the grid that are not modified in steps 4 and 5 retain their original values from the input grid.
"""

import numpy as np
from collections import deque

input_grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

expected_output = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
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
        grid[min_r, max_c] = 1 # Top-right of first region

    if len(region_bounding_boxes) >= 2:
        (min_r, min_c), (max_r, max_c), _ = region_bounding_boxes[1]
        grid[max_r, min_c] = 1 # Bottom-left of second region

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
