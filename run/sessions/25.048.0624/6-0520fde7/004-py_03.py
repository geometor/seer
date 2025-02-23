"""
The updated transformation rule can be summarized as follows:

1. Identify the vertical line object (color 5) and its central column.
2. For each row, count the blue pixels (color 1) adjacent to the gray line.
3. Create a 3x3 output grid filled with color 0.
4. For each row, if the count of adjacent blue pixels is exactly 2, set the central pixel of that row in the output grid to color 2.
"""

import numpy as np

def count_adjacent_blue_pixels(grid, center_col):
    """
    Count the number of blue pixels (color 1) adjacent to the central column for each row.
    Returns a list of counts for each row.
    """
    rows, cols = grid.shape
    counts = []
    
    for r in range(rows):
        count = 0
        if center_col > 0 and grid[r, center_col - 1] == 1:
            count += 1
        if center_col < cols - 1 and grid[r, center_col + 1] == 1:
            count += 1
        counts.append(count)
    return counts

def transform(input_grid):
    """
    Transforms the input grid according to the updated rule.
    """
    # Initialize output grid as 3x3 with all zeros
    output_grid = np.zeros((3, 3), dtype=int)

    # Find the central column (assuming the gray line is always in the center)
    _, cols = input_grid.shape
    center_col = cols // 2

    # Count adjacent blue pixels for each row
    blue_counts_per_row = count_adjacent_blue_pixels(input_grid, center_col)

    # Update the output grid based on the counts
    for i, count in enumerate(blue_counts_per_row):
        if count == 2:
            output_grid[i, 1] = 2

    return output_grid