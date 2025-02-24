"""
1.  **Identify and Preserve Horizontal Lines:** Find any horizontal, contiguous lines of color 2 or color 6 pixels on row 1 (second row). These lines, and their positions, remain unchanged in the output grid.
2.  **Remove Gray Pixels in Row 0:** All pixels of color 5 in the first row (row index 0) are removed, which may affect the width of the grid.
3.  **Process Gray Pixels in Row 1:** For any gray pixels (color 5) in the second row (row index 1), replace them based on adjacency with the following:

    *   If adjacent to a color 1 or 2, change to that color. If adjacent to BOTH, prioritize the color to the *right*.
    *   Propagate the replacement from right to left.
4.  **Process Gray Pixels in Row 2:** For any gray pixels (color 5) in the third row (row index 2):

    *   If adjacent to a color 3 or 8, change to that color. If adjacent to BOTH, prioritize the color to the *right*.
    *   Propagate the replacement from right to left.
5. The height of the grid is always 3.
"""

import numpy as np

def get_horizontal_lines(grid, row_index, colors):
    """
    Finds horizontal lines of specified colors in a given row.

    Args:
        grid: The input grid (numpy array).
        row_index: The index of the row to search.
        colors: A list of colors to search for.

    Returns:
        A list of tuples, where each tuple represents a horizontal line
        and contains (start_column, end_column, color).
    """
    lines = []
    rows, cols = grid.shape
    if row_index >= rows:
        return lines

    in_line = False
    start_col = -1
    current_color = -1

    for c in range(cols):
        if grid[row_index, c] in colors:
            if not in_line:
                in_line = True
                start_col = c
                current_color = grid[row_index, c]
            elif grid[row_index,c] != current_color:
                # color changed within the line
                lines.append( (start_col, c-1, current_color) )
                start_col = c
                current_color = grid[row_index,c]

        elif in_line:
            lines.append((start_col, c - 1, current_color))
            in_line = False

    if in_line:
        lines.append((start_col, cols - 1, current_color))

    return lines
def transform(input_grid):
    # initialize output_grid
    rows, cols = input_grid.shape
    output_grid = np.zeros((3,0), dtype=int)


    # 1. Identify and Preserve Horizontal Lines (Row 1)
    horizontal_lines = get_horizontal_lines(input_grid, 1, [2, 6])
    preserved_cols = []
    for start_col, end_col, color in horizontal_lines:
        segment = input_grid[1, start_col:end_col+1]
        output_grid = np.concatenate((output_grid, np.array([[0]*(end_col-start_col+1),[color]*(end_col-start_col+1),[0]*(end_col-start_col+1))), axis=1)
        preserved_cols.extend(range(start_col, end_col+1))

    # build a temporary grid for processing, removing the columns that are part
    # of the horizontal lines, so we do not overwrite
    temp_grid = np.copy(input_grid)

    # 2. Remove Gray Pixels in Row 0 and build new temporary grid
    temp_cols = []
    for c in range(cols):
        if c not in preserved_cols:
            if temp_grid[0,c] != 5:
                temp_cols.append(c)
        else:
            temp_cols.append(c)

    temp_grid_filtered = temp_grid[:, temp_cols]

    # 3 & 4: Process the filtered data
    rows_temp, cols_temp = temp_grid_filtered.shape
    new_temp_grid = np.copy(temp_grid_filtered)

    for r in range(rows_temp):
        for c in range(cols_temp -1, -1, -1): # right to left
            if new_temp_grid[r,c] == 5:
                if r == 1:
                    if c < cols_temp - 1 and new_temp_grid[r,c+1] in [1,2]:
                        new_temp_grid[r,c] = new_temp_grid[r,c+1]
                    elif c > 0 and new_temp_grid[r,c-1] in [1,2]:
                        new_temp_grid[r,c] = new_temp_grid[r,c-1]
                    else:
                         new_temp_grid[r,c] = 0 # default
                if r == 2:
                    if c < cols_temp - 1 and new_temp_grid[r,c+1] in [3,8]:
                        new_temp_grid[r,c] = new_temp_grid[r,c+1]
                    elif c > 0 and new_temp_grid[r,c-1] in [3,8]:
                        new_temp_grid[r,c] = new_temp_grid[r,c-1]
                    else:
                         new_temp_grid[r,c] = 0

    # merge the new temp grid with the output grid
    output_rows, output_cols = output_grid.shape
    temp_rows, temp_cols = new_temp_grid.shape
    final_output = np.zeros((3,0), dtype=int)
    temp_idx = 0
    out_idx = 0

    for c in range(cols):
        if c in preserved_cols: # part of preserved line
            # search output grid to insert
            found = False
            for ec in range(output_cols):
                if output_grid[1,ec] == input_grid[1,c] and not found:
                    final_output = np.concatenate( (final_output, output_grid[:, ec:ec+1]), axis=1 )
                    found = True

        elif temp_idx < temp_cols and temp_grid_filtered[0,temp_idx] == input_grid[0,c] \
             and temp_grid_filtered[1, temp_idx] == input_grid[1,c] \
             and temp_grid_filtered[2, temp_idx] == input_grid[2,c]:
            final_output = np.concatenate((final_output, new_temp_grid[:, temp_idx:temp_idx+1]), axis=1)
            temp_idx += 1

    return final_output