# b527c5c6 • 010 • refine_coder

---
```python
"""
1.  **Identify Green Rectangles:** Locate all green (3) rectangles in the input grid.
2.  **Find Red Pixel:** Within each green rectangle, locate the single red (2) pixel.
3.  **Horizontal Elongation (wider than tall):** if a rectangle is wider than tall, copy its red pixel to *all* positions to the left within that rectangle. Copy the red pixel to *all* empty positions along the bottom edge of the *entire* rectangle.
4.  **Vertical Elongation (taller than wide)** If a rectangle is taller than wide, copy the red pixel to *all* positions directly above, within the bounds of that rectangle. copy the red pixel to *all* empty positions along the leftmost edge of the *entire* rectangle.
5.  **Square elongation (equal height and width)** Perform both horizontal and
    vertical actions.
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
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    green_rectangles = find_rectangles(input_grid, 3)

    for rect in green_rectangles:
        red_pixel_pos = find_red_pixel(input_grid, rect)
        if red_pixel_pos:
            red_row, red_col = red_pixel_pos
            r, c, width, height = rect

            # Horizontal Elongation (wider than tall)
            if width > height:
                # Copy to the left
                for i in range(c, red_col):
                    output_grid[red_row, i] = 2
                # Copy to the bottom edge
                for i in range(width):
                    output_grid[r + height - 1, c + i] = 2

            # Vertical Elongation (taller than wide)
            elif height > width:
                # Copy above
                for i in range(r, red_row):
                    output_grid[i, red_col] = 2
                #copy to the left edge
                for i in range(height):
                    output_grid[r+i,c]=2
            # Square Elongation
            else:
                # Copy to the left
                for i in range(c, red_col):
                    output_grid[red_row, i] = 2
                # Copy to the bottom edge
                for i in range(width):
                    output_grid[r + height - 1, c + i] = 2
                # Copy above
                for i in range(r, red_row):
                    output_grid[i, red_col] = 2
                #copy to the left edge
                for i in range(height):
                    output_grid[r+i,c]=2

    return output_grid
```
