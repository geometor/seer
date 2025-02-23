"""
Transforms the input grid by replicating and translating magenta (6) and blue (1) objects based on their initial positions, while leaving gray (5) objects unchanged.
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
    """Transforms the input grid according to the specified rules."""
    grid = np.array(input_grid)  # Convert to NumPy array for easier manipulation
    output_grid = np.copy(grid)  # Initialize output grid
    objects = find_objects(grid)  # Find all objects in the grid
    rows, cols = grid.shape
    center_col = cols // 2

    for obj in objects:
        color = obj['color']
        pixels = obj['pixels']

        if color == 6:  # Magenta (6)
            for r, c in pixels:
                # Replication and translation logic for magenta
                
                #Top row rules
                if r == 0 and c == center_col - 6:
                    output_grid[r,c] = 6

                if r == 0 and c == center_col + 6:
                    output_grid[r,c] = 6

                if r == 0 and c == center_col - 5:
                    output_grid[r,c] = 6
                    output_grid[r,c+1] = 6

                if r == 0 and c == center_col + 5:
                    output_grid[r,c-1] = 6
                    output_grid[r,c] = 6
                
                # Quadrant rules
                if r < rows//2 and c > cols//2: #first quadrant
                    output_grid[r+1,c+1] = 6
                elif r < rows//2 and c < cols//2: # second quadrant
                    output_grid[r,c-1] = 6
                elif r > rows //2 and c < cols//2:
                    pass
                elif r > rows//2 and c > cols//2: # forth quadrant
                    output_grid[r+1,c] = 6
        elif color == 1:  # Blue (1)
             for r, c in pixels:
                # Replication and translation logic for blue
                if r == rows - 1 and c > 0:
                    output_grid[r,c-1] = 1
                if r == rows - 2:
                    output_grid[r,c] = 1
                if r == rows-5:
                    output_grid[r-1,c] = 1
                    output_grid[r-2,c] = 1
                if r == rows - 6:
                    output_grid[r+1,c+1] = 1

    return output_grid.tolist()  # Convert back to list