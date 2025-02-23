# 7837ac64 • 024 • refine_coder

---
```python
"""
The input grid is divided into nine 3x3 subgrids. Each subgrid maps to a single pixel in the output grid. The output color for each subgrid is determined as follows:

1.  **Count Colors:** Count the occurrences of each color (0-9) within the 3x3 subgrid.
2.  **Majority, excluding 0:** Find the color with highest count, ignoring 0.
3.  **Output Value:** If a color has more occurences than any other, the value of the output pixel will be the color with the highest count.
4.  **Zero Output:** If there are no colors other than zero or if there is a tie, output is 0.
"""

import numpy as np

def count_colors_in_subgrid(grid, row_start, col_start):
    """Counts the occurrences of each color in a 3x3 subgrid."""
    color_counts = np.zeros(10, dtype=int)
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            color = grid[row, col]
            color_counts[color] += 1
    return color_counts

def find_majority_color(color_counts):
    """Finds the color with the highest count, excluding 0."""
    max_count = 0
    majority_color = 0
    for color in range(1, 10):  # Iterate from 1 to 9 (excluding 0)
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            majority_color = color
        elif color_counts[color] == max_count and max_count >0:
            majority_color = 0 #reset in the case of a tie
    return majority_color

def transform(input_grid):
    # Initialize the output grid as a 3x3 array filled with white (0).
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid)

    # Iterate through each 3x3 subgrid.
    for row in range(3):
        for col in range(3):
            row_start = row * 3
            col_start = col * 3
            # Count color occurrences in the subgrid.
            color_counts = count_colors_in_subgrid(input_grid, row_start, col_start)
            # Determine the majority color (excluding 0).
            majority_color = find_majority_color(color_counts)
            # Set the output pixel value.
            output_grid[row, col] = majority_color

    return output_grid
```
