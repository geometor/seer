"""
1.  **Identify Input Sections:** Divide the input grid into two sections. The first section goes from the top of the grid until the last row that starts with a non-zero and non-one number. In the provided data this is row index `0` to `3`. The next section starts from first row that begins with either `0` or `1` until the end of the grid.
2.  **Determine Output Size:** The output grid has the same dimensions as the first identified section of the input.
3. **Locate Critical Input Cell** Find the `0` in first section of input grid which is surrounded by most `3`s, including diagonals.
4.  **Check Corresponding Cell in Second Section**: Check value in second section of input with same coordinates as `0` identified in previous step. If this value is `1`, this is location of non-zero value `2` for the output grid.
5.  **Create Output Grid:** Initialize an output grid of the determined size, filled with 0s.
6. **Find matching coordinate** Find the coordinates in input grid top section where value is `0` AND surrounded by maximum number of `3` AND the same coordinates in bottom section contains a `1`.
7.  **Populate Output:** Place a `2` in the output grid at the coordinates of `0` found in previous step. All other cells in the output grid remain 0.
"""

import numpy as np

def get_sections(grid):
    # split the grid into two sections based on row starting value
    rows = len(grid)
    section1_end_row = 0

    # Section 1 ends last row before a row starts with 0 or 1.
    for r in range(rows):
      if grid[r][0] == 0 or grid[r][0] == 1:
        section1_end_row = r
        break

    section1 = grid[:section1_end_row]
    section2 = grid[section1_end_row:]

    return np.array(section1), np.array(section2)

def count_surrounding(grid, r, c, value):
    # count surrounding cells with given value, including diagonals
    count = 0
    rows, cols = grid.shape
    for i in range(max(0, r - 1), min(rows, r + 2)):
        for j in range(max(0, c - 1), min(cols, c + 2)):
            if (i != r or j != c) and grid[i][j] == value:
                count += 1
    return count

def transform(input_grid):
    # get sections 
    section1, section2 = get_sections(input_grid)
    
    # initialize the output_grid with zeros and size of section1
    output_grid = np.zeros_like(section1)

    rows, cols = section1.shape
    max_threes = -1
    target_row, target_col = -1, -1
    
    # find zero cell in section 1 with most surrounding threes
    for r in range(rows):
        for c in range(cols):
            if section1[r][c] == 0:
              num_threes = count_surrounding(section1, r, c, 3)
              if num_threes > max_threes:
                #check second grid contains a 1 at same position
                if section2.size > 0 and section2[r][c] == 1:
                  max_threes = num_threes
                  target_row, target_col = r, c

    # set the corresponding cell in output_grid to 2
    if target_row != -1 and target_col != -1:
      output_grid[target_row][target_col] = 2

    return output_grid