"""
1.  **Identify the Blue Line:** Find the vertical, full-height blue (color 1) line in the input grid.  This line's column index is crucial.
2.  **Column Grouping:** Divide the input columns into three groups:
    *   Group 1: Columns to the left of the blue line (exclusive of the blue line).
    *   Group 2: The blue line itself.
    *   Group 3: Columns to the right of the blue line (exclusive of the blue line).
3.  **Output Grid Initialization:** Create an output grid with the same height as the input grid and three columns.
4.  **Column Mapping and Color Transformation:**
    *   **Group 1 -> Output Column 0:** For each row, examine all pixels in Group 1. If *all* pixels in Group 1 on that row are white (0), the corresponding pixel in output column 0 is white (0). Otherwise, the corresponding pixel in output column 0 is green (3).
    *   **Group 2 -> Output Column 1:** Map the blue line to column 1 in the output. The output will be blue (1).
    *   **Group 3 -> Output Column 2:** For each row, examine all pixels in Group 3. If *all* pixels in Group 3 on that row are white (0), the corresponding pixel in output column 2 is white (0). Otherwise, the corresponding pixel in output column 2 is green (3).
5.  **Return the output grid**
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the column index of a full-height vertical line of the specified color."""
    rows, cols = grid.shape
    for j in range(cols):
        if all(grid[i, j] == color for i in range(rows)):
            return j
    return -1  # Return -1 if no such line is found

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, 3), dtype=int)
    blue_line_col = find_vertical_line(input_grid, 1)

    # Group 2: Blue line
    for row in range(rows):
        output_grid[row, 1] = 1

    # Group 1 and Group 3 processing
    for row in range(rows):
        # Group 1
        all_white_left = True
        if blue_line_col > 0 :
          for col in range(0, blue_line_col):
              if input_grid[row, col] != 0:
                  all_white_left = False
                  break
        output_grid[row, 0] = 0 if all_white_left else 3

        # Group 3
        all_white_right = True

        if blue_line_col >= 0 and blue_line_col + 1 < cols:
          for col in range(blue_line_col + 1, cols):
              if input_grid[row, col] != 0:
                  all_white_right = False
                  break;
        output_grid[row, 2] = 0 if all_white_right else 3

    return output_grid