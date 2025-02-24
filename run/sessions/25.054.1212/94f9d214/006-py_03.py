"""
1.  **Identify Green and Blue Pixels:** Find all pixels that are green (value 3) and blue (value 1) in the input grid. Store their coordinates.
2.  **Determine the Bounding Box:** Find the smallest rectangle that contains all green and blue pixels. The top-left corner of this rectangle is defined by the minimum row and column indices of all green and blue pixels. The bottom-right corner is defined by the maximum row and column indices of all green and blue pixels.
3.  **Identify Red Pixel Locations:** Iterate through the green pixels. For each green pixel, check if a blue pixel exists immediately to its left, right, above, or below. If any of these conditions are true, mark the green pixel's location as a red pixel location.
4. **Create Bounding Box Grid.** Create a new grid using the dimensions calculated for the bounding box.
5.  **Populate Output Grid:** Within the new bounding box grid, set the pixels identified in step 3 to red (value 2). Fill all other pixels within the bounding box with white (value 0).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Green and Blue Pixels
    green_pixels = []
    blue_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 3:
                green_pixels.append((r, c))
            elif input_grid[r, c] == 1:
                blue_pixels.append((r, c))

    # 2. Determine the Bounding Box
    if not green_pixels and not blue_pixels:
        return [[0]]

    min_row = min(r for r, _ in green_pixels + blue_pixels)
    min_col = min(c for _, c in green_pixels + blue_pixels)
    max_row = max(r for r, _ in green_pixels + blue_pixels)
    max_col = max(c for _, c in green_pixels + blue_pixels)

    # 3. Identify Red Pixel Locations
    red_pixel_locations = []
    for r, c in green_pixels:
        # Check for adjacent blue pixels
        if (r - 1, c) in blue_pixels:  # Above
            red_pixel_locations.append((r, c))
        elif (r + 1, c) in blue_pixels:  # Below
            red_pixel_locations.append((r, c))
        elif (r, c - 1) in blue_pixels:  # Left
            red_pixel_locations.append((r, c))
        elif (r, c + 1) in blue_pixels:  # Right
            red_pixel_locations.append((r, c))

    # 4. Create Bounding Box Grid
    output_rows = max_row - min_row + 1
    output_cols = max_col - min_col + 1
    output_grid = np.zeros((output_rows, output_cols), dtype=int)

    # 5. Populate Output Grid
    for r, c in red_pixel_locations:
        output_grid[r - min_row, c - min_col] = 2

    return output_grid.tolist()