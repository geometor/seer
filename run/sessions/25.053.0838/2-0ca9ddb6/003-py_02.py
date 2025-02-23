"""
Transforms an input grid based on the location of red and blue pixels.

1.  **Red Pixel Rule:** For every red pixel in the input, keep it as is in output and add yellow pixels directly above and below if those adjacent spots exist within the grid boundary and contains white pixel.

2.  **Blue Pixel Rule:** For every blue pixel in the input, keep it as is in output and change the directly adjacent area, if any, into orange color (above, below, left, right, but *not* diagonals), if those adjacent spots exist within the grid boundary and are white.

3.   **Other Colors:** Pixels of any color other than red or blue remain unchanged in their position and color from input to the output.
"""

import numpy as np

def get_pixel(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        return grid[r][c]
    else:
        return None
    
def set_pixel(grid, r, c, value):
   if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        grid[r][c] = value
   
def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Iterate through each cell of the input_grid
    for r in range(rows):
        for c in range(cols):
            # Red pixel rule
            if input_grid[r][c] == 2:  # Red pixel found
                #output_grid[r][c] = 2 # keep the red pixel (this is redundant as output is copy)
                # Add yellow above and below if within bounds
                if r > 0 and input_grid[r-1][c] == 0 :
                    output_grid[r - 1][c] = 4  # Yellow
                if r < rows - 1 and input_grid[r+1][c] == 0:
                    output_grid[r + 1][c] = 4  # Yellow
                if c > 0 and input_grid[r][c-1] == 0:
                    output_grid[r][c-1] = 4
                if c < cols -1 and input_grid[r][c+1] == 0:
                    output_grid[r][c+1] = 4

            # Blue pixel rule
            elif input_grid[r][c] == 1:  # Blue pixel found
                # output_grid[r][c] = 1 # keep the blue pixel (this is redundant as output is copy)
                # Change adjacent cells to orange if within bounds
                if r > 0 and input_grid[r-1][c] == 0:
                    output_grid[r - 1][c] = 7  # Orange
                if r < rows - 1 and input_grid[r+1][c] == 0:
                    output_grid[r + 1][c] = 7  # Orange
                if c > 0 and input_grid[r][c-1] == 0:
                    output_grid[r][c - 1] = 7  # Orange
                if c < cols - 1 and input_grid[r][c+1] == 0:
                    output_grid[r][c + 1] = 7  # Orange

    return output_grid