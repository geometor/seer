"""
1. **Find the Most Frequent Color(s):** Examine the input grid and determine the color(s) that appear most frequently.
2. **Handle Ties:** If multiple colors share the highest frequency, consider all of them as the "target" colors.
3. **Create a Mask:**  Generate an output grid where:
    *   Pixels matching any of the most frequent color(s) in the input are set to black (0).
    *   All other pixels (those *not* matching any of the most frequent colors) are set to gray (5).
"""

import numpy as np
from collections import Counter

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find the most frequent color(s)
    counts = Counter(input_grid.flatten())
    max_count = max(counts.values())
    most_frequent_colors = [color for color, count in counts.items() if count == max_count]

    # Create a mask:
    #  - Pixels matching any of the most frequent colors are set to black (0).
    #  - All other pixels are set to gray (5).
    for row_index, row in enumerate(input_grid):
        for col_index, pixel in enumerate(row):
            if pixel in most_frequent_colors:
                output_grid[row_index, col_index] = 0  # Set to black
            else:
                output_grid[row_index, col_index] = 5  # Set to gray
    return output_grid