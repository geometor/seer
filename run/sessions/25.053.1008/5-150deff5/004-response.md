# 5-150deff5 • 004 • example_2 - CODE

---
```python
"""
1.  **Identify the background:** The background is the grid itself, and all pixels with a value of 0 (white) remain unchanged.
2.  **Identify the shape:** Find the contiguous block of pixels with a value of 5 (gray). This is the primary shape.
3. **Segment Identification**: Find the segments of the contiguous block, defining segments as only single pixel width horizontal or vertical lines of pixels
4.  **Horizontal Segment Replacement:** Replace each horizontal line segment of the gray shape with pixels of value 8 (azure).
5.  **Vertical Segment Replacement:** Replace each vertical line segment of the gray shape with pixels of value 2 (red).
6.  **Output:** The output grid consists of the unchanged background, and the transformed shape with azure and red segments.
"""

import numpy as np

def find_contiguous_block(grid, color):
    # Find the contiguous block of pixels with a specific color.
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    block = []

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        block.append((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                dfs(r, c)
                return block  # Return after finding the first block
    return block

def is_horizontal(grid, r, c):
    # Check if the pixel at (r, c) is part of a horizontal segment.
    if grid[r][c] == 0:
        return False

    rows, cols = grid.shape
    #check left and right - if at least one neighbor matches, return true
    if (c > 0 and grid[r, c - 1] == grid[r,c]) or (c < cols - 1 and grid[r, c + 1] == grid[r,c]):
        return True
    return False
    

def is_vertical(grid, r, c):
    # Check if the pixel at (r, c) is part of a vertical segment.
    if grid[r][c] == 0:
        return False
    
    rows, cols = grid.shape
    #check above and below - if at least one neighbor matches return true
    if (r > 0 and grid[r - 1, c] == grid[r,c]) or (r < rows - 1 and grid[r + 1, c] == grid[r,c]):
          return True

    return False
    

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find the gray shape
    gray_shape = find_contiguous_block(input_grid, 5)

    #change output pixels
    for r, c in gray_shape:
      if is_horizontal(input_grid, r, c):
        output_grid[r,c] = 8
      elif is_vertical(input_grid, r, c):
        output_grid[r,c] = 2


    return output_grid
```
