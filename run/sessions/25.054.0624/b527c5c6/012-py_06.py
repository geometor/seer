"""
1.  **Identify Green Rectangles:** Find all green (color 3) rectangles in the input grid.
2.  **Locate Red Pixel:** Within each green rectangle, find the single red (color 2) pixel.
3. **Determine Elongation Direction:**
    *   If the rectangle is wider than or equal to its height, prepare for horizontal elongation.
    *   If the rectangle is taller than its height, prepare for vertical elongation.
4.  **Elongate Within Rectangle:**
    *   **Horizontal Elongation**: Fill all empty (color 0) positions *within the rectangle* to the left and right of the red pixel with red, stopping at the rectangle's boundaries, or when a non-empty pixel is encountered.
    *  **Vertical Elongation:** Fill all empty positions *within the rectangle* above and below the red pixel with red, stopping at the rectangle's boundaries, or when a non-empty pixel is encountered.
    * **Square**: perform Both.
5.  **Extend to Edges:**
    * **Horizontal Elongation**: extend the bottom edge of the green rectangle to red, filling only empty spaces,
    *   **Vertical Elongation**: extend the left edge of the green rectangle, filling only empty spaces to red.
    * **Square:** perform Both.
"""

import numpy as np

def find_rectangles(grid, color):
    rectangles = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                # Found a potential start of a rectangle, try to expand
                width = 0
                while c + width < cols and grid[r, c + width] == color and not visited[r, c + width]:
                    width += 1
                height = 0
                while r + height < rows and all(grid[r + height, c + i] == color for i in range(width)) and not any(visited[r + height, c + i] for i in range(width)):
                    height += 1

                # Mark as visited
                for i in range(height):
                    for j in range(width):
                        visited[r + i, c + j] = True
                rectangles.append((r, c, width, height))
    return rectangles

def find_red_pixel(grid, rectangle, red_color=2):
    r, c, width, height = rectangle
    for i in range(height):
        for j in range(width):
            if grid[r + i, c + j] == red_color:
                return r + i, c + j
    return None

def transform(input_grid):
    output_grid = np.copy(input_grid)
    green_rectangles = find_rectangles(input_grid, 3)

    for rect in green_rectangles:
        red_pixel_pos = find_red_pixel(input_grid, rect)
        if red_pixel_pos:
            red_row, red_col = red_pixel_pos
            r, c, width, height = rect

            # Determine Elongation Direction
            if width >= height:  # Horizontal or Square
                # Elongate Within Rectangle (Horizontal)
                for i in range(width):
                    if output_grid[red_row, c + i] == 0:
                        output_grid[red_row, c + i] = 2
                # Extend to Bottom Edge
                for i in range(output_grid.shape[1]):
                    if output_grid[r + height - 1 ,i] == 0:
                         output_grid[r + height - 1, i] = 2


            if height > width:  # Vertical
                # Elongate Within Rectangle (Vertical)
                for i in range(height):
                     if output_grid[r + i,red_col] == 0:
                        output_grid[r + i, red_col] = 2
                # Extend to Left Edge
                for i in range(output_grid.shape[0]):
                    if output_grid[i,c] == 0:
                        output_grid[i, c] = 2
            if height == width:
                for i in range(height):
                     if output_grid[r + i,red_col] == 0:
                        output_grid[r + i, red_col] = 2
                # Extend to Left Edge
                for i in range(output_grid.shape[0]):
                    if output_grid[i,c] == 0:
                        output_grid[i, c] = 2

    return output_grid