"""
1. Identify Horizontal Lines: For each row in the input grid, find contiguous horizontal lines of the same color.
2. Find Most Frequent Horizontal Line Color: Determine the color that appears most frequently within those horizontal lines across the entire grid.
3. Transform Colors, most frequent first:
    *   Pixels matching that color become Gray (5).
    *   All other pixels become White (0).
"""

import numpy as np
from collections import Counter

def find_horizontal_lines(grid):
    """Finds contiguous horizontal lines of the same color in each row."""
    lines = []
    for row in grid:
        current_line = []
        for i in range(len(row)):
            if i == 0:
                current_line.append((row[i], 1))  # (color, length)
            else:
                if row[i] == current_line[-1][0]:
                    current_line[-1] = (row[i], current_line[-1][1] + 1)
                else:
                    current_line.append((row[i], 1))
        lines.append(current_line)
    return lines

def most_frequent_horizontal_line_color(lines):
    """Determines the most frequent color across all horizontal lines."""
    color_counts = Counter()
    for row_lines in lines:
        for color, length in row_lines:
            color_counts[color] += length  # count all pixels, not lines
    if not color_counts: # handle the case with empty grid
      return None
    most_common_color = color_counts.most_common(1)[0][0]
    return most_common_color

def transform(input_grid):
    """Transforms the input grid based on the most frequent horizontal line color."""
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find horizontal lines
    lines = find_horizontal_lines(input_grid)

    # Find the most frequent color in horizontal lines
    most_frequent_color = most_frequent_horizontal_line_color(lines)
    if most_frequent_color is None:
        return output_grid # return blank grid

    # Transform pixels:  most_frequent_color to Gray(5), others to White (0)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == most_frequent_color:
                output_grid[i, j] = 5
            else:
                output_grid[i, j] = 0

    return output_grid