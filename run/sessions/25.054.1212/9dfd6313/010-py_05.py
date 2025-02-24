"""
1.  **Gray Anchors:** Identify all gray (5) pixels within the input grid. These pixels remain stationary in the output grid, serving as anchors.

2.  **Magenta Positioning:** Locate all magenta (6) pixels. Sort these pixels first by their original column index and then by their original row index, preserving their relative order. Place the magenta pixels in the top-right section of the output grid, starting at column 2 and proceeding right and then down.

3. **Yellow Positioning:** Locate yellow (4) pixel. Place the yellow pixel directly above the bottom-rightmost gray pixel.

4. **Relative Positioning of Other Colors (General Rule):** The input grid appears to be rearranged into sections of the output grid based on the position of the gray (5) pixels.
    - all colors in columns to the left of the leftmost gray pixel in a row are placed to the left of the leftmost gray in the output.
    - all pixels between gray pixels in a row are placed in between the same gray pixels in the output
    - pixels right of the rightmost gray in an input row, go to the right of rightmost gray in the output.

5. **Grid Size:** The output grid has the same dimensions as the input grid.
"""

import numpy as np

def get_colored_pixels(grid, color):
    """
    Finds the coordinates of all pixels of a specified color.
    Returns a list of (row, col) tuples.
    """
    pixels = []
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color:
                pixels.append((row, col))
    return pixels

def transform(input_grid):
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # 1. Place gray (5) pixels (anchors)
    gray_pixels = get_colored_pixels(input_grid, 5)
    for r, c in gray_pixels:
        output_grid[r, c] = 5

    # 2. Place magenta (6) pixels
    magenta_pixels = get_colored_pixels(input_grid, 6)
    magenta_pixels.sort(key=lambda x: (x[1], x[0]))  # Sort by column, then row
    magenta_target_row = 0
    magenta_target_col = 2
    for _ in magenta_pixels:
        while output_grid[magenta_target_row, magenta_target_col] != 0:
          magenta_target_col += 1
          if magenta_target_col >= cols:
              magenta_target_row += 1
              magenta_target_col = 2
              if magenta_target_row >= rows:
                break
        if magenta_target_row < rows:
          output_grid[magenta_target_row, magenta_target_col] = 6

    # 3. Place yellow (4) pixel
    yellow_pixels = get_colored_pixels(input_grid, 4)
    if yellow_pixels:
        bottom_right_gray = None
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if input_grid[r, c] == 5:
                    bottom_right_gray = (r, c)
                    break
            if bottom_right_gray:
                break
        if bottom_right_gray:
            target_r, target_c = bottom_right_gray[0] - 1, bottom_right_gray[1]
            if target_r >= 0:
              output_grid[target_r, target_c] = 4
    
    # 4. Place other colored pixels based on relative position to gray pixels
    for r in range(rows):
        input_gray_cols = [c for c in range(cols) if input_grid[r, c] == 5]
        output_gray_cols = [c for c in range(cols) if output_grid[r, c] == 5]

        if not input_gray_cols:  # No gray pixels in this row
            # Place non-gray pixels sequentially
            output_col = 0
            for c in range(cols):
                if input_grid[r,c] != 5:
                    while output_col < cols and output_grid[r, output_col] != 0 :
                      output_col +=1
                    if output_col < cols:
                      output_grid[r, output_col] = input_grid[r,c]

            continue

        #place pixels to left of the leftmost gray
        output_col = 0
        for c in range(input_gray_cols[0]):
          if input_grid[r,c] != 5:
            while output_col < output_gray_cols[0] and output_grid[r,output_col] != 0:
              output_col += 1
            if output_col < output_gray_cols[0]:
              output_grid[r,output_col] = input_grid[r,c]
        
        #place pixels between gray pixels
        for i in range(len(input_gray_cols)-1):
          input_start = input_gray_cols[i] + 1
          input_end = input_gray_cols[i+1]
          output_start = output_gray_cols[i] + 1
          output_end = output_gray_cols[i+1]

          output_col = output_start
          for c in range(input_start, input_end):
            if input_grid[r,c] != 5:
              while output_col < output_end and output_grid[r, output_col] != 0:
                output_col += 1
              if output_col < output_end:
                output_grid[r, output_col] = input_grid[r,c]
        
        #place pixels to the right of rightmost gray
        output_col = output_gray_cols[-1] + 1
        for c in range(input_gray_cols[-1] + 1, cols):
          if input_grid[r,c] != 5:
            while output_col < cols and output_grid[r,output_col] != 0:
              output_col += 1
            if output_col < cols:
              output_grid[r,output_col] = input_grid[r,c]

    return output_grid