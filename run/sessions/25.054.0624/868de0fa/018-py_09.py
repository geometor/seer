"""
1.  **Identify Blue Regions:** Find all distinct, connected regions of blue (1) pixels. These are the `blue_region` objects.
2.  **Identify the Boundary:** Find all white pixels(0) which are adjacent to the `blue_region`.
3. **Define Inner Region 1 (Orange):** For each `blue_region`, identify the blue pixels which are adjacent to the `boundary`. These constitute `inner_region_1`.
4.  **Define Inner Region 2 (Red):** For each `blue_region`, the remaining blue pixels *not* in `inner_region_1` constitute `inner_region_2`.
5.  **Color Inner Region 1:** Change the color of all pixels in `inner_region_1` to orange (7).
6.  **Color Inner Region 2:** Change the color of all pixels in `inner_region_2` to red (2).
7.  **Preserve Other Colors:** All pixels not part of any `blue_region` keep their original color.
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
        # Create a mask for the current blue region.
        current_blue_region_mask = (blue_regions == region_id)
        
        # 2. Identify Boundary (white pixels adjacent to blue region)
        boundary = []
        for r in range(rows):
            for c in range(cols):
                if input_grid[r,c] == 0: #white pixel
                    neighbors = get_neighbors(input_grid, r, c)
                    for nr, nc in neighbors:
                        if current_blue_region_mask[nr,nc]: #if neighbor is in the current blue region
                            boundary.append((r,c))
                            break

        # 3. Define Inner Region 1
        inner_region_1 = []
        for r in range(rows):
            for c in range(cols):
                if current_blue_region_mask[r, c]: #if current pixel in blue region
                    neighbors = get_neighbors(input_grid, r, c)
                    for nr, nc in neighbors:
                        if (nr, nc) in boundary: #if a neighbor is in the boundary
                            inner_region_1.append((r,c))
                            break

        # 4. Define Inner Region 2 (remaining blue pixels)
        inner_region_2 = []
        inner_region_1_coords = set(inner_region_1)
        for r in range(rows):
            for c in range(cols):
                if current_blue_region_mask[r, c] and (r, c) not in inner_region_1_coords:
                    inner_region_2.append((r, c))

        # 5. & 6. Color the regions
        for r, c in inner_region_1:
            output_grid[r, c] = 7  # Orange

        for r, c in inner_region_2:
            output_grid[r, c] = 2  # Red

    return output_grid