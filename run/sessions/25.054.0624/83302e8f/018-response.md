# 83302e8f • 018 • refine_coder

---
```python
"""
The transformation rule is as follows:
1.  Identify the Bounding Object Color: Determine the color of the object that forms the boundary. This is any color other than white (0).
2.  Identify White Regions: Find all contiguous regions of white (0) pixels. Pixels are considered connected horizontally, vertically, and diagonally.
3. Find Bounding Box: Find the minimum bounding rectangle of all bounding objects.
4.  Conditional Color Change:
    *   For white regions completely within the bounding box and in the upper-left, change their color to yellow (4).  "Upper-left" is defined relative to the bounding box of bounding object.
    *   For white regions *not* meeting both above criteria (either not fully inside or not upper-left), change their color to green (3).

"""

import numpy as np

def find_contiguous_regions(grid, color):
    """Finds contiguous regions of a given color in the grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, current_region):
        """Depth-first search to explore a region."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return

        visited[row, col] = True
        current_region.append((row, col))

        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc, current_region)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_region = []
                dfs(row, col, current_region)
                regions.append(current_region)

    return regions

def is_within_bounds(region, min_row, min_col, max_row, max_col):
   """Checks if a region is entirely within the bounding box."""
   for row, col in region:
      if row < min_row or row > max_row or col < min_col or col > max_col:
         return False  # Region is outside bounds
   return True

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)
    
    # 1. Identify the Bounding Object Color
    unique_colors = np.unique(input_grid)
    bounding_color = unique_colors[unique_colors != 0][0]

    # 2. Find white (0) regions
    white_regions = find_contiguous_regions(input_grid, 0)

    # 3. Find Bounding Box
    bounding_pixels = np.argwhere(input_grid == bounding_color)
    min_bp_row, min_bp_col = np.min(bounding_pixels, axis=0)
    max_bp_row, max_bp_col = np.max(bounding_pixels, axis=0)
    
    #find region with the lowest combined row and col values from bounding boxes
    
    region_bounding_boxes = []
    for region in white_regions:
       coords = np.array(region)
       min_row, min_col = np.min(coords, axis=0)
       max_row, max_col = np.max(coords, axis=0)
       region_bounding_boxes.append( (min_row, min_col, max_row, max_col ) )

    # 4. Conditional Color Change

    if len(white_regions) >= 2:
       
        upper_left_indices = []
        other_indices = []
        for i, region_bb in enumerate(region_bounding_boxes):
           #check the region is within the bounding object box
           if region_bb[0] >= min_bp_row and region_bb[1] >= min_bp_col:
              if region_bb[2] <= max_bp_row and region_bb[3] <= max_bp_col:
                 upper_left_indices.append(i)
              else:
                 other_indices.append(i)
           else:
              other_indices.append(i)

        for i in upper_left_indices:
            for row, col in white_regions[i]:
               output_grid[row,col] = 4
        
        for i in other_indices:
            for row, col in white_regions[i]:
               output_grid[row,col] = 3
    elif len(white_regions) == 1:
        #only one region, so we need to determine if inside or outside box
        if is_within_bounds(white_regions[0], min_bp_row, min_bp_col, max_bp_row, max_bp_col ):
           for row, col in white_regions[0]:
              output_grid[row,col] = 4
        else:
           for row, col in white_regions[0]:
              output_grid[row,col] = 3

    return output_grid
```
