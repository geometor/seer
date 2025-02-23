"""
1.  **Identify** the contiguous shape formed by gray (5) pixels in the input grid. This is the `gray_object`.
2.  **Preserve** all pixels that are white (0) in the input grid, keeping their positions unchanged in the output grid.
3.  **Extract** the leftmost vertical line segment of the `gray_object`. Create
    a new object with the color red (2) that has the height of the extracted segment. This is the `red_object`.
4. **Extract** the remaining columns of the gray object, and convert them into the azure (8) color. This is the `azure_object`.
5.  **Place** the `red_object` in the output grid in place of the leftmost column of the original gray object
6. **Place** the `azure_object` in the output grid, starting from the immediate
   right of the red object, and filling the columns of the original gray object.
"""

import numpy as np

def get_object(grid, color):
    """Finds the coordinates of a contiguous object of a specified color."""
    coords = []
    visited = set()
    rows, cols = grid.shape
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        coords.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                dfs(r, c)
                return coords # return first object found
    return []


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # get the gray object
    gray_object_coords = get_object(input_grid, 5)

    # if no gray object exists, return
    if not gray_object_coords:
      return output_grid

    # change the color of gray pixels to white
    for r, c in gray_object_coords:
        output_grid[r, c] = 0

    # find leftmost and rightmost columns, and min and max rows
    min_col = min(c for _, c in gray_object_coords)
    max_col = max(c for _, c in gray_object_coords)
    min_row = min(r for r, _ in gray_object_coords)
    max_row = max(r for r, _ in gray_object_coords)

    # build red object using the left part of gray object
    for r in range(min_row, max_row + 1):
        output_grid[r, min_col] = 2


    #build azure object by extending right from red object
    for r, c in gray_object_coords:
        if c > min_col:
          output_grid[r,c] = 8

    return output_grid