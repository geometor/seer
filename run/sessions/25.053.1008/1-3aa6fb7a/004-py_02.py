"""
1.  **Identify Contiguous Azure Regions:** Group connected azure (8) pixels into distinct regions.
2.  **Locate Edge Pixels:** Within each azure region, identify the "edge" pixels. An edge pixel is an azure pixel that is directly adjacent (up, down, left or right) to at least one non-azure pixel.
3.  **Determine Change Condition**: Check each identified edge pixel within each identified azure region.
4.  **Conditional Color Change**: Of the identified azure pixels, if the pixel is at on a specific "edge" or "end" of a connected block of azure pixels, change the pixel color from azure (8) to blue (1).
5.  **Preserve Other Pixels:** All other pixels (non-azure, and interior azure pixels) remain unchanged.
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

    # 1. Identify Contiguous Azure Regions using scipy.ndimage.label
    labeled_grid, num_regions = label(input_grid == 8)

    # 2. & 3. Locate Edge Pixels and Determine Change Condition
    for r in range(rows):
        for c in range(cols):
            if is_azure(r, c):
                # Check neighbors (up, down, left, right)
                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                is_edge = False
                for nr, nc in neighbors:
                    if not (0 <= nr < rows and 0 <= nc < cols and input_grid[nr, nc] == 8):
                        is_edge = True
                        break
                # 4. Conditional Color Change (only if it's an edge pixel)
                if is_edge:
                    # Determine the specific edge condition.  This part needs further refinement based on examples.
                    # For now, a simplified version is used, which will be improved upon iteration.
                    if (r > 0 and not is_azure(r - 1, c)) or \
                       (r < rows - 1 and not is_azure(r + 1, c)) or \
                       (c > 0 and not is_azure(r, c - 1) and is_azure(r-1,c-1)) or\
                       (c < cols - 1 and not is_azure(r, c + 1) and is_azure(r+1,c+1)):
                           output_grid[r,c] = 1


    # 5. Preserve Other Pixels (already handled by copying input_grid)
    return output_grid