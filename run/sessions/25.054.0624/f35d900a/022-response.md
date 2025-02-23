# f35d900a • 022 • refine_coder

---
```python
"""
1.  **Identify Single Pixels:** Find all pixels in the input grid that have a color other than white (0) and are surrounded by white pixels (0) or the grid boundary. These are the "single pixels."
2.  **Expand to 3x3 Squares:** For each identified single pixel, create a 3x3 square of the same color centered on the original pixel's location in the output grid.
3.  **Connect with Gray Lines:** For every pair of single pixels in the *input grid* that are aligned either horizontally or vertically, draw a line of gray (5) pixels between their corresponding 3x3 squares in the output grid.
    *   The connecting gray line is placed in the output grid such that gray pixels replace output pixels that are on the same row or column as the original single input pixels, and the alternating gray pattern starts from the single pixel position.
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
        for c in range(start_col+1, end_col):
            if (c - start_col) % 2 == 1:
                output_grid[r1, c] = 5

    elif c1 == c2:  # Vertical connection
        start_row = min(r1, r2)
        end_row = max(r1, r2)

        for r in range(start_row + 1, end_row):

            if (r - start_row) % 2 == 1:
                output_grid[r, c1] = 5


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

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
```

