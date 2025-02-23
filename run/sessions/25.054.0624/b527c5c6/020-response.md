# b527c5c6 • 020 • example_4 • investigate_coder

---
```python
"""
1. Preserve: Keep the green region in the top-left corner of the input grid unchanged in the output grid.
2. Preserve: Keep the single red pixel within the top left green region.
3. Copy and Extend: Copy the red pixel in the upper green area and extend it downwards, creating a vertical red bar, copying green L shape from input. This fills parts of the originally white area.
4. Replicate green region 2 from the input into the output.
"""

import numpy as np

def find_object(grid, color):
    """Finds the coordinates of a contiguous object of the specified color."""
    coords = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return []
        visited.add((r, c))
        region_coords = [(r, c)]
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            region_coords.extend(dfs(r + dr, c + dc))
        return region_coords

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                coords.extend(dfs(r,c))
                return coords # return after first object
    return coords

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.copy(input_grid)
    
    # Find the single red pixel in the green region
    top_left_green_coords = find_object(input_grid, 3)
    red_pixel_coords = []
    for r,c in top_left_green_coords:
        if input_grid[r,c] == 2:
            red_pixel_coords.append((r,c))

    red_pixel = red_pixel_coords[0] if len(red_pixel_coords) > 0 else None

    #Find green L
    inverse_l_green = find_object(input_grid, 3)

    # Replicate inverse L
    if inverse_l_green:
      for r,c in inverse_l_green:
        if input_grid[r,c] == 3:
          output_grid[r,c] = 3

    # Extend red pixel downwards
    if red_pixel:
        red_row, red_col = red_pixel
        for row in range(red_row, input_grid.shape[0]):
            output_grid[row, red_col] = 2

    return output_grid
```
