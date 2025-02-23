# 1-3aa6fb7a • 003 • example_2 - NLP

---

**input**
```
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_input.png)


**output**
```
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

![Image](000-example_1_output.png)

**Natural Language Program:**

The task is to modify the input grid by identifying connected regions of azure color (color 8) and adding a blue cell (color 1) adjacent to each region. The placement of the blue cell depends on the shape of the azure region, specifically whether it is "left-leaning" or "right-leaning".

Here's the step-by-step transformation rule:

1.  **Identify Azure Regions:** Find all connected components of cells with color 8 in the input grid.
2.  **Analyze Each Region:** For each identified azure region, perform the following steps:
    a. **Determine Bounding Box:** Find the smallest rectangle that encloses the azure region. This is defined by the minimum and maximum row and column indices of the cells in the region.
    b. **Calculate Centroid:** Calculate the average row and average column of all cells in the azure region. This represents the "center of mass" of the region.
    c. **Calculate Bounding Box Center:** Calculate the center point of the bounding box by averaging its minimum and maximum row and column indices.
    d. **Compare Centroid and Bounding Box Center (Column-wise):** Compare the column coordinate of the centroid with the column coordinate of the bounding box center.
        - **If the centroid's column is to the left of the bounding box center's column (smaller column index):** This indicates a "left-leaning" shape. Place a blue cell (color 1) at the top-right corner of the bounding box. That is, at the row corresponding to the minimum row of the bounding box and the column corresponding to the maximum column of the bounding box.
        - **If the centroid's column is to the right of the bounding box center's column (larger column index):** This indicates a "right-leaning" shape. Place a blue cell (color 1) at the bottom-left corner of the bounding box. That is, at the row corresponding to the maximum row of the bounding box and the column corresponding to the minimum column of the bounding box.
    e. **Preserve Azure Region:** Ensure that the azure region itself remains unchanged in the output grid.
3.  **Maintain Background:** All cells in the input grid that are not part of any azure region and are not modified by step 2.d, remain white (color 0) in the output grid.

This process is applied independently to each connected azure region in the input grid to produce the final output grid.
```python
"""
The task is to modify the input grid by identifying connected regions of azure color (color 8) and adding a blue cell (color 1) adjacent to each region. The placement of the blue cell depends on the shape of the azure region, specifically whether it is "left-leaning" or "right-leaning".

Here's the step-by-step transformation rule:

1.  **Identify Azure Regions:** Find all connected components of cells with color 8 in the input grid.
2.  **Analyze Each Region:** For each identified azure region, perform the following steps:
    a. **Determine Bounding Box:** Find the smallest rectangle that encloses the azure region. This is defined by the minimum and maximum row and column indices of the cells in the region.
    b. **Calculate Centroid:** Calculate the average row and average column of all cells in the azure region. This represents the "center of mass" of the region.
    c. **Calculate Bounding Box Center:** Calculate the center point of the bounding box by averaging its minimum and maximum row and column indices.
    d. **Compare Centroid and Bounding Box Center (Column-wise):** Compare the column coordinate of the centroid with the column coordinate of the bounding box center.
        - **If the centroid's column is to the left of the bounding box center's column (smaller column index):** This indicates a "left-leaning" shape. Place a blue cell (color 1) at the top-right corner of the bounding box. That is, at the row corresponding to the minimum row of the bounding box and the column corresponding to the maximum column of the bounding box.
        - **If the centroid's column is to the right of the bounding box center's column (larger column index):** This indicates a "right-leaning" shape. Place a blue cell (color 1) at the bottom-left corner of the bounding box. That is, at the row corresponding to the maximum row of the bounding box and the column corresponding to the minimum column of the bounding box.
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

def centroid(region):
    """Calculate the centroid of a region."""
    sum_r, sum_c = 0, 0
    for r, c in region:
        sum_r += r
        sum_c += c
    return sum_r / len(region), sum_c / len(region)

def bounding_box_center(bbox):
     """Calculate the center of the bounding box"""
     min_r, min_c, max_r, max_c = bbox
     return (min_r+max_r)/2, (min_c + max_c)/2
     

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for region in azure_objects:
        # Calculate bounding box
        bbox = bounding_box(region)
        # Calculate centroid
        cen_r, cen_c = centroid(region)
        # Calculate the center of the bounding box.
        bbox_center_r, bbox_center_c = bounding_box_center(bbox)

        # Compare centroid and bounding box center (column-wise)
        if cen_c < bbox_center_c:  # Left-leaning
            # Place blue cell at top-right corner of bounding box
            output_grid[bbox[0], bbox[3]] = 1
        elif cen_c > bbox_center_c:  # Right-leaning
            # Place blue cell at bottom-left corner of bounding box
            output_grid[bbox[2], bbox[1]] = 1

    return output_grid
```

**input**
```
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
```

![Image](002-example_2_input.png)


**output**
```
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
```

![Image](002-example_2_output.png)

**Instructions**

- Describe in natural language the step-by-step transformation observed between the input and output grids.
- Focus on identifying objects, their properties (predicates), and the actions performed on them.
- Be as clear and concise as possible, providing a complete description of the transformation rule.
