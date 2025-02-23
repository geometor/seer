"""
1.  **Identify Stripes:** Locate all horizontal and vertical stripes of red (2) and yellow (4) pixels. A stripe is defined as a contiguous sequence of pixels of the same color along a row or column.
2.  **Find Intersections:** Determine the points (pixels) where the red stripes intersect the yellow stripe. An intersection occurs where a red pixel in a red stripe is in the same row or column as a section of the horizontal yellow stripe.
3.  **Color Replacement:** At each intersection point identified in step 2, change the color of the pixel from red (2) to yellow (4).
4. **Preserve other:** All other pixels should not be changed.
"""

import numpy as np

def find_stripes(grid, color, orientation):
    stripes = []
    if orientation == "horizontal":
        for i, row in enumerate(grid):
            stripe_start = None
            for j, pixel in enumerate(row):
                if pixel == color:
                    if stripe_start is None:
                        stripe_start = j
                elif stripe_start is not None:
                    stripes.append((i, stripe_start, i, j - 1))
                    stripe_start = None
            if stripe_start is not None:
                stripes.append((i, stripe_start, i, len(row) - 1))
    elif orientation == "vertical":
        for j in range(grid.shape[1]):
            stripe_start = None
            for i, pixel in enumerate(grid[:, j]):
                if pixel == color:
                    if stripe_start is None:
                        stripe_start = i
                elif stripe_start is not None:
                    stripes.append((stripe_start, j, i - 1, j))
                    stripe_start = None
            if stripe_start is not None:
                stripes.append((stripe_start, j, grid.shape[0] - 1, j))
    return stripes

def find_intersections(red_stripes, yellow_stripes):
    intersections = []
    for r_start_row, r_start_col, r_end_row, r_end_col in red_stripes:
      for y_start_row, y_start_col, y_end_row, y_end_col in yellow_stripes:
        if r_start_row == r_end_row: # red horizontal
          if y_start_row == y_end_row: # yellow horizontal
            continue # both horizontal
          else: # yellow vertical
            if y_start_col >= r_start_col and y_start_col <= r_end_col and r_start_row >= y_start_row and r_start_row <= y_end_row:
              intersections.append( (r_start_row, y_start_col))
        else: # red vertical
          if y_start_row == y_end_row: # yellow horizontal
            if r_start_row <= y_start_row and r_end_row >= y_start_row and y_start_col <= r_start_col and y_end_col >= r_start_col:
              intersections.append( (y_start_row, r_start_col))

          else: # yellow vertical
            continue; # both vertical

    return intersections

def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)
    output_grid = np.copy(grid)

    # Find red and yellow stripes
    red_horizontal_stripes = find_stripes(grid, 2, "horizontal")
    red_vertical_stripes = find_stripes(grid, 2, "vertical")
    yellow_horizontal_stripes = find_stripes(grid, 4, "horizontal")
    yellow_vertical_stripes = find_stripes(grid, 4, "vertical")  #find vertical yellow as well

    red_stripes = red_horizontal_stripes + red_vertical_stripes
    yellow_stripes = yellow_horizontal_stripes + yellow_vertical_stripes

    # Find intersection points
    intersections = find_intersections(red_stripes, yellow_stripes)

    # change output pixels 
    for row, col in intersections:
        output_grid[row, col] = 4

    return output_grid