"""
Preserves two complete horizontal lines of a single color, copies any unique colored pixels to their original location and fills adjacent areas of unique color pixels of the same color, except for preserved lines.
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

def transform(input_grid):
    # Initialize output grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Preserve horizontal lines
    horizontal_lines = get_horizontal_lines(input_grid)
    if len(horizontal_lines) == 2:
        preserved_row1, color1 = horizontal_lines[0]
        preserved_row2, color2 = horizontal_lines[1]

        # Ensure they are same
        if color1 != color2:
          return input_grid # Not a valid task

        preserved_color = color1

        # if they aren't the same color - return input, since this isn't
        # something our algorithm will handle

        for c in range(cols):
          output_grid[preserved_row1, c] = preserved_color
          output_grid[preserved_row2, c] = preserved_color
    else:
        return input_grid # Not a valid task

    # Get Unique Pixels
    unique_color_pixels = get_unique_color_pixels(input_grid, preserved_color)

    # Preserve unique color pixels, and Fill Rule
    for color, locations in unique_color_pixels.items():
        for r, c in locations:
            output_grid[r, c] = color # Preserve

            # Fill adjacent cells with same color
            neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neighbors:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if nr != preserved_row1 and nr != preserved_row2:
                      if output_grid[nr, nc] == 0:
                        output_grid[nr, nc] = color

    return output_grid