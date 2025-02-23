# 2-0ca9ddb6 • 006 • example_3 - CODE

---
```python
"""
1.  **Preserve Isolated Pixels:** Any colored pixel in the input grid that has only white (0) neighbors (up, down, left, and right) is preserved in the output grid at the same location.

2.  **Introduce Yellow:** If a colored pixel exists at `(x,y)` and only has white neighbors:
    *   If the `y` value of the input is less than or equal to the `y` median, two new yellow pixels are created. The new pixels are created at `(x-1, y-1)` and `(x+1, y-1)`.

3. **Introduce Orange**: If a colored pixel exists at (x,y) and only has white neighbors:
    * If the 'y' value is greater that the median y:
    * A new orange pixel is placed at the location to above and to the left `(x-1, y-1)`
    * A new orange pixel is placed at the location below and to the left `(x-1, y+1)`
    * A new orange pixel is place at the location to the right `(x+1,y)`

The median value is calculated on the y coordinate of all colored pixels.
"""

import numpy as np

def get_colored_pixels(grid):
    pixels = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                pixels.append((x, y, grid[y, x]))
    return pixels

def get_neighbors(grid, x, y):
    neighbors = {}
    if y > 0:
        neighbors['up'] = grid[y-1, x]
    if y < grid.shape[0] - 1:
        neighbors['down'] = grid[y+1, x]
    if x > 0:
        neighbors['left'] = grid[y, x-1]
    if x < grid.shape[1] - 1:
        neighbors['right'] = grid[y, x+1]
    return neighbors

def calculate_y_median(pixels):
    y_values = [y for x, y, _ in pixels]
    if not y_values:  # Handle empty list case (no colored pixels)
        return 0
    return np.median(y_values)


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    colored_pixels = get_colored_pixels(input_grid)
    y_median = calculate_y_median(colored_pixels)

    # change output pixels
    for x, y, color in colored_pixels:
        neighbors = get_neighbors(input_grid, x, y)
        if all(value == 0 for value in neighbors.values()):
            # Preserve isolated pixels
            output_grid[y, x] = color

            # Introduce Yellow
            if y <= y_median:
                if x > 0 and y > 0:
                  output_grid[y - 1, x - 1] = 4
                if x < output_grid.shape[1] -1 and y > 0:
                  output_grid[y - 1, x + 1] = 4
            # Introduce Orange
            else:
              if x > 0 and y > 0:
                output_grid[y - 1, x - 1] = 7  # Up and left
              if x > 0 and y < output_grid.shape[0]-1:
                output_grid[y + 1, x - 1] = 7  # Down and left
              if x < output_grid.shape[1]-1:
                output_grid[y, x + 1] = 7      # Right


    return output_grid
```
