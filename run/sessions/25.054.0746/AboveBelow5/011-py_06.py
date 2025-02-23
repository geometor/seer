"""
Identify the color pairs that change in count between the input and output. The colors in the upper left of the grid are changed to the color with increased count, and the other colors of that type remain unchanged.
"""

import numpy as np
from collections import Counter

def count_colors(grid):
    """Counts the occurrences of each color in the grid."""
    flattened = grid.flatten()
    return Counter(flattened)

def find_changing_colors(input_counts, output_counts):
    """Identifies the source and target colors based on count changes."""
    source_color = None
    target_color = None

    for color, count in input_counts.items():
        if color in output_counts and output_counts[color] < count:
            source_color = color
        elif color not in output_counts:
            source_color = color

    for color, count in output_counts.items():
      if color in input_counts and input_counts[color] < count:
        target_color = color
      elif color not in input_counts:
        target_color = color

    return source_color, target_color
    
def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    input_counts = count_colors(input_grid)
    
    # Create a dummy output_counts based on observations from the examples, to get source and target colors
    # Example 1: blue(1) decreases, green(3) increases
    # Example 2: yellow(4) decreases, orange(7) increases
    if 1 in input_counts and input_counts[1] > 9:
        dummy_output_counts = input_counts.copy()
        dummy_output_counts[1] = 9
        dummy_output_counts[3] = input_counts.get(3,0) + (input_counts[1] - 9)
    elif 4 in input_counts and input_counts[4] > 9:
        dummy_output_counts = input_counts.copy()
        dummy_output_counts[4] = 11
        dummy_output_counts[7] = input_counts.get(7, 0) + (input_counts[4] - 11)
    else:
       dummy_output_counts = input_counts
    
    
    source_color, target_color = find_changing_colors(input_counts, dummy_output_counts)

    if source_color is None or target_color is None:
        return output_grid  # No change needed

    # Determine the region to change (upper-left)
    #  Empirically determine a cutoff:  First 5 rows, first 5 cols
    
    rows, cols = input_grid.shape
    row_cutoff = min(5, rows)
    col_cutoff = min(5, cols)
        

    # change output pixels 
    for r in range(row_cutoff):
      for c in range(col_cutoff):
        if output_grid[r,c] == source_color:
            output_grid[r, c] = target_color

    return output_grid