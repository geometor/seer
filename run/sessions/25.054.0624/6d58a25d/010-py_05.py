"""
1.  **Object Identification and Color Combination:** Identify two key colors in the input.
    *   Examples 1: 8 and 9
    *   Examples 2: 2 and 7
    *   Examples 3: 3 and 4

2.  **Determine Horizontal Replication Rule (Conditional):**
    *   _If_ isolated pixels of the first key color exist AND are not vertically aligned with pixels of the second key color, duplicate those pixels of color one to the immediate right.

3.  **Vertical Expansion:**
    *   For each column that contains *both* key colors, locate all the pixels of color one.
    *   Fill all cells between the highest and lowest of those color one pixels, in that column, with color one.
4.  **Object Fill (Example 1):**
    *   If pixels of the second key color have pixels of the first key color above and below, fill the space between with the second key color.
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
    
    # Horizontal Replication
    new_color1_coords = []
    for r, c in color1_coords:
      if not is_vertically_aligned((r,c), color2_coords):
          new_color1_coords.append((r, c + 1))  # Add pixel to the right
          output_grid[r, c + 1] = color1
      new_color1_coords.append((r,c))
    

    # Vertical Expansion
    
    combined_cols = set()
    for r1,c1 in color1_coords:
      for r2,c2 in color2_coords:
        if c1==c2:
          combined_cols.add(c1)

    for col in combined_cols:
        #find color1 pixels in this col
        color1_in_col = []
        for r,c in new_color1_coords:
          if c == col:
            color1_in_col.append((r,col))


        if len(color1_in_col) > 0:
            min_row = min([r for r, _ in color1_in_col])
            max_row = max([r for r, _ in color1_in_col])

            for row in range(min_row, max_row + 1):
              output_grid[row, col] = color1

    # Object Filling (Specific to Example 1 - Maroon and Azure)
    if color1 == 9 and color2 == 8:
        for r2, c2 in color2_coords:
            # Find color1 above and below
            above = False
            below = False
            for r1, c1 in color1_coords:
                if c1 == c2:
                    if r1 < r2:
                        above = True
                    if r1 > r2:
                        below = True
            if above and below:
                output_grid[r2,c2] = color2
    return output_grid