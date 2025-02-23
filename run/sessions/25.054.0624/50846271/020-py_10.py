"""
1.  **Identify a "cross" shape:** Locate a contiguous region of red (2) pixels forming a cross shape. The cross is defined by a central red pixel, with four red pixels directly adjacent to it (above, below, left, and right).

2.  **Locate insertion points relative to cross:**
    *   **Point 1:** locate the position immediately to the left of the central red pixel of the cross
    *   **Point 2:** locate the postion immediately below the central red pixel of the cross.

3.  **perform insertion** insert an azure (8) pixel at each of the insertion points.

4.  **Copy all other pixels:** All pixels from the input that are not part of the modification defined above, are directly copied to the output.
"""

import numpy as np

def find_cross_center(grid):
    # Find all red pixels
    red_pixels = np.argwhere(grid == 2)

    for r, c in red_pixels:
        # Check for cross shape (adjacent red pixels)
        if (
            r > 0 and grid[r-1, c] == 2 and  # Above
            r < grid.shape[0] - 1 and grid[r+1, c] == 2 and  # Below
            c > 0 and grid[r, c-1] == 2 and  # Left
            c < grid.shape[1] - 1 and grid[r, c+1] == 2  # Right
        ):
            return r, c  # Return the center coordinates

    return None  # No cross found

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the center of the red cross
    cross_center = find_cross_center(input_grid)

    if cross_center:
        center_row, center_col = cross_center

        # Insert azure pixels
        output_grid[center_row, center_col - 1] = 8  # Left of center
        output_grid[center_row + 1, center_col] = 8  # Below center

    return output_grid