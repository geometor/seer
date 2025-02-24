# cf98881b • 006 • refine_coder

---
```python
"""
1.  **Identify Target Columns:** Examine the input grid. Identify columns that contain at least one pixel of color 9 (maroon), 4 (yellow), or 1 (blue).

2.  **Determine Column Output Order and Color Priority**:
    *   Find the *last* occurrence (highest row index) of each of the target colors (9, 4, and 1) within the *entire* input grid.
    *   Sort the target colors in descending order based on the row index of their last occurrence.
    * generate a list of target columns - preserving the original order
    * reorder the target columns based on color priority - if a column contains multiple colors from the target list, use the color with the highest priority.

3.  **Extract Subgrid:** Create a new grid (the "subgrid") consisting only of the target columns from the input grid, using the reordered column list from step 2.

4.  **Vertical Reduction:** For *each* column in the subgrid:
    *   Identify the *first* contiguous block of non-zero pixels.
    *   Set all other pixels in that column to 0 (white).

5.  **Column Limit:** Keep only the first 4 columns (or fewer, if less then 4 columns are available)

6.  **Output:** The resulting grid is the final output.
"""

import numpy as np

def get_target_columns(input_grid, target_colors):
    """
    Identifies columns containing any of the target colors, preserving original order.
    """
    target_columns = []
    for j in range(input_grid.shape[1]):
        for i in range(input_grid.shape[0]):
            if input_grid[i, j] in target_colors:
                target_columns.append(j)
                break  # Move to the next column
    return target_columns

def get_last_occurrence(input_grid, target_colors):
    """
    Finds the last occurrence (highest row index) of each target color.
    """
    last_occurrence = {}
    for color in target_colors:
        last_occurrence[color] = -1  # Initialize to -1

    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            color = input_grid[i, j]
            if color in target_colors:
                last_occurrence[color] = i

    return last_occurrence

def determine_color_priority(last_occurrence):
    """
    Sorts target colors based on the last occurrence row index (descending).
    """
    sorted_colors = sorted(last_occurrence.items(), key=lambda item: item[1], reverse=True)
    return [color for color, _ in sorted_colors]

def reorder_columns(input_grid, target_columns, color_priority):
    """
    Reorders target columns based on color priority.
    """
    reordered_columns = []
    column_colors = {}

    # determine color of column
    for col_index in target_columns:
      column = input_grid[:, col_index]
      colors_in_col = [c for c in color_priority if c in column]
      if colors_in_col:
        column_colors[col_index] = colors_in_col[0]

    for color in color_priority:
        for col_index in target_columns:
            if col_index in column_colors and column_colors[col_index] == color:
                reordered_columns.append(col_index)
    return reordered_columns

def extract_subgrid(input_grid, ordered_columns):
    """
    Extracts a subgrid based on the ordered target columns.
    """
    subgrid = input_grid[:, ordered_columns]
    return subgrid

def reduce_vertically(input_grid):
    """
    Keeps only the first contiguous block of non-zero pixels in each column.
    """
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    for j in range(cols):
        first_block_started = False
        first_block_ended = False
        for i in range(rows):
            if not first_block_started:
                if input_grid[i,j] != 0:
                    first_block_started = True
                    output_grid[i,j] = input_grid[i,j]
            elif not first_block_ended:
                if input_grid[i,j] == 0:
                    first_block_ended = True
                else:
                    output_grid[i,j] = input_grid[i,j]
    return output_grid

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    target_colors = [9, 4, 1]

    # get target columns in original order
    target_cols = get_target_columns(input_grid, target_colors)

    # get last occurrence of each target color
    last_occurrence = get_last_occurrence(input_grid, target_colors)
    
    # determine color priority
    color_priority = determine_color_priority(last_occurrence)
    
    # reorder the columns by color priority
    ordered_cols = reorder_columns(input_grid, target_cols, color_priority)

    # extract subgrid based on reordered columns
    subgrid = extract_subgrid(input_grid, ordered_cols)

    # perform vertical reduction
    reduced_grid = reduce_vertically(subgrid)

    # limit to at most first 4 columns
    output_grid = reduced_grid[:, :4]
    
    return output_grid.tolist()
```
