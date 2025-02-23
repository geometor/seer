# aedd82e4 • 006 • refine_coder

---
```python
"""
Identifies groups of contiguous red pixels and changes the color of single pixels, the bottom-rightmost pixel in groups of two or three, or two pixels (bottom-most and right-most) in diagonal groups to blue.
"""

import numpy as np

def find_red_groups(grid):
    """Finds groups of contiguous red pixels."""
    red_groups = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_group):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != 2:
            return
        visited[r, c] = True
        current_group.append((r, c))
        # Explore adjacent cells (up, down, left, right)
        dfs(r + 1, c, current_group)
        dfs(r - 1, c, current_group)
        dfs(r, c + 1, current_group)
        dfs(r, c - 1, current_group)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 2 and not visited[r, c]:
                current_group = []
                dfs(r, c, current_group)
                red_groups.append(current_group)
    return red_groups

def is_diagonal(group):
    """Checks if a group of pixels forms a diagonal line."""
    if len(group) < 2:
        return False
    
    group.sort() #sort by row then column
    for i in range(len(group) - 1):
        dr = abs(group[i+1][0] - group[i][0])
        dc = abs(group[i+1][1] - group[i][1])
        if dr != 1 or dc != 1:
           return False
    return True
    

def select_target_pixel(group):
    """Selects the target pixel(s) within a red group."""
    if len(group) == 0:
       return []
    
    if len(group) == 1:
       return [group[0]]

    group.sort(key=lambda x: (x[0], x[1]))  # Sort by row, then column

    targets = []
    
    if is_diagonal(group):
        # Find bottom-most
        bottom_most = group[0]
        for pixel in group:
            if pixel[0] > bottom_most[0]:
                bottom_most = pixel

        #Find right-most
        right_most = group[0]
        for pixel in group:
            if pixel[1] > right_most[1]:
                right_most = pixel
        targets.append(bottom_most)
        targets.append(right_most)

    else:
        targets.append(group[-1]) #right_most

    return targets
        

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find groups of contiguous red pixels.
    red_groups = find_red_groups(input_grid)

    # Select and change the target pixel(s) in each group.
    for group in red_groups:
        target_pixels = select_target_pixel(group)
        for target_pixel in target_pixels:
          if target_pixel:
            output_grid[target_pixel] = 1

    return output_grid
```
