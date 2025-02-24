# 234bbc79 • 014 • example_3 • investigate_coder

---
```python
"""
1.  **Identify target color groups:** Find the groups in the input grid of color 5, and color 6.
2.  **Replace color groups:**
    *   Replace all color 5's with color 0.
    *   Replace all color 6's with color 8.

3.  **Locate shifted groups:** Identify the color groups that consist of colors 8.

4.  **Shift to row 3**: Move the first identified color group to the location of the second identified color group.

5.  **Shift to row 2**: Move the second identifed color group down to replace color 5 in row 3.

6.  **Shift color 2 group**: if there is a horizontal group of color 2 in row 2, shift the group of color 2 to the vertical position of the first color 8 group.
"""

import numpy as np

def find_color_groups(grid, color):
    groups = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_group):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_group.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, current_group)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_group = []
                dfs(r, c, current_group)
                groups.append(current_group)
    return groups

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    
    # Replace colors
    output_grid[output_grid == 5] = 0
    output_grid[output_grid == 6] = 8

    # Find color 8 groups
    color_8_groups = find_color_groups(output_grid, 8)
    
    # Find color 2 group in the second row
    color_2_groups = find_color_groups(output_grid, 2)
    
    #Shift the identified color 8 and color 2 groups
    if len(color_8_groups)>=2 and len(color_2_groups) >= 1:
        #shift color 8 group in row 2 to row 3
        group1 = color_8_groups[0]
        for r, c in group1:
            output_grid[r,c] = 0
        for r, c in group1:
            output_grid[2, c] = 8
        
        #shift color 8 group in row 3 to row 2, where original group1 cells were
        group2 = color_8_groups[1]
        for r, c in group2:
            output_grid[r,c] = 0
        for r,c in group1:
            output_grid[1, c + (group2[0][1]-group1[0][1])] = 8
        
        #shift color 2 group in row 2 to row 1
        group3 = color_2_groups[0]
        for r, c in group3:
            output_grid[r,c] = 0
        for r,c in group3:
            output_grid[r - 1, c] = 2

    return output_grid
```
