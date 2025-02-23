"""
1.  **Identify Green Regions:** Locate all contiguous regions of green (3) pixels in the input grid.  "Contiguous" means connected horizontally or vertically.

2.  **Selective Color Change:** Within *some* of the identified green regions, change the color of a subset of the green pixels to yellow (4). The rule for selecting *which* green pixels to change is not entirely clear from this single example, but it's not *all* green pixels. It appears that green regions maintain their general shape when adjacent to white regions.

3.  **Preserve Other Pixels:** All pixels that are not green in the input grid remain unchanged in the output grid.

4. **Output:** The resulting grid, with the selected green pixels changed to yellow, is the output.
"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def is_valid(x, y):
        """Checks if a coordinate is within the grid bounds."""
        return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

    def dfs(x, y, current_region):
        """Performs Depth-First Search to find contiguous pixels."""
        if not is_valid(x, y) or visited[x, y] or grid[x, y] != color:
            return

        visited[x, y] = True
        current_region.append((x, y))

        # Explore adjacent pixels (up, down, left, right)
        dfs(x + 1, y, current_region)
        dfs(x - 1, y, current_region)
        dfs(x, y + 1, current_region)
        dfs(x, y - 1, current_region)

    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == color and not visited[x, y]:
                current_region = []
                dfs(x, y, current_region)
                regions.append(current_region)
    return regions

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    # change output pixels

    green_regions = find_contiguous_regions(input_grid, 3)

    for region in green_regions:
      # currently changes interior to yellow, preserving one layer of green
      for x,y in region:
        neighbors = 0
        if input_grid[x+1, y] == 3 if x+1 < input_grid.shape[0] else False:
            neighbors += 1
        if input_grid[x-1, y] == 3 if x-1 >= 0 else False:
            neighbors += 1
        if input_grid[x, y+1] == 3 if y+1 < input_grid.shape[1] else False:
          neighbors += 1
        if input_grid[x, y-1] == 3 if y-1 >= 0 else False:
          neighbors += 1
        if neighbors == 4:
          output_grid[x,y] = 4

    return output_grid