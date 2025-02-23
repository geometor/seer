"""
1. **Find Blue Regions:** Identify all distinct, connected regions of blue (1) pixels in the input grid.  These are our `blue_region` objects.
2. **Find Inner Region 1 (Orange Boundary):** Within each `blue_region`, locate all blue pixels that are directly adjacent (up, down, left, or right) to a white (0) pixel. These pixels form `inner_region_1`.
3. **Find Inner Region 2 (Red Interior):** Within each `blue_region`, identify all pixels that belong to the `blue_region` but are *not* part of `inner_region_1`. These pixels form `inner_region_2`. It is the area remaining after identifying `inner_region_1`, and could include originally white or blue pixels.
4. **Color Inner Region 1:** Change the color of all pixels in `inner_region_1` to orange (7).
5. **Color Inner Region 2:** Change the color of all pixels in `inner_region_2` to red (2).
6. **Preserve Other Colors:**  All pixels that are not part of any `blue_region` should remain their original color.
"""

import numpy as np
from scipy.ndimage import label

def get_neighbors(grid, r, c):
    """Gets the valid neighbors of a cell in a grid (up, down, left, right)."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors

def find_regions(grid, color):
    """Finds contiguous regions of a specific color in the grid."""
    mask = (grid == color)
    labeled_array, num_features = label(mask)
    return labeled_array, num_features

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape

    # 1. Find Blue Regions
    blue_regions, num_blue_regions = find_regions(input_grid, 1)

    # Iterate through each blue region
    for region_id in range(1, num_blue_regions + 1):
        inner_region_1 = []
        inner_region_2 = []
        
        # Create a mask for the current blue region.
        current_blue_region_mask = (blue_regions == region_id)

        # 2. Identify Inner Region 1 (adjacent to white pixels)
        for r in range(rows):
            for c in range(cols):
                if current_blue_region_mask[r,c]:
                    neighbors = get_neighbors(input_grid, r, c)  # Use 4-connectivity
                    for nr, nc in neighbors:
                        if input_grid[nr, nc] == 0:
                            inner_region_1.append((r, c))
                            break

        #create a mask for inner region 1
        inner_region_1_mask = np.zeros_like(input_grid, dtype=bool)
        for r, c in inner_region_1:
            inner_region_1_mask[r,c] = True

        # 3. Identify inner region 2 (remaining pixels inside blue region)
        for r in range(rows):
            for c in range(cols):
                if current_blue_region_mask[r,c] and not inner_region_1_mask[r,c]:
                    inner_region_2.append((r,c))

        # 4. & 5. Color Changes
        for r, c in inner_region_1:
            output_grid[r, c] = 7  # Orange

        for r,c in inner_region_2:
            output_grid[r,c] = 2 #Red


    return output_grid