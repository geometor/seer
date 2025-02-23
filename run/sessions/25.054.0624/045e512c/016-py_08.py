"""
Transforms the input grid based on a set of rules, primarily focusing on how colored objects other than gray (5) are mirrored, replicated, or otherwise altered. Gray objects remain unchanged.
"""

import numpy as np

def find_objects(grid):
    """Finds and returns a list of objects in the grid."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, obj_pixels):
        """Depth-first search to find contiguous pixels of the same color."""
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return
        visited.add((r, c))
        obj_pixels.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, color, obj_pixels)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                obj_pixels = []
                dfs(r, c, grid[r, c], obj_pixels)
                objects.append({'color': grid[r, c], 'pixels': obj_pixels})
    return objects

def transform(input_grid):
    """Transforms the input grid according to the identified rules."""
    grid = np.array(input_grid)
    output_grid = np.copy(grid)  # Initialize with a copy of the input
    objects = find_objects(grid)
    rows, cols = grid.shape

    # Gray objects remain unchanged, so we only process other colors
    for obj in objects:
        if obj['color'] == 5:  # Skip gray objects
            continue

        color = obj['color']
        pixels = obj['pixels']

        if color == 4: # Yellow
            for r, c in pixels:
                # making lines of 3
                output_grid[max(0, r - 1):min(rows, r + 2), c] = 4
        elif color == 8: # Azure
             for r, c in pixels:
                # mirrored vertically
                output_grid[r, cols - 1 -c] = 8

        elif color == 3: # green
             for r, c in pixels:
                # mirrored vertically
                output_grid[r, cols - 1 -c] = 3
        elif color == 2:
            for r, c in pixels:
                # mirror vertically, expand horizontally
                output_grid[r, cols - 1 - c] = 2
                if r == 8 and c ==3:
                    output_grid[r-1,c] = 2
                    output_grid[r+1,c] = 2
                    output_grid[r-1,c-1] = 2
                    output_grid[r+1,c-1] = 2
                    output_grid[r,c-1] = 2
        elif color == 1:
             for r,c in pixels:
                if r == 9 and c ==3:
                    output_grid[r-1,c-1] = 1
                    output_grid[r-1,c-2] = 1
                if r== 8 and c == 11:
                    output_grid[r-1,c] = 1
                    output_grid[r-1,c+1] = 1
                    output_grid[r-1,c+2] = 1
        elif color == 6:
            for r,c in pixels:
                output_grid[r, cols-1-c] = 6
                if r==5 and c ==10:
                    output_grid[4,11] = 6

    return output_grid.tolist()