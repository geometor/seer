# 1e32b0e9 • 014 • example_3 • investigate_coder

---
```python
"""
Preserves two horizontal blue lines and green pixel locations, inserting blue pixels into columns with greens and alternating inserting a 1 in all other columns, *not* including those two rows of 1s.
"""

import numpy as np

def get_horizontal_blue_lines(grid):
    blue_lines = []
    for row_index, row in enumerate(grid):
        if all(pixel == 1 for pixel in row):
            blue_lines.append(row_index)
    return blue_lines

def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape
    blue_line_rows = get_horizontal_blue_lines(input_grid)

    # Iterate through each column
    for j in range(cols):
        # Check if the column contains a green pixel (3)
        col_has_green = any(input_grid[i][j] == 3 for i in range(rows))

        # Apply rules based on green presence
        for i in range(rows):

            # Skip horizontal blue lines
            if i in blue_line_rows:
              continue

            if col_has_green:
                if (j % 2 == 0) :  # every *other* column WITH Green.
                    #insert 1 if the current pixel is not blue(1) and there are currently no blues in this column
                    if input_grid[i][j] != 1 and not any(input_grid[row][j] == 1 for row in range(rows) if row not in blue_line_rows):
                        output_grid[i][j] = 1

            else:  #columns with NO green
                if (j % 2 == 0): #every *other* column with NO Green
                    if input_grid[i][j] != 1 and not any(input_grid[row][j] == 1 for row in range(rows) if row not in blue_line_rows) : #insert 1 if not blue.
                        output_grid[i][j] = 0
                else:
                    if input_grid[i][j] != 1 and not any(input_grid[row][j] == 1 for row in range(rows) if row not in blue_line_rows) :
                        output_grid[i][j] = 1

    return output_grid
```
