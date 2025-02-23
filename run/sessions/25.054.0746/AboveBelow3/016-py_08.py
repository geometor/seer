"""
The transformation involves identifying the top-most horizontal rectangle in the input grid and moving it down by one position (one row below current position).
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

                if width > 0: # is it a rectangle?
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

def move_rectangle_down(grid, start_pos, size, color):
    """Moves the specified rectangle down by one position."""
    new_grid = np.copy(grid)
    r, c = start_pos
    width, height = size

    # Clear old position
    for i in range(r, r + height):
        for j in range(c, c + width):
            new_grid[i, j] = 0

    # Set new position - one position down
    new_r = r + 1
    for i in range(new_r, new_r + height):
        for j in range(c, c + width):
          if i < new_grid.shape[0]:
            new_grid[i, j] = color

    return new_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the top-most horizontal rectangle
    top_rect = find_top_rectangle(output_grid)

    if top_rect:
        start_pos, size, color = top_rect
        # Move the rectangle down by one row
        output_grid = move_rectangle_down(output_grid, start_pos, size, color)

    return output_grid