"""
The task is to transform an input grid of colored pixels into an output grid of the same dimensions, where all pixels in the output grid have the same color, and the chosen color is present in the input grid. The chosen color is the one that appears most frequently in the input grid. If there is a tie, the rule is not yet known.
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Count color occurrences
    color_counts = Counter(input_grid.flatten())

    # Find the most frequent color.  Handle ties (imperfectly)
    max_count = 0
    fill_color = -1 # Initialize with a value not in 0-9 to indicate no color.

    for color, count in color_counts.items():
      if count > max_count:
        max_count = count
        fill_color = color
      # if there is a tie for color counts, we don't yet have a way to handle.
      # elif count == max_count:
        #fill_color = -1 # set fill color to error value

    # change output pixels
    if(fill_color >= 0):
      for i in range(rows):
          for j in range(cols):
              output_grid[i, j] = fill_color

    return output_grid