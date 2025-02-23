# 1e32b0e9 • 018 • refine_coder

---
```python
"""
1.  **Identify Horizontal Lines:** Find two complete horizontal lines of the *same* color within the input grid. If less than 2 lines, exit and return input
2.  **Identify Unique Colors:** Except for the line color, identify unique colors within the grid that occur one or more times
3.  **Preserve:** The horizontal lines remain unchanged.
4.  **Extend Unique Colors:** The unique colors should persist from input to output.
5. **Fill:** For all colors that appear on the same line, extend pixels of that color using 4-connectivity (up, down, left, right) until encountering a boundary (edge of grid or a different color). The fill should not extend through diagonal connections. Do not extend colors across the complete preserved lines.
"""

import numpy as np

def get_horizontal_lines(grid):
    lines = []
    for row_index, row in enumerate(grid):
        first_pixel = row[0]
        if all(pixel == first_pixel for pixel in row) and first_pixel != 0:
            lines.append((row_index, first_pixel))
    return lines

def get_unique_color_pixels(grid, preserved_color):
    rows, cols = grid.shape
    color_counts = {}
    pixel_locations = {}

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if color != 0 and color != preserved_color:
                if color not in color_counts:
                    color_counts[color] = 0
                    pixel_locations[color] = []
                color_counts[color] += 1
                pixel_locations[color].append((r, c))

    unique_pixels = {}
    for color, count in color_counts.items():
       if count > 0: # Just get colors that exist
         unique_pixels[color] = pixel_locations[color]
    return unique_pixels

def fill(grid, start_row, start_col, color, preserved_rows):
    rows, cols = grid.shape
    queue = [(start_row, start_col)]

    while queue:
        r, c = queue.pop(0)

        if grid[r, c] == color or grid[r,c] == 0: # can only fill if we match or blank
          grid[r, c] = color # set

          neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
          for nr, nc in neighbors:
              if 0 <= nr < rows and 0 <= nc < cols: # In grid
                if nr not in preserved_rows: # not preserved
                  if grid[nr, nc] == 0:  # Fill
                    queue.append((nr, nc))

def transform(input_grid):
    # Initialize output grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = output_grid.shape

    # Preserve horizontal lines
    horizontal_lines = get_horizontal_lines(input_grid)
    if len(horizontal_lines) < 2:
        return input_grid

    preserved_row1, color1 = horizontal_lines[0]
    preserved_row2, color2 = horizontal_lines[1]

    # Ensure they are same
    if color1 != color2:
      return input_grid # Not a valid task

    preserved_color = color1
    preserved_rows = [preserved_row1, preserved_row2]

    # Preserve lines
    for c in range(cols):
      output_grid[preserved_row1, c] = preserved_color
      output_grid[preserved_row2, c] = preserved_color


    # Get Unique Pixels
    unique_color_pixels = get_unique_color_pixels(input_grid, preserved_color)

    # Preserve and Fill
    # Preserve unique color pixels, and Fill Rule
    for color, locations in unique_color_pixels.items():
        for r, c in locations:
            output_grid[r, c] = color # Preserve

            # Fill adjacent cells with same color
            fill(output_grid, r, c, color, preserved_rows)


    return output_grid
```
