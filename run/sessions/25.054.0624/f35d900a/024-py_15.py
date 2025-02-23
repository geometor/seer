"""
1.  **Identify Single Pixels:** Examine the input grid to find all pixels that meet these criteria:
    *   The pixel's color is not white (0).
    *   The pixel is surrounded by white pixels (0) or the boundaries of the grid. These are considered "single pixels."

2.  **Expand to 3x3 Squares:** For each "single pixel" found:
    *   In the output grid, create a 3x3 square centered on the same location as the original single pixel.
    *   All pixels within this 3x3 square should have the same color as the original single pixel.

3.  **Connect with Gray Lines:** Identify pairs of single pixels in the *input grid* that are aligned either horizontally or vertically. For each such pair:
    *   In the *output* grid, draw a line of gray (5) pixels connecting the *edges* of their corresponding 3x3 squares.
    *   Start the gray line from the pixel adjacent to the position of the original single pixel.
    *   The gray line should only occupy cells that directly connect the two squares in a straight line (horizontal or vertical).
    *   The gray line consists of single gray pixels placed such that they maintain an alternating pattern, starting immediately adjacent to the original single pixel's location, and ending adjacent to the corresponding pixel of the other single pixel.
"""

import numpy as np

def find_single_pixels(grid):
    # Find single pixels of non-white color
    single_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                is_single = True
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i != 0 or j != 0) and 0 <= r + i < rows and 0 <= c + j < cols:
                            if grid[r + i, c + j] != 0:
                                is_single = False
                                break
                    if not is_single:
                        break
                if is_single:
                    single_pixels.append((r, c, grid[r, c]))
    return single_pixels

def expand_to_square(grid, r, c, color):
    # Expand a single pixel to a 3x3 square
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= r + i < grid.shape[0] and 0 <= c + j < grid.shape[1]:
                grid[r + i, c + j] = color

def connect_with_gray_lines(output_grid, input_pixel1, input_pixel2):
    # Connect two 3x3 squares with gray lines based on original input pixel positions
    r1, c1, color1 = input_pixel1
    r2, c2, color2 = input_pixel2

    if r1 == r2:  # Horizontal connection
        start_col = min(c1, c2)
        end_col = max(c1, c2)
        for c in range(start_col + 1, end_col):
            if (c - c1) % 2 == 1 and (c - c2) % 2 == 1 :

                output_grid[r1, c] = 5

    elif c1 == c2:  # Vertical connection
        start_row = min(r1, r2)
        end_row = max(r1, r2)
        for r in range(start_row + 1, end_row):
            if (r - r1) % 2 == 1 and (r-r2) % 2 == 1:
                output_grid[r, c1] = 5


def transform(input_grid):
    # Initialize output_grid as an all-zero grid of the same size as the input
    output_grid = np.zeros_like(input_grid)

    # 1. Find single pixels in the input grid
    input_single_pixels = find_single_pixels(input_grid)

    # 2. Expand single pixels to 3x3 squares in the output grid
    for r, c, color in input_single_pixels:
        expand_to_square(output_grid, r, c, color)

    # 3. Connect squares with gray lines based on input single pixel positions
    for i in range(len(input_single_pixels)):
        for j in range(i + 1, len(input_single_pixels)):
            # Check for horizontal or vertical alignment in the input grid
            if input_single_pixels[i][0] == input_single_pixels[j][0] or \
               input_single_pixels[i][1] == input_single_pixels[j][1]:
                connect_with_gray_lines(output_grid, input_single_pixels[i], input_single_pixels[j])

    return output_grid