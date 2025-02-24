"""
1.  **Grid Dimensions:** The output grid has the same dimensions as the input grid.

2.  **Gray Anchors:** Identify all gray (5) pixels in the input grid.  These pixels maintain their exact positions in the output grid.

3.  **Magenta Placement:**  Locate all magenta (6) pixels. Place these pixels in the top-right section of the output grid.  Start at the first row and the first column *after* any gray pixels in that row. If a gray pixel is at the last position in the row, start at the first position of that row. Fill available positions to the right, and if no space remains and more magenta pixels are left, move down to the beginning of the next row (column 0) and repeat until all magenta pixels are placed.

4.  **Yellow Placement:** Locate the yellow (4) pixel. Find the bottom-rightmost gray pixel in the grid. Place the yellow pixel one row above and in the same column as the bottom-rightmost gray pixel. If there is no row above, place yellow in the same row as the gray pixel. If there are multiple gray pixels on the last row, use the right-most of those.

5. **Relative Positioning within Rows (General Rule):**
    *   Iterate through each row of the input grid.
    *   Identify the gray pixels (if any) in the current row. These act as anchors for that row.
    *   For pixels *before* the first gray pixel in the row: Place these in the output grid, in the same row, in the columns before the corresponding gray pixel. Maintain the original order.
    *   For pixels *between* gray pixels: Place these pixels in the output grid, in the same row, in the columns between the corresponding gray pixels. Maintain the original order. If the space is already full, continue to the next available space in the next row (wrapping around to the start of the grid if necessary).
    *   For pixels *after* the last gray pixel in the row:  Place these in the output grid, in the same row, after the last gray pixel. Maintain their original order.
    *   If a row has *no* gray pixels: Place all non-gray pixels on that row, in order, at the end of the output grid - filling available space from left to right, continuing on the following rows if necessary.

    *   **All color pixels (other than gray) must be re-arranged in the output grid**
"""

import numpy as np

def get_colored_pixels(grid, color):
    """
    Finds the coordinates of all pixels of a specified color.
    Returns a list of (row, col) tuples.
    """
    return [(r, c) for r in range(grid.shape[0]) for c in range(grid.shape[1]) if grid[r, c] == color]

def find_bottom_right_gray(grid):
    """Finds the bottom-rightmost gray pixel."""
    gray_pixels = get_colored_pixels(grid, 5)
    if not gray_pixels:
        return None
    return max(gray_pixels, key=lambda x: (x[0], x[1]))

def transform(input_grid):
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Place gray (5) pixels (anchors)
    for r, c in get_colored_pixels(input_grid, 5):
        output_grid[r, c] = 5

    # 2. Place magenta (6) pixels
    magenta_pixels = get_colored_pixels(input_grid, 6)
    magenta_row = 0
    magenta_col = 0
    for _ in magenta_pixels:
        # Find the next available position for magenta
        while magenta_row < rows:
            if output_grid[magenta_row, magenta_col] == 0:
                if any(input_grid[magenta_row,:] == 5) and not any(output_grid[magenta_row, 0:cols] == 5):
                    #gray is present and this slot is free
                    break

                elif not any(input_grid[magenta_row,:] == 5) and output_grid[magenta_row, magenta_col] == 0:
                  #no gray in the row
                  break

                elif any(output_grid[magenta_row, 0:magenta_col] == 5) and output_grid[magenta_row, magenta_col] == 0:
                    #the gray is left of this slot and the slot is free
                    break

            magenta_col += 1
            if magenta_col >= cols:
                magenta_col = 0
                magenta_row += 1
            
            if magenta_row >= rows:
               break

        if magenta_row < rows:
            output_grid[magenta_row, magenta_col] = 6

    # 3. Place yellow (4) pixel
    yellow_pixels = get_colored_pixels(input_grid, 4)
    bottom_right_gray = find_bottom_right_gray(input_grid)
    if yellow_pixels and bottom_right_gray:
        target_r, target_c = bottom_right_gray
        target_r -= 1  # Try above
        if target_r < 0:
            target_r = bottom_right_gray[0]  # Same row if no row above
        output_grid[target_r, target_c] = 4

    # 4. Relative Positioning within Rows
    next_available_row = 0
    next_available_col = 0

    for r in range(rows):
        gray_cols_input = [c for c in range(cols) if input_grid[r, c] == 5]
        gray_cols_output = [c for c in range(cols) if output_grid[r,c] == 5]

        if not gray_cols_input:  # No gray pixels in this row
            for c in range(cols):
                if input_grid[r,c] != 5:
                    while next_available_row < rows:
                      if output_grid[next_available_row, next_available_col] == 0:
                        break;
                      next_available_col += 1
                      if next_available_col >= cols:
                        next_available_col = 0
                        next_available_row += 1

                    if next_available_row < rows:
                      output_grid[next_available_row,next_available_col] = input_grid[r,c]

        else:
            # Pixels before the first gray
            output_col = 0
            for c in range(gray_cols_input[0]):
              if input_grid[r, c] != 5:
                while output_col < gray_cols_output[0] and output_grid[r, output_col] != 0:
                    output_col += 1
                if output_col < gray_cols_output[0]:
                  output_grid[r, output_col] = input_grid[r, c]

            # Pixels between gray pixels
            for i in range(len(gray_cols_input) - 1):
                input_start = gray_cols_input[i] + 1
                input_end = gray_cols_input[i+1]
                output_start = gray_cols_output[i] + 1
                output_end = gray_cols_output[i+1]
                
                output_col = output_start

                for c in range(input_start, input_end):
                    if input_grid[r, c] != 5:
                      while next_available_row < rows:
                        if output_grid[next_available_row, next_available_col] == 0:
                          break;
                        next_available_col += 1
                        if next_available_col >= cols:
                          next_available_col = 0
                          next_available_row += 1

                      if next_available_row < rows:
                        output_grid[next_available_row, next_available_col] = input_grid[r,c]

            # Pixels after the last gray
            output_col = gray_cols_output[-1] + 1
            for c in range(gray_cols_input[-1] + 1, cols):
                if input_grid[r, c] != 5:
                  while next_available_row < rows:
                    if output_grid[next_available_row, next_available_col] == 0:
                      break;
                    next_available_col += 1
                    if next_available_col >= cols:
                      next_available_col = 0
                      next_available_row += 1

                  if next_available_row < rows:
                    output_grid[next_available_row,next_available_col] = input_grid[r,c]

    return output_grid