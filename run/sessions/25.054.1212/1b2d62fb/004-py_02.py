"""
1.  **Find the Vertical Blue Line:** Locate the column index of the vertical line of blue (1) pixels in the input grid.

2.  **Identify Rows with Azure:** Find all rows in the *input* grid that contain one or more azure (8) pixels.

3.  **Determine Output Grid Height:** The output grid's height equals the number of rows identified in step 2, plus additional padding rows as needed.

4.  **Create the Output Grid:** Initialize an output grid of dimensions *height* (from step 3) x 3, filled with white (0) pixels.

5.  **Map Azure Pixels:** For each row in the *input* grid that contains azure pixels:
    *   Find the horizontal distance (number of columns) between each Azure pixel and the blue line.
    *   In the corresponding row of the *output grid*, if the azure pixel is to the left of the blue line set a pixel at column 0. if the azure pixel is to the right of the blue line, set column 2. If the azure pixel is at the blue line column: set column 1.

6. **Return Output Grid:** The resulting output grid is the transformed output.
"""

import numpy as np

def find_vertical_line(grid, color):
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i,j] == color for i in range(rows)):
            return j
    return -1

def find_azure_rows(grid):
    rows, _ = grid.shape
    azure_rows = []
    for i in range(rows):
        if 8 in grid[i]:
            azure_rows.append(i)
    return azure_rows

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find the vertical blue line.
    blue_line_col = find_vertical_line(input_grid, 1)

    # Find rows containing azure pixels.
    azure_rows = find_azure_rows(input_grid)

    # Determine output grid height.
    if len(azure_rows)==0:
        output_height = rows
    else:
        output_height = rows #len(azure_rows)
    # Create the output grid.
    output_grid = np.zeros((output_height, 3), dtype=int)

    # Map azure pixels to the output grid.
    if blue_line_col != -1:  # Ensure blue line exists
       
        output_row_index = 0
        for input_row_index in range(rows):
          if 8 in input_grid[input_row_index]:
            for col_index in range(cols):
                if input_grid[input_row_index, col_index] == 8:
                    if col_index < blue_line_col:
                        output_grid[input_row_index, 0] = 8
                    elif col_index > blue_line_col:
                        output_grid[input_row_index, 2] = 8
                    else:
                        output_grid[input_row_index, 1] = 8
          else:
            # copy non-azure rows to corresponding output row if blue exists
            if rows == output_height:
              if blue_line_col !=-1:
                output_grid[input_row_index,1] = 8
                output_grid[input_row_index,2] = 8


    return output_grid