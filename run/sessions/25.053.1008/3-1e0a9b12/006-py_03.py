"""
1.  **Identify Key Colors:** Focus on pixels with colors 3 (green), 6 (magenta), 1 (blue), and 2 (red).

2.  **Green (3) Movement:** Move any green (3) pixels down to the row directly above any other present color (6, 1 or 2). If other color pixels occupy all the rows, move color 3 down as far down as possible.

3.  **Magenta (6) Placement:** Place the magenta (6) pixel in the bottom-left corner (row 4, column 0).

4.  **Blue (1) and Red (2) Movement:** Move the blue (1) and red (2) pixels such that they retain their relative horizontal relationship. The blue and red will occupy the two rightmost spaces, placing the blue pixel in the first available spot in the first available row from the bottom up. Then place the red pixel relative to the blue one.

5.  **Clear Remaining:** All other cells are set to white (0).
"""

import numpy as np

def find_pixels(grid, color):
    # Find coordinates of all pixels of a specific color.
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == color]

def transform(input_grid):
    input_grid = np.array(input_grid)  # Convert to numpy array for easier manipulation
    output_grid = np.zeros_like(input_grid)  # Initialize output grid with all zeros (white)
    rows, cols = input_grid.shape

    # Green (3) Movement
    green_pixels = find_pixels(input_grid, 3)
    if green_pixels:
        target_row = rows -1 # default to the last row
        for row in range(rows -1, -1, -1):
            if any(input_grid[row,col] in [1,2,6] for col in range(cols)):
              target_row = row -1
              break
                
        for i in range(len(green_pixels)):
          output_grid[min(target_row + i, rows-1)][green_pixels[i][1]] = 3
          
    # Magenta (6) Placement
    magenta_pixels = find_pixels(input_grid, 6)
    if magenta_pixels:
        output_grid[rows - 1, 0] = 6

    # Blue (1) and Red (2) Movement
    blue_pixels = find_pixels(input_grid, 1)
    red_pixels = find_pixels(input_grid, 2)

    if blue_pixels and red_pixels:
        
        #find x diff
        red_x_diff = red_pixels[0][1] - blue_pixels[0][1]

        #find target row
        target_row = rows - 1
        for row in range(rows-1, -1, -1):
          if any(output_grid[row,col] != 0 for col in range(cols)):
            target_row = row-1
            break
        
        #place according to diff
        output_grid[target_row, cols-2] = 1 #place blue
        output_grid[target_row, cols-2 + red_x_diff] = 2  # Place red relative to blue

    return output_grid.tolist()