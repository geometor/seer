"""
1.  **Identify single-pixel objects:** Locate all pixels in the input grid that are not white (0) and are surrounded by white pixels (or the edge of the grid).
2.  **Expand objects:** For each identified single-pixel object, replace it with a 3x3 square of the same color. The original pixel should be the center of the new 3x3 square.
3. **Connect Objects with Gray Lines:** Find pairs of 3x3 colored squares that are close to each other (in this case, green and azure squares). Draw gray (5) colored one pixel wide horizontal lines between them. The line is drawn such that every other pixel on the input line is mirrored to a corresponding pixel on the output line. The lines should start in the middle row and middle column of each square.
"""

import numpy as np

def find_single_pixels(grid):
    # Find single pixels of non-white color
    single_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                is_single = True
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i != 0 or j != 0) and 0 <= r + i < rows and 0 <= c + j < cols:
                            if grid[r + i, c + j] != 0:
                                is_single = False
                                break
                    if not is_single:
                        break
                if is_single:
                    single_pixels.append((r, c, grid[r, c]))
    return single_pixels

def expand_to_square(grid, r, c, color):
    # Expand a single pixel to a 3x3 square
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= r + i < grid.shape[0] and 0 <= c + j < grid.shape[1]:
                grid[r + i, c + j] = color

def connect_with_gray_lines(grid, square1, square2):
    # Connect two 3x3 squares with gray lines, ensuring 1-pixel gap
    r1, c1, color1 = square1
    r2, c2, color2 = square2
    
    if c1<c2:
      start_col = c1+2
      end_col = c2-2
      row = r1
    else:
      start_col = c2+2
      end_col = c1-2
      row=r2

    if 0 <= row < grid.shape[0]:
        for c in range(start_col, end_col + 1):
          if (c-start_col)%2==0:
            if 0 <= c < grid.shape[1]:
              grid[row,c] = 5
              

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # 1. Find single pixels
    single_pixels = find_single_pixels(output_grid)

    # 2. Expand single pixels to 3x3 squares
    squares = []
    for r, c, color in single_pixels:
      expand_to_square(output_grid, r, c, color)
      squares.append((r,c,color))
    

    # 3. Connect squares with gray lines
    for i in range(len(squares)):
        for j in range(i + 1, len(squares)):
          connect_with_gray_lines(output_grid, squares[i], squares[j])

    return output_grid