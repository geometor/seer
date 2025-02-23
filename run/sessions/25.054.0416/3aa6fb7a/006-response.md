# 3aa6fb7a • 006 • refine_coder

---
```python
"""
1.  **Identify Azure Regions:** Find all distinct, contiguous regions of azure (8) pixels in the input grid. Consider each region as a separate object.
2.  **Region Traversal:** For each identified azure region, traverse its pixels sequentially from top-to-bottom and left-to-right.
3. **Change one pixel in each region:** In each region, find the *first* azure pixel that does not have any adjacent azure pixels *above* or to its *left*. Change the color of the identified pixel to blue (1). If no such pixel is found in the region, no changes are made to that region.
4.  **Unaffected Pixels:** All other pixels in the grid that are not part of the identified azure regions retain their original colors.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col, color):
    """
    Gets the coordinates of adjacent pixels with the specified color.
    """
    rows, cols = grid.shape
    adjacent = []

    # Check above
    if row > 0 and grid[row-1, col] == color:
        adjacent.append((row-1, col))
    # Check left
    if col > 0 and grid[row, col-1] == color:
        adjacent.append((row, col-1))

    return adjacent

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    # iterate through each cell to find azure regions
    for r in range(rows):
        for c in range(cols):
            if input_grid[r,c] == 8 and not visited[r,c]:
                # find all connected azure pixels (region)
                region = []
                queue = [(r,c)]
                visited[r,c] = True

                while queue:
                    row, col = queue.pop(0)
                    region.append((row,col))
                    adjacent_pixels = get_adjacent_pixels(input_grid, row, col, 8)

                    for adj_r, adj_c in adjacent_pixels:
                        if not visited[adj_r, adj_c]:
                            visited[adj_r,adj_c] = True
                            queue.append((adj_r, adj_c))

                # find the first azure that meets criteria (no neighbors above or left)
                for row, col in region:
                    adjacent_pixels = get_adjacent_pixels(input_grid, row, col, 8)
                    has_neighbor_above_or_left = False
                    for adj_r, adj_c in adjacent_pixels:
                        if adj_r < row or (adj_r == row and adj_c < col):
                            has_neighbor_above_or_left = True
                            break
                    if not has_neighbor_above_or_left:
                        output_grid[row,col] = 1
                        break  # Only change one pixel per region

    return output_grid
```
