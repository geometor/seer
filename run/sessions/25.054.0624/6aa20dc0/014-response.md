# 6aa20dc0 • 014 • example_3 • investigate_coder

---
```python
"""
Replicates non-background color pixel clusters in a grid. The yellow (4) color, if existing in a cluster, serves as the origin.  The existing clusters are replicated one position down and one position to the right, relative to the original yellow pixel.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous clusters of non-background pixels."""
    visited = set()
    objects = []

    rows, cols = len(grid), len(grid[0])

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r][c] == 8:
            return
        visited.add((r, c))
        current_object.append((r, c, grid[r][c]))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and grid[r][c] != 8:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)

    return objects

def transform(input_grid):
    # Initialize output grid with the same dimensions and background color
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = len(input_grid), len(input_grid[0])

    # Find objects (clusters of non-background pixels)
    objects = find_objects(input_grid)
    
    # Iterate through each object
    for obj in objects:
        #find yellow pixel location
        yellow_location = None
        for r, c, color in obj:
            if color == 4:
               yellow_location = (r,c)
               break;
        
        #skip if no yellow in object
        if yellow_location is None:
            continue
            
        #compute relative position of pixels to yellow
        relative_positions = []
        for r, c, color in obj:
            relative_positions.append(((r-yellow_location[0], c-yellow_location[1]), color))

        #Replicate the clusters
        new_r = yellow_location[0]+1
        new_c = yellow_location[1]+1

        #check if new positioins out of bounds
        for (dr,dc), color in relative_positions:
            nr, nc = new_r+dr, new_c+dc
            if 0 <= nr < rows and 0 <= nc < cols:  
                output_grid[nr][nc] = color

    return output_grid.tolist()
```
