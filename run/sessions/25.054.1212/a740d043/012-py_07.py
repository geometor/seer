"""
1.  **Identify Background:** Determine the most frequent color in the input grid. This is the background color.
2.  **Identify Distinct Colors:** Find all the unique colors in the input grid that are *different* from the background color.
3.  **Determine Output Rows:** The output grid has a number of rows equal to the number of rows in the input grid that contain at least one pixel that is *not* the background color.
4.  **Determine Output Columns:** The output grid has a number of columns equal to the greater of the number of distinct colors, and in cases with a single pixel of one color, add one column.
5. **Populate Output Grid:** Create the output grid filled with zeros. Iterate through the rows of the output:
   * if the row index is less that the number of distinct colors, fill the row with the next distinct color, starting with the first distinct color.
   * If any single color appears only once in the input, insert the 0 at the third column.
"""

import numpy as np
from collections import Counter

def find_background_color(grid):
    colors = Counter(grid.flatten())
    background_color = colors.most_common(1)[0][0]
    return background_color

def find_distinct_colors(grid, background_color):
    return sorted(list(set(grid.flatten()) - {background_color}))

def count_rows_with_distinct_colors(grid, background_color):
    count = 0
    for row in grid:
        if any(pixel != background_color for pixel in row):
            count += 1
    return count

def check_single_pixel_color(grid, distinct_colors):
    color_counts = Counter(grid.flatten())
    for color in distinct_colors:
        if color_counts[color] == 1:
            return True
    return False

def transform(input_grid):
    # Identify Background
    background_color = find_background_color(input_grid)

    # Identify Distinct Colors
    distinct_colors = find_distinct_colors(input_grid, background_color)
    num_distinct_colors = len(distinct_colors)

    # Determine Output Rows
    num_rows = count_rows_with_distinct_colors(input_grid, background_color)

    # Determine Output Columns
    num_cols = num_distinct_colors
    insert_zero = check_single_pixel_color(input_grid, distinct_colors)
    if insert_zero:
        num_cols += 1

    # Populate Output Grid
    output_grid = np.zeros((num_rows, num_cols), dtype=int)
    
    color_index = 0
    zero_inserted = False
    for i in range(num_rows):
        if color_index < len(distinct_colors):
            if insert_zero and len(distinct_colors)>1 and color_index == 2 and not zero_inserted:
                output_grid[i, 2] = 0 #insert at position
                zero_inserted = True
            else:
                output_grid[i, :] = distinct_colors[color_index]

            color_index += 1

    return output_grid