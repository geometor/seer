"""
1.  **Identify Azure Regions:** Identify all contiguous regions of azure (8) pixels.
2.  **Identify Edge Pixels:** Within each azure region, identify the "edge" pixels. An edge pixel is an azure pixel directly adjacent (up, down, left, or right) to at least one non-azure pixel.
3.  **Conditional Color Change:** For *each* identified edge pixel:
    *   If the edge pixel is adjacent to a non-azure pixel *above* it, change the azure pixel to blue (1).
    *   If the edge pixel is adjacent to a non-azure pixel to its *left*, change the azure pixel to blue (1).
4.  **Preserve Other Pixels:** All other pixels (non-azure pixels, and azure pixels that do not meet the above condition) remain unchanged.
"""

import numpy as np
from scipy.ndimage import label

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Helper function to check if a pixel is azure
    def is_azure(r, c):
        return 0 <= r < rows and 0 <= c < cols and input_grid[r, c] == 8

    # 1. Identify Contiguous Azure Regions (not strictly needed for this refined logic, but kept for potential future use)
    labeled_grid, num_regions = label(input_grid == 8)

    # 2. & 3. Iterate through all pixels, checking for azure and edge conditions
    for r in range(rows):
        for c in range(cols):
            if is_azure(r, c):
                # Check if there's a non-azure pixel above
                if r > 0 and input_grid[r - 1, c] != 8:
                    output_grid[r, c] = 1
                # Check if there's a non-azure pixel to the left
                elif c > 0 and input_grid[r, c - 1] != 8:
                    output_grid[r, c] = 1

    # 4. Preserve Other Pixels (already handled by copying input_grid)
    return output_grid