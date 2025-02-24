"""
1.  **Identify** the red (2) pixels in the input grid.
2.  Change the color of the red pixel at the top right to blue (1).
3.  Change to blue(1) all white pixels (0) to the left.
4. **Identify** the red (2) pixel in the input grid that is at the bottom-left
5.  **Flood Fill:** Starting from the bottom red (2) pixel, change all directly adjacent or diagonally adjacent white (0) pixels to blue (1). Continue this expansion until no more directly or diagonally adjacent white pixels can be changed to blue.
6.  **Preserve:** The green (3) and azure (8) pixels remain unchanged in their original positions and colors.
"""

import numpy as np

def find_pixels_by_color(grid, color):
    return np.argwhere(grid == color)

def flood_fill(grid, start_row, start_col, target_color, replacement_color):
    rows, cols = grid.shape
    if grid[start_row, start_col] != target_color:
        return

    stack = [(start_row, start_col)]
    while stack:
        row, col = stack.pop()
        if grid[row, col] == target_color:
            grid[row, col] = replacement_color

            # Check adjacent and diagonal cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        stack.append((nr, nc))


def transform(input_grid):
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all red pixels
    red_pixels = find_pixels_by_color(input_grid, 2)

    # Find the top-rightmost red pixel
    if len(red_pixels) > 0:
        top_right_red = max(red_pixels, key=lambda item: (item[1], -item[0]))

      # change the color of top_right_red
        output_grid[top_right_red[0], top_right_red[1]] = 1

        # change to blue all white pixels to the left
        for c in range(top_right_red[1]-1, -1, -1):
          if output_grid[top_right_red[0],c] == 0:
            output_grid[top_right_red[0], c] = 1
          else:
             break # stop at first non-white

    #find other red pixel that is not the top_right
    for red_pixel in red_pixels:
        if not np.array_equal(red_pixel, top_right_red):

            # Flood fill from the other red pixel
            flood_fill(output_grid, red_pixel[0], red_pixel[1], 0, 1)

    return output_grid