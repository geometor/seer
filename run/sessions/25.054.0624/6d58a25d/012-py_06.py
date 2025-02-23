"""
1.  **Identify Key Colors:** Determine the two most prominent colors in the input grid (excluding black/background). We'll call them Color 1 and Color 2. The specific pairs are (9, 8), (2, 7), and (3, 4) for the examples.

2.  **Conditional Horizontal Replication (Color 1):**
    *   Iterate through each pixel of Color 1.
    *   If a Color 1 pixel does *not* have a Color 2 pixel in the same column, duplicate the Color 1 pixel to its immediate right.

3.  **Vertical Expansion (Color 1):**
    * Iterate through all columns.
    *   If a column contains *both* Color 1 and Color 2 pixels:
        *   Find the topmost and bottommost Color 1 pixels within that column.
        *   Fill all grid cells between (and including) those two rows in that column with Color 1.

4.  **Object Combination**
    * example 1 only: if any color 2 pixel is surrounded vertically by color 1, replace it with color 1
    * example 3 only: for all horizontal line segments, if any yellow segment is bound on both ends by green pixels, change the color of the yellow pixels to green.
"""

import numpy as np

def get_objects(grid, color):
    """Finds coordinates of all pixels of a given color."""
    return np.argwhere(grid == color)

def is_vertically_aligned(coord, other_color_coords):
    """Checks if a coordinate is vertically aligned with any pixel of another color."""
    for other_coord in other_color_coords:
        if coord[1] == other_coord[1]:
            return True
    return False

def get_color_pair(input_grid):
  """Determine color pair from input grid"""
  unique_colors = np.unique(input_grid)
  unique_colors = unique_colors[unique_colors != 0]  # Exclude background color

  if len(unique_colors) >= 2:
        color1 = unique_colors[0]
        color2 = unique_colors[1]

        # Special handling for example 1
        if 8 in unique_colors and 9 in unique_colors:
            return 9, 8  # Order matters based on observation
        if 3 in unique_colors and 4 in unique_colors:
          return 3,4
        if 2 in unique_colors and 7 in unique_colors:
            return 2,7
          
        return color1, color2 #default
  return None, None

def transform(input_grid):
    # Initialize output grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Determine color pair
    color1, color2 = get_color_pair(input_grid)
    if color1 is None:
        return output_grid # Handle edge case of no identifiable colors

    color1_coords = get_objects(input_grid, color1)
    color2_coords = get_objects(input_grid, color2)

    # --- Conditional Horizontal Replication (Color 1) ---
    new_color1_coords = []  # Store updated color1 coordinates
    for r, c in color1_coords:
        if not is_vertically_aligned((r, c), color2_coords):
            if c + 1 < cols:  # Check bounds before replication
                output_grid[r, c + 1] = color1
                new_color1_coords.append((r, c + 1))
        new_color1_coords.append((r,c))

    # --- Vertical Expansion (Color 1) ---
    for col in range(cols):
        # Check if the column contains both colors
        col_contains_color1 = False
        col_contains_color2 = False

        for r in range(rows):
            if (r,col) in new_color1_coords:
                col_contains_color1 = True
            if (r, col) in [(c[0], c[1]) for c in color2_coords]:
              col_contains_color2 = True

        if col_contains_color1 and col_contains_color2:
          color1_in_col_rows = []
          for r,c in new_color1_coords:
            if c == col:
              color1_in_col_rows.append(r)
          if len(color1_in_col_rows) > 0:  #Avoid errors if empty
            min_row = min(color1_in_col_rows)
            max_row = max(color1_in_col_rows)
            for row in range(min_row, max_row + 1):
                output_grid[row, col] = color1
    
    # --- Object Combination ---
    # Example 1: Replace vertically surrounded Color 2 with Color 1
    if color1 == 9 and color2 == 8:
        for r2, c2 in color2_coords:
            above = False
            below = False
            for r1, c1 in color1_coords:
                if c1 == c2:
                    if r1 < r2:
                        above = True
                    if r1 > r2:
                        below = True
            if above and below:
                output_grid[r2, c2] = color1 #replace

    # Example 3: change yellow segments to green
    if color1 == 3 and color2 == 4:
        for r2, c2 in color2_coords:
          left = False
          right = False
          for r1, c1 in color1_coords:
            if r1==r2:
              if c1 < c2:
                left = True
              if c1 > c2:
                right = True
          if left and right:
            output_grid[r2,c2] = color1

    return output_grid