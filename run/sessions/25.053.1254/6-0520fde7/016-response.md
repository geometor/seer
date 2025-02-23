# 6-0520fde7 • 016 • refine_coder

---
```python
"""
1.  **Locate the Separator:** Find the vertical line composed entirely of gray (5) pixels within the input grid. Note its x-coordinate. This line acts as a separator.

2.  **Extract Adjacent Pixels:** For each row in the input grid:
    *   Identify the pixel immediately to the left of the gray separator line.
    *   Identify the pixel immediately to the right of the gray separator line.

3.  **Construct Output Grid:** Create a new output grid with the same height as the input grid and a width of 3 columns.

4.  **Populate Output Rows:** For each row:
    *   **Left Column:** If a pixel was found to the *left* of the separator in the input grid, place its translated value in the first column of the output grid, otherwise the value should be 0.
        *   If the extracted pixel's value is 1 (blue), the translated value is 2 (red).
        *   If the extracted pixel's value is not 0, the translated value is 0.

    *   **Center Column:** The second (center) column of the output grid is always 0.

    *   **Right Column:** If a pixel was found to the *right* of the separator in the input grid, place its translated value in the third column of the output, otherwise the value should be 0.
        * If the extracted pixel is 1 (blue) the value should be 2 (red)
        * If the extracted pixel's value is not 0, the translated value is 0.

5. **Final Output:** Return output grid.
"""

import numpy as np

def find_vertical_line(grid, color):
    """Finds the x-coordinate of a vertical line of the specified color."""
    height, width = grid.shape
    for x in range(width):
        is_line = True
        for y in range(height):
            if grid[y, x] != color:
                is_line = False
                break
        if is_line:
            return x
    return -1  # Return -1 if no line is found

def translate_pixel(value):
    """Translates a pixel value according to the rules."""
    if value == 1:
        return 2
    elif value != 0:
        return 0
    else:
        return 0

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    height, width = input_grid.shape
    output_grid = np.zeros((height, 3), dtype=int)

    # Find the vertical line of gray (5) pixels
    center_x = find_vertical_line(input_grid, 5)

    # Extract the columns to the left and right of the center and construct output
    if center_x != -1:
        for y in range(height):
            # Get pixel to the left, if it exists
            if center_x > 0 :
                left_pixel = input_grid[y, center_x - 1]
                output_grid[y, 0] = translate_pixel(left_pixel)

            # Center column of output is always 0
            output_grid[y,1] = 0

            # Get pixel to the right, if it exists
            if center_x < width - 1:
                right_pixel = input_grid[y, center_x + 1]
                output_grid[y, 2] = translate_pixel(right_pixel)


    return output_grid.tolist()
```
