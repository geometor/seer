# 868de0fa • 024 • refine_coder

---
```python
"""
1.  **Identify Blue Regions:** Find all contiguous regions of blue (1) pixels in the input grid. Each separate contiguous block of blue pixels is considered a distinct region.

2.  **Classify Regions:**
    *   Determine the bounding box for each blue region. The bounding box is the smallest rectangle that fully encloses the region.
    *   Sort the regions based on the bottom-most row of their bounding box. The region with the lowest y-coordinate (highest row index) for its bottom edge is the "bottom-most" region.

3.  **Bottom-Most Region Transformation:**
    *   Fill the interior of the *bottom-most* blue region with orange (7), leaving a one-pixel wide blue border around the filled area.

4.  **Other Regions Transformation:**
    *   For each blue region that is *not* the bottom-most:
        *   Calculate the geometric center of the region's bounding box.  This is done by averaging the row indices and averaging the column indices of the bounding box's top-left and bottom-right corners.
        *   Place a 2x2 square of red (2) pixels centered at the calculated center coordinates.
            *  The placement is adjusted if the center lies close to a region boundary. If the calculated center row is such that `center_row - 1` is less than the top boundary row of the bounding box, shift the placement down by one row.  If `center_row + 1` would exceed the bottom boundary, shift the placement up by one row. Do similarly for columns.
            *  If after the adjustment a part of the 2x2 square falls outside the region, then *do not place* the red square in that region.

5.  **Preserve Other Pixels:** Pixels that are not part of any identified blue region remain unchanged.
6. **Order of Operations:** Perform filling of the bottom-most blue region *before* placing red squares to avoid overwriting issues.
"""

import numpy as np

def find_regions(grid, color):
    """Finds contiguous regions of a specific color in a grid."""
    visited = np.zeros_like(grid, dtype=bool)
    regions = []

    def dfs(row, col, current_region):
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
        dfs(row + 1, col, current_region)
        dfs(row - 1, col, current_region)
        dfs(row, col + 1, current_region)
        dfs(row, col - 1, current_region)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color and not visited[i, j]:
                current_region = []
                dfs(i, j, current_region)
                regions.append(current_region)
    return regions

def get_bounding_box(region):
    """Calculates the bounding box of a region."""
    min_row = min(r for r, _ in region)
    max_row = max(r for r, _ in region)
    min_col = min(c for _, c in region)
    max_col = max(c for _, c in region)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # find blue regions
    blue_regions = find_regions(input_grid, 1)

    # find bottom blue region
    bottom_blue_region = None
    max_bottom_row = -1

    for region in blue_regions:
        min_row, max_row, min_col, max_col = get_bounding_box(region)
        if max_row > max_bottom_row:
            max_bottom_row = max_row
            bottom_blue_region = region

    # fill bottom with orange, excluding the border
    if bottom_blue_region:
        min_row, max_row, min_col, max_col = get_bounding_box(bottom_blue_region)
        for row in range(min_row + 1, max_row):
            for col in range(min_col + 1, max_col):
                output_grid[row, col] = 7

    # central transformation. 
    # Find and replace within other blue regions
    for region in blue_regions:
        if region != bottom_blue_region:
            min_row, max_row, min_col, max_col = get_bounding_box(region)

            # Calculate the center, with adjustments
            center_row = (min_row + max_row) // 2
            center_col = (min_col + max_col) // 2
            
            # Adjust center for 2x2 placement
            start_row = center_row
            end_row = center_row + 1
            start_col = center_col
            end_col = center_col + 1
            
            if start_row -1 < min_row:
                start_row += 1
                end_row += 1

            if end_row + 1 > max_row + 1:
              start_row -= 1
              end_row -= 1

            if start_col - 1 < min_col:
              start_col += 1
              end_col += 1
              
            if end_col + 1 > max_col + 1:
              start_col -= 1
              end_col -= 1

            # Check for valid placement and fill with red
            if (min_row <= start_row and end_row <= max_row and
               min_col <= start_col and end_col <= max_col):
                for r in range(start_row, end_row):
                    for c in range(start_col, end_col):
                        output_grid[r, c] = 2

    return output_grid
```

