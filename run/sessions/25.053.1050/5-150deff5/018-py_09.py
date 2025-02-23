"""
1.  **Identify** the contiguous shape formed by gray (5) pixels in the input grid.
2.  **Preserve** all pixels with the color white (0) in their original positions in the output grid.
3.  **Create** a new shape, colored red (2). This shape will be the leftmost vertical line of the original gray.
4.  **Create** a second shape, colored azure(8). This starts from the immediate right of the red shape and extends the same shape, but shifted.
5. **Place** these new color shapes in the output.
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

    # find leftmost and rightmost columns
    min_col = min(c for _, c in gray_object_coords)
    max_col = max(c for _, c in gray_object_coords)

    # build red object using the left part of gray object
    red_object_coords = []
    for r, c in gray_object_coords:
      if c == min_col:
        red_object_coords.append((r,c))
    
    for r, c in red_object_coords:
      output_grid[r,c] = 2


    #build azure object by extending right from red object
    azure_object_coords = []
    for r, c in gray_object_coords:
        if c > min_col:
          azure_object_coords.append((r,c))

    for r, c in azure_object_coords:
      output_grid[r,c] = 8

    return output_grid