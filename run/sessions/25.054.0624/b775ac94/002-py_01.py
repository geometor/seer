"""
1.  **Identify Objects:** Find all contiguous clusters of non-zero pixels in the input grid. Consider each cluster as a separate object.

2.  **Replicate and Modify:** For each identified object:
    *   Create a copy of object.
    *   Iterate each pixel in the copied object
    *   If the pixel exist in original, change it to match output.
    *   If a nearby pixel in same object has different color, randomly take
        some.

3.  **Preserve Background:**  All pixels with a value of 0 in the input grid remain 0 in the output grid.

4. **Output:** assemble changed objects into output image.
"""

import numpy as np
from collections import deque

def find_objects(grid):
    """Finds contiguous objects in the grid."""
    visited = set()
    objects = []

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        object_pixels = []
        color = grid[start_r, start_c]

        while queue:
            r, c = queue.popleft()
            object_pixels.append((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and grid[nr, nc] != 0 and (nr, nc) not in visited:
                    if grid[nr,nc] == color or grid[start_r, start_c] == 0:
                       queue.append((nr, nc))
                       visited.add((nr, nc))
        return object_pixels

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0 and (r, c) not in visited:
                objects.append(bfs(r, c))

    return objects
def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # find objects
    objects = find_objects(input_grid)
    
    # apply the transformation on the input_grid
    modified_input_grid = input_grid.copy()
    for obj in objects:
       for r,c in obj:
          modified_input_grid[r,c] = input_grid[r,c]


    # apply identified object changes to output
    for obj in objects:
        for r,c in obj:
            output_grid[r,c] = modified_input_grid[r,c]

    return output_grid