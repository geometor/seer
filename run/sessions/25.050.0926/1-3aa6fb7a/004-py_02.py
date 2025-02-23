"""
Identifies azure (color 8) components in the input grid. Based on shape of azure component:
- 1x2 (horizontal): places a blue pixel (color 1) below and to the left of the top-left corner.
- 2x1 (vertical): places a blue pixel (color 1) on the same row, one column to the right.
- Irregular shape: Look for a pixel which as south and east neighbors. Place a blue pixel (color 1) one row above, and one column to the left.
All other pixels remain unchanged (color 0).
"""

import numpy as np

def find_objects(grid, color):
    """
    Finds objects of a specified color in the grid.
    Returns a list of positions where the color is found.
    """
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                objects.append((r, c))
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    processed = set()

    for r, c in azure_objects:
        if (r,c) in processed:
          continue

        # Check for 1x2 horizontal
        if (r, c + 1) in azure_objects:
            output_grid[r + 1, c] = 1
            processed.add((r,c))
            processed.add((r, c+1))
            continue
        # Check for 2x1 vertical
        if (r + 1, c) in azure_objects:
            output_grid[r, c + 1] = 1
            processed.add((r,c))
            processed.add((r+1, c))
            continue

        #check for irregular with south and east neighbors
        rows, cols = input_grid.shape

        if (r+1 < rows) and (c+1 < cols) and ((r+1,c) in azure_objects) and ((r, c+1) in azure_objects):
           output_grid[r,c-1] = 1
           processed.add((r,c))


    return output_grid