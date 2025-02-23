# b527c5c6 • 024 • refine_coder

---
```python
"""
1.  **Identify Green Inverse L Shapes:** Find all separate green inverse L-shaped regions in the input grid.
2.  **Locate Red Pixels:** Identify all red pixels within the green inverse L shapes.
3.  **Determine Red Bar Height:** Determine the combined height of the inverse L shapes.
4.  **Create Red Vertical Bar:** Create a red vertical bar. The height is determined by the height of the combined green shapes. The bar's x-coordinate is determined by the red pixel in the top-left most inverse L shape.
5.  **Connect Green Inverse L shapes.** Combine all green regions. The shapes connect to the red vertical bar.
"""

import numpy as np

def find_all_objects(grid, color):
    """Finds the coordinates of all disjoint objects of the specified color."""
    objects = []
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
                objects.append(dfs(r, c))
    return objects

def get_top_left_coord(coords):
  """Returns the top-left coordinate from a list of coordinates."""
  if not coords:
      return None
  min_row = min(r for r, c in coords)
  min_col = min(c for r, c in coords if r == min_row) # find min col for min row
  return (min_row, min_col)

def get_combined_height(regions):
  """Calculates the combined height of regions"""
  if not regions:
    return 0
  
  min_row = min(r for region in regions for r, _ in region)
  max_row = max(r for region in regions for r, _ in region)
  return max_row - min_row + 1

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Green Inverse L Shapes
    green_regions = find_all_objects(input_grid, 3)

    # Find top-left green region and other green regions
    top_left_green_region = None
    other_green_regions = []

    if (len(green_regions) > 0):
      top_left_green_region = green_regions[0]
      top_left_most_coord = get_top_left_coord(top_left_green_region)

      for region in green_regions:
          curr_top_left = get_top_left_coord(region)
          if curr_top_left[0] < top_left_most_coord[0] or (curr_top_left[0] == top_left_most_coord[0] and curr_top_left[1] < top_left_most_coord[1]):
              top_left_most_coord = curr_top_left
              other_green_regions.append(top_left_green_region)
              top_left_green_region = region
          else:
              other_green_regions.append(region)
    
    # 2. Identify Red Pixels.
    red_pixels = []
    for region in green_regions:
      for r, c in region:
        if input_grid[r,c] == 2:
          red_pixels.append((r,c))

    # 3. Determine Red Bar Height
    combined_height = get_combined_height(green_regions)


    # 4. Create Red Vertical Bar
    if top_left_green_region and red_pixels:
      red_pixel_in_top_left = None
      for r, c in top_left_green_region:
          if input_grid[r, c] == 2:
            red_pixel_in_top_left = (r,c)
            break
      if red_pixel_in_top_left:
        red_row, red_col = red_pixel_in_top_left
        min_row = min(r for region in green_regions for r, _ in region) # find top

        for row in range(min_row, min_row + combined_height):
          output_grid[row, red_col] = 2

    # 5. Connect Green Inverse L shapes.
    for region in green_regions:
        for r, c in region:
            output_grid[r, c] = 3

    return output_grid
```
