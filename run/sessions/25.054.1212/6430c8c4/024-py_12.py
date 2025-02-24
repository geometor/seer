"""
1.  **Find Divider:** Locate the horizontal line of yellow (4) pixels in the input grid.
2.  **Separate Regions:** Define the "upper region" as the area above the divider and the "lower region" as the area at and below the divider.
3.  **Determine Output Size:** The dimensions of the output grid are the same as the dimensions of the *upper region*.
4.  **Initialize Output:** Create an output grid filled with white (0) pixels, with the size determined in the previous step.
5.  **Mirror Orange Pixels:** Iterate through each pixel in the *upper region*.
    *   If a pixel is orange (7):
        *   Swap its row and column indices (i, j) to get the mirrored position (j, i).
        *   If the mirrored position is within the bounds of the *upper region*, set the pixel at the mirrored position in the *output grid* to green (3).
6.  **Ignore Other Pixels:**  Pixels in the upper region that are not orange (7) are not explicitly processed; they remain white (0) in the output because of initialization. The lower region does not affect the output.
7.  **Output:** Return the output grid.
"""

import numpy as np

def find_horizontal_line(grid, color):
    """Finds the row index of a horizontal line of a given color."""
    for i, row in enumerate(grid):
        if all(pixel == color for pixel in row):
            return i
    return -1  # Not found

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    input_grid = np.array(input_grid)

    # 1. Find Divider
    yellow_line_row = find_horizontal_line(input_grid, 4)

    # 2. Separate Regions
    upper_region = input_grid[:yellow_line_row]

    # 3. Determine Output Size
    output_height, output_width = upper_region.shape

    # 4. Initialize Output
    output_grid = np.zeros((output_height, output_width), dtype=int)

    # 5. Mirror Orange Pixels
    for i in range(output_height):
        for j in range(output_width):
            if upper_region[i, j] == 7:  # Only mirror orange pixels
                mirrored_i, mirrored_j = j, i
                if mirrored_i < output_height and mirrored_j < output_width:  # Boundary Check
                    output_grid[mirrored_i, mirrored_j] = 3  # Set to green

    # 6. Ignore Other Pixels - handled by initialization

    # 7. Output
    return output_grid.tolist()