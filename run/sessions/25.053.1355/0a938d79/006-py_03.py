"""
1.  **Identify Key Colors:** Examine the input grid. Identify "key colors" as any non-zero color.
2.  **Detect Horizontal Pattern**: Look for repeating patterns of colors and blank spaces horizontally.
3. **Detect Vertical Pattern:** If there is a consisten horizontal pattern, look for repeating pattern of colors and blank rows in a vertical stacking.
4.  **Build Output:**
    *   If a horizontal pattern is found, fill the output grid rows by repeating the pattern starting at the column of the first colored pixel, until the end of the row.
    * If a vertical pattern is found, use the horizontal pattern from the first set of colored rows. Repeat the combination of colored and blank rows, starting from the first colored row index.
5.  **Default:** If no key colors are found, return an output grid of the same size, filled with 0.
"""

import numpy as np

def find_key_colors(grid):
    """Finds unique non-zero colors in the grid."""
    return np.unique(grid[grid != 0])

def detect_horizontal_pattern(row):
    """Detects a repeating horizontal pattern in a row."""
    non_zero_indices = np.where(row != 0)[0]
    if len(non_zero_indices) == 0:
        return None

    first_color_index = non_zero_indices[0]
    pattern = []
    for i in range(first_color_index, len(row)):
        pattern.append(row[i])

    # Check if the pattern repeats
    pattern_length = len(pattern)
    
    # Find the shortest repeating pattern
    for length in range(1, pattern_length + 1):
      if pattern_length % length == 0:
        sub_pattern = pattern[:length]
        if pattern == sub_pattern * (pattern_length // length):
          return sub_pattern

    return None
    

def detect_vertical_pattern(grid, key_colors):
    """Detects a repeating vertical pattern of colored and blank rows."""
    
    # find first colored row
    first_colored_row_index = -1
    for i, row in enumerate(grid):
      if np.any(row != 0):
        first_colored_row_index = i
        break

    if first_colored_row_index == -1:
        return None, None
        
    # determine horizontal pattern for first colored row
    horizontal_pattern = detect_horizontal_pattern(grid[first_colored_row_index])

    if horizontal_pattern is None:
      return None, None

    # determine repeating row pattern
    vertical_pattern = []
    
    rows, cols = grid.shape

    
    current_row_index = first_colored_row_index
    while current_row_index < rows:
      row = grid[current_row_index]
      if np.any(row != 0):
        vertical_pattern.append(horizontal_pattern)
      else:
         vertical_pattern.append([0] * len(horizontal_pattern))
      current_row_index += 1

    for length in range(1, len(vertical_pattern) + 1):
      if len(vertical_pattern) % length == 0:
        sub_pattern = vertical_pattern[:length]
        
        if vertical_pattern == sub_pattern * (len(vertical_pattern) // length):
           return sub_pattern, first_colored_row_index

    return None, None
      

def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)

    # find key colors
    key_colors = find_key_colors(input_grid)
    
    if len(key_colors) == 0:
        return output_grid

    # detect vertical pattern, and the starting row
    vertical_pattern, first_colored_row_index = detect_vertical_pattern(input_grid, key_colors)

    # build output
    if vertical_pattern:
      pattern_length = len(vertical_pattern)
      
      for row_index in range(rows):
        pattern_row = vertical_pattern[(row_index-first_colored_row_index) % pattern_length]
        
        output_grid[row_index, :len(pattern_row)] = pattern_row

    return output_grid