"""
1.  **Identify Objects:** Locate all contiguous blocks of pixels of the same color, excluding white (0) and blue (1). These are initial colored objects and are vertical strips.

2.  **Horizontal Expansion:**
    *   Iterate through each row of the grid.
    *   If a blue (1) pixel is horizontally adjacent to non-white and non-blue colors, change the blue pixel's color to the color of the strip.

3.  **Vertical Expansion:**
    * Iterate through each column.
    *   If a column contains colored objects (excluding 0 and 1), extend those colors vertically to fill the entire column, replacing blue(1) pixels. If a column has multiple colored objects, then expand all of them within the column.

4. **Preservation:**
    * The horizontal and vertical lines with color white(0) are preserved.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the rules."""
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Horizontal Expansion
    for row in range(rows):
        for col in range(cols):
            if output_grid[row, col] == 1:
                left_color = 0  # Default to white
                right_color = 0 # Default to white

                # Find the nearest non-blue/white color to the left
                for i in range(col - 1, -1, -1):
                    if output_grid[row, i] not in [0, 1]:
                        left_color = output_grid[row, i]
                        break

                # Find the nearest non-blue/white color to the right.
                for i in range(col + 1, cols):
                    if output_grid[row, i] not in [0, 1]:
                        right_color = output_grid[row, i]
                        break

                # if the color is between two non-white, non-blue pixels, propagate color
                if left_color != 0 and right_color != 0 and left_color == right_color:
                   output_grid[row,col] = left_color
                elif left_color != 0 and right_color != 0 :
                    output_grid[row, col] = left_color

    # Vertical Expansion
    for col in range(cols):
        column_colors = []
        for row in range(rows):
            color = output_grid[row, col]
            if color not in [0, 1]:
                column_colors.append((row, color))  # Store row index and color

        # Fill the entire column based on the colors found
        for row in range(rows):
           if output_grid[row,col] == 1:
              if len(column_colors) > 0:
                 for r, c in column_colors:
                   output_grid[row,col] = c

    return output_grid