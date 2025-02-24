"""
1.  **Consolidate Colors:** All non-zero colored pixels in the input grid are treated as a single color group (conceptually, "colored").

2.  **Determine Color Extent:** Find the minimum and maximum row and column indices of the "colored" pixels in the input grid.  This defines the overall area where color is present.

3.  **Divide into Quadrants (Implicitly):** The key insight here is that the input grid is *not* divided into fixed 4x4 quadrants.  Instead, we're interested in whether color exists *anywhere* within regions relative to the overall color extent.  We implicitly divide the *colored area* into quadrants based on its bounding box.

4.  **Presence Mapping (4x4 Output):** Create a 4x4 output grid initialized with all zeros (white). For each cell in the 4x4 output, determine if any "colored" pixels exist in the corresponding quadrant of the input's *colored area*. If color is present in that quadrant, set the output cell to green (3); otherwise, leave it as white (0). "Corresponding Quadrant" means dividing input rows/cols by (color extent height/4) and (color extent width/4), not by fixed amounts.
   - Divide input_height / 4 = quadrant_height_scale.
   - Divide input_width / 4 = quadrant_width_scale.
   - input cell row, col maps to output[row // quadrant_height_scale, col // quadrant_width_scale]

5. **Output:** The resulting 4x4 grid represents the presence of color in the input, compressed into a 4x4 representation.
"""

import numpy as np

def get_color_extents(grid):
    """
    Finds the bounding box for non-zero colors in the grid.

    Returns:
        A dictionary where keys are colors and values are (min_row, max_row, min_col, max_col) tuples.
        Returns an empty dictionary if no non-zero colors are found.
    """
    color_extents = {}
    rows, cols = np.where(grid != 0)
    if len(rows) > 0:
        min_row, max_row = np.min(rows), np.max(rows)
        min_col, max_col = np.min(cols), np.max(cols)
        color_extents[1] = (min_row, max_row, min_col, max_col) #color is essentially irrelevant
    return color_extents

def transform(input_grid):
    # Initialize the output grid as a 4x4 array filled with 0s (white).
    output_grid = np.zeros((4, 4), dtype=int)

    # Determine the extent of colored pixels in the input.
    color_extents = get_color_extents(input_grid)

    if not color_extents:  # Handle cases where there are no colored pixels
        return output_grid

    min_row, max_row, min_col, max_col = color_extents[1]
    
    # Calculate scaling factors for quadrant mapping.
    height_scale = (max_row - min_row + 1) / 4
    width_scale = (max_col - min_col + 1) / 4
    
    # Iterate through colored area to find the output
    for i in range(min_row, max_row+1):
        for j in range(min_col, max_col+1):
            if input_grid[i,j] != 0:
                out_row = int((i - min_row) / height_scale) if height_scale >0 else 0
                out_col = int((j - min_col) / width_scale) if width_scale > 0 else 0
                
                output_grid[out_row, out_col] = 3

    return output_grid