# 39e1d7f9 • 012 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all 3x3 squares in the input grid. Note their colors and top-left corner positions.

2.  **Swap Rule:** If there are 3x3 squares of yellow (4) and magenta (6), they swap positions. The swapping process involves these steps for each pair:
    *   Record the top-left coordinates of both the yellow and magenta squares.
    *   Copy the 3x3 yellow square to the original top-left position of the magenta square in the output grid.
    *  Copy the 3x3 magenta square to the original top-left position of the yellow square in the output grid.

3.  **Preserve Context (Restoration around swapped elements):**
    + Immediately after swapping any pair of squares:
      * The 5x5 area centered on the *original* top-left corner of the magenta 3x3 region is copied from input to output.
      * The 5x5 area centered on the *original* top-left corner of the yellow 3x3 region is copied from input to output.

4.  **Other 3x3 blocks:**
    + Blocks of color green(3) are translated one row up.
    + Blocks of color red(2) are translated one column right.

5.  **Other Pixels:**
    + All other pixels that are *not* involved with swapping or translating operations are copied from input directly to output.

"""

import numpy as np

def find_squares(grid, color=None):
    """Finds the top-left corner coordinates of all 3x3 squares of a given color (or any color if color is None)."""
    squares = []
    rows, cols = grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            if color is None or np.all(grid[r:r+3, c:c+3] == color):
                squares.append((r, c))
    return squares

def copy_square(grid, r, c, size=3):
    """Copies a square region from the grid."""
    return np.copy(grid[r:r+size, c:c+size])

def paste_square(grid, r, c, square):
    """Pastes a square region into the grid."""
    size = square.shape[0]
    grid[r:r+size, c:c+size] = square
    
def restore_context(input_grid, output_grid, r, c, size=5):
    """Copies a region of size x size centered at (r+1, c+1) from input_grid to output_grid."""
    
    r0 = max(0, r - (size//2))
    r1 = min(output_grid.shape[0], r + (size//2) + 2)
    c0 = max(0, c- (size//2))
    c1 = min(output_grid.shape[1], c + (size//2) + 2)
    
    output_grid[r0:r1,c0:c1] = input_grid[r0:r1,c0:c1]


def transform(input_grid):
    # Initialize output_grid
    output_grid = np.copy(input_grid)

    # Find objects
    yellow_squares = find_squares(input_grid, 4)
    magenta_squares = find_squares(input_grid, 6)
    green_squares = find_squares(input_grid,3)
    red_squares = find_squares(input_grid, 2)

    # Swap yellow and magenta squares
    for y_r, y_c in yellow_squares:
        for m_r, m_c in magenta_squares:
            # Copy squares
            yellow_square = copy_square(input_grid, y_r, y_c)
            magenta_square = copy_square(input_grid, m_r, m_c)

            # Paste squares in swapped positions
            paste_square(output_grid, y_r, y_c, magenta_square)
            paste_square(output_grid, m_r, m_c, yellow_square)
            
            #restore
            restore_context(input_grid,output_grid,y_r,y_c)
            restore_context(input_grid,output_grid,m_r,m_c)

    # Translate green blocks up
    for g_r,g_c in green_squares:
        green_square = copy_square(input_grid,g_r,g_c)
        if(g_r > 0):
          paste_square(output_grid,g_r-1,g_c,green_square)
          #restore
          restore_context(input_grid, output_grid, g_r - 1,g_c)
        
    # Translate red blocks right
    for r_r, r_c in red_squares:
        red_square = copy_square(input_grid, r_r, r_c)
        if(r_c < input_grid.shape[1]):
            paste_square(output_grid,r_r,r_c + 1,red_square)
            restore_context(input_grid,output_grid,r_r,r_c + 1)
    
    return output_grid
```
