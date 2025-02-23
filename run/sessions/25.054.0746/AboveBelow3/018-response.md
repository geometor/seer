# AboveBelow3 • 018 • refine_coder

---
```python
"""
1.  **Identify the top-most rectangle:** Iterate through the grid, from top to bottom and left to right, to find the rectangle that starts at the highest row. A rectangle is defined as a contiguous block of pixels of the same color, with a width of at least 2 and where all the rows are complete to that width.
2.  **Determine Destination Row:** The destination for this rectangle is the row immediately below its original *top* row, unless it would overlap other objects, in which case it is skipped..
3.  **Clear Source:** The source area of the top-most rectangle is cleared (all pixels set to black/0).
4.  **Redraw Rectangle:** Redraw the rectangle at the new position. The new top row of the rectangle becomes the destination row.
"""

import numpy as np

def find_top_rectangle(grid):
    """Finds the top-most horizontal rectangle in the grid."""
    rows, cols = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    top_rectangle = None
    top_row = rows  # Initialize with a row number that's beyond the grid

    for r in range(rows):
        for c in range(cols):
            if not visited[r, c] and grid[r, c] != 0:
                color = grid[r, c]
                width = 0
                # Check for horizontal rectangle
                c_temp = c
                while c_temp < cols and grid[r, c_temp] == color:
                    width += 1
                    c_temp += 1

                if width > 1: # is it a rectangle? width must be > 1
                    # check if all rows below until color changes are same
                    height = 1
                    r_temp = r + 1
                    valid_rect = True
                    while r_temp < rows and grid[r_temp,c] == color:
                        for i in range(width):
                            if c + i >= cols or grid[r_temp, c+i] != color:
                                valid_rect = False
                                break
                        if not valid_rect:
                            break

                        height += 1
                        r_temp += 1

                    if valid_rect: # we found a rectangle, now check to mark it as visited.
                        for i in range(r, r + height):
                            for j in range(c, c + width):
                                visited[i,j] = True

                        if r < top_row: # is this the top most?
                            top_row = r
                            top_rectangle = ((r, c), (width, height), color)


    return top_rectangle

def redraw_rectangle(grid, start_pos, size, color):
    """Redraws the rectangle at the new position."""
    new_grid = np.copy(grid)
    r, c = start_pos
    width, height = size
    new_r = r + 1  # Destination row is one below the original top row

    # Check for out of bounds
    if new_r + height > new_grid.shape[0]:
        return new_grid  # Don't move if it goes out of bounds

    # clear source
    for i in range(r, r+height):
      for j in range(c, c+width):
        new_grid[i,j] = 0

    # Redraw at new position
    for i in range(new_r, new_r + height):
        for j in range(c, c + width):
            new_grid[i, j] = color

    return new_grid
def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the top-most horizontal rectangle
    top_rect = find_top_rectangle(output_grid)

    # If a rectangle is found, redraw it one row down.
    if top_rect:
        start_pos, size, color = top_rect
        output_grid = redraw_rectangle(output_grid, start_pos, size, color)
    return output_grid
```
