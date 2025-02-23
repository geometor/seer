# 9565186b • 011 • refine_coder

---
```python
"""
1.  **Identify a Region of Interest (ROI):** In each input grid, find the largest contiguous region of non-white and non-background (2) color(s) forming either a 2x2 square, or largest area, or a column.
2. **Identify the Target Color:** The target color within the output grid is consistently '5' (gray).
3.  **Transformation Rule:** Within the ROI, change all pixels to color '5'. Other pixels remain unchanged.
"""

import numpy as np
from collections import Counter

def find_roi(grid):
    """Finds the region of interest (ROI) in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    max_region = []
    max_region_size = 0

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_region):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] == 0 or grid[r,c] == 2:
            return
        visited[r, c] = True
        current_region.append((r, c))

        dfs(r + 1, c, current_region)
        dfs(r - 1, c, current_region)
        dfs(r, c + 1, current_region)
        dfs(r, c - 1, current_region)

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0 and grid[r, c] != 2:
                current_region = []
                dfs(r, c, current_region)
                if len(current_region) > max_region_size:
                    max_region_size = len(current_region)
                    max_region = current_region
    return max_region
    

def transform(input_grid):
    """Transforms the input grid according to the identified rule."""
    
    # Convert to numpy array for easier manipulation
    grid = np.array(input_grid)
    output_grid = np.copy(grid)  # Initialize output as a copy

    # Find the Region of Interest
    roi = find_roi(grid)

    # Apply transformation: change ROI pixels to 5
    for r, c in roi:
        output_grid[r, c] = 5

    return output_grid.tolist()  # Convert back to list
```
