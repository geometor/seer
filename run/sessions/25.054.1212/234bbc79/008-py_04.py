"""
The transformation rule is as follows:
1. Identify Objects: Recognize contiguous blocks of pixels of the same color as distinct objects.
2. Color Replacement:
    *   Replace all instances of grey (5) with blue (1).
    *   Replace all instances of blue (1) with white (0).
3. Preserve other blocks: keep red(2) and green(3) unchanged.
"""

import numpy as np

def get_objects(grid):
    """
    Finds contiguous blocks of the same color in a grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, object_pixels):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        object_pixels.append((row, col))
        dfs(row + 1, col, color, object_pixels)
        dfs(row - 1, col, color, object_pixels)
        dfs(row, col + 1, color, object_pixels)
        dfs(row, col - 1, color, object_pixels)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                color = grid[row, col]
                object_pixels = []
                dfs(row, col, color, object_pixels)
                if object_pixels:
                    objects.append({'color': color, 'pixels': object_pixels})
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Get objects from input_grid - although direct color replacement seems to
    # work - get objects is still useful and consistent with the SEER
    # architecture, this is to future-proof for more complex tasks
    objects = get_objects(input_grid)

    # change output pixels 
    for obj in objects:
        if obj['color'] == 5:
          for row, col in obj['pixels']:
            output_grid[row,col] = 1
        elif obj['color'] == 1:
          for row, col in obj['pixels']:
            output_grid[row,col] = 0
            
    return output_grid