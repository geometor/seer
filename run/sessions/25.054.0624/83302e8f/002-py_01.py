"""
1.  **Identify the "cross" shape:** Find the diagonal lines of azure (8) pixels forming an "X" in the center of the grid.

2.  **Recolor Inside Cross:** Starting from center outward, change azure(8) pixels to yellow(4), leaving only the outline of the cross in original color.

3. **Recolor Background Diagonally:** Recolor white(0) background pixels to green(3) or yellow(4) based on diagonal stripes starting from each cross arm, symmetrically, so that:
     - The white pixels that connect to the remaining azure pixels will be green
     - All remaining white pixels will be yellow.
"""

import numpy as np

def find_cross(grid):
    """Finds the coordinates of the azure cross."""
    rows, cols = grid.shape
    cross_coords = []
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 8:
                cross_coords.append((r, c))
    return cross_coords

def recolor_inside_cross(grid, cross_coords):
    """Recolors the inside of the cross to yellow."""
    # Create a copy to modify
    new_grid = np.copy(grid)

    #find center of cross by finding min and max row and col
    min_row = min(r for r, _ in cross_coords)
    max_row = max(r for r, _ in cross_coords)
    min_col = min(c for _, c in cross_coords)
    max_col = max(c for _, c in cross_coords)
    center_row = (min_row + max_row) // 2
    center_col = (min_col + max_col) // 2

    for r, c in cross_coords:
        #check if inside the cross
        if (r != min_row and r != max_row and
            c != min_col and c!= max_col):
            new_grid[r,c] = 4

    return new_grid


def recolor_background(grid, cross_coords):
    """Recolors the background in alternating stripes."""
    new_grid = np.copy(grid)
    rows, cols = grid.shape

    #find the cross coordinates that outline the cross
    cross_outline = []
    for r,c in cross_coords:
        if (r == min(row for row, _ in cross_coords) or
            r == max(row for row, _ in cross_coords) or
            c == min(col for _, col in cross_coords) or
            c == max(col for _, col in cross_coords)):
            cross_outline.append((r,c))
    
    #iterate through grid and change white to green if beside cross
    for r in range(rows):
        for c in range(cols):
            if new_grid[r, c] == 0:
                for cr, cc in cross_outline:
                    if abs(r - cr) <= 1 and abs(c - cc) <= 1:
                        new_grid[r, c] = 3
                        break

    #change remaining white background to yellow
    for r in range(rows):
        for c in range(cols):
            if new_grid[r,c] == 0:
                new_grid[r,c] = 4
    return new_grid

def transform(input_grid):
    # Find the coordinates of the cross
    cross_coords = find_cross(input_grid)

    # Recolor the inside of cross
    output_grid = recolor_inside_cross(input_grid, cross_coords)

    # Recolor the background
    output_grid = recolor_background(output_grid, cross_coords)

    return output_grid