"""
1.  **Identify Green Regions:** Find all separate green inverse L-shaped regions in the input grid.
2.  **Identify Red Pixels:** Find the red pixel within each green region.
3.  **Extend Red Pixel in first green region:** Extend the red pixel from the top-left green region downwards to create a vertical red bar that fills the height of the combined green regions.
4. **Replicate Top Left Green Inverse L.** Replicate the top left green inverse L shape, connect with the red vertical bar.
5.  **Replicate Bottom Right Green Region:** Copy the bottom-right green region to the output, maintaining its relative position.
6. Connect the green inverse L and bottom right green region into a single green object, connected to the red vertical bar.
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

def transform(input_grid):
    """Transforms the input grid according to the specified rules."""

    output_grid = np.zeros_like(input_grid)
    
    # 1. Identify Green Regions
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

    # 2. Identify Red Pixels within green regions.
    red_pixels = []
    for region in green_regions:
        for r, c in region:
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))

    # 3. Extend Red Pixel in the first green region
    if top_left_green_region:
        red_pixel_in_top_left = None
        for r, c in top_left_green_region:
            if input_grid[r, c] == 2:
                red_pixel_in_top_left = (r,c)
                break
        
        if red_pixel_in_top_left:
          red_row, red_col = red_pixel_in_top_left

          # find bottom of combined object
          combined_height = input_grid.shape[0]

          # extend
          for row in range(red_row, combined_height):
            output_grid[row, red_col] = 2
    
    # 4. Replicate top left and connect to vertical red bar
    if top_left_green_region:
      for r,c in top_left_green_region:
        output_grid[r,c] = 3

    # 5 & 6. Replicate other green regions, connect them and to the red bar.
    for other_region in other_green_regions:
      for r, c in other_region:
          output_grid[r,c] = 3

    return output_grid