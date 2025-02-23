# 1-3aa6fb7a • 002 • example_1 - CODE

---
```python
"""
The transformation rule is to add blue pixels in between distinct groups of azure pixels.
"""

import numpy as np

def find_azure_groups(input_grid):
    """
    Finds and returns a list of distinct groups of azure pixels.
    """
    azure_groups = []
    visited = set()
    rows, cols = input_grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_group):
        if (r, c) in visited or not is_valid(r, c) or input_grid[r, c] != 8:
            return
        visited.add((r, c))
        current_group.append((r, c))

        # Check adjacent cells (up, down, left, right)
        dfs(r + 1, c, current_group)
        dfs(r - 1, c, current_group)
        dfs(r, c + 1, current_group)
        dfs(r, c - 1, current_group)

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 8 and (r, c) not in visited:
                current_group = []
                dfs(r, c, current_group)
                if current_group:
                    azure_groups.append(current_group)
    return azure_groups

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find distinct groups of azure pixels
    azure_groups = find_azure_groups(input_grid)
    
    # Create a set of all azure pixel coordinates for quick lookup
    azure_pixels = set()
    for group in azure_groups:
        for r, c in group:
            azure_pixels.add((r,c))


    # Iterate through all cells to check for placement conditions
    for r in range(rows):
        for c in range(cols):
            # Condition: current cell is white
            if input_grid[r,c] == 0:
                # check neighbors for azure pixels from different groups
                neighboring_groups = set()
                
                neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                
                for nr, nc in neighbors:
                    if (nr, nc) in azure_pixels:
                        #find which group this neighbor belongs
                        for i, group in enumerate(azure_groups):
                            if (nr, nc) in group:
                                neighboring_groups.add(i)
                                break
                
                if len(neighboring_groups) > 1:
                     output_grid[r,c] = 1

    return output_grid
```
