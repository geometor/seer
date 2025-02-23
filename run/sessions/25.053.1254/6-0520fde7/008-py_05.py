"""
1. **Identify the Vertical Gray Stripe:** Find the vertical column in the input grid where all pixels are gray (color value 5).
2. **Extract a 3-column Region:** Create a region that includes the gray stripe and one column to its left and one column to its right.  The region must contain all the rows of the original grid
3. **Create Output.** Create an empty output of the same dimensions as the extracted region.
4. **Recolor the Output:**
    *   If a pixel in the extracted region is gray (5), the corresponding pixel in the output grid becomes red (2).
    *   If a pixel in the extracted region is white (0) or blue (1), the corresponding pixel in the output grid becomes white (0).
"""

import numpy as np

def find_gray_stripe_center(input_grid):
    # Find the column index where the gray (value 5) pixels are located.
    for j in range(input_grid.shape[1]):
        if np.all(input_grid[:, j] == 5):
            return j
    return -1  # Return -1 if no gray stripe is found


def transform(input_grid):
    """
    Extracts a 3-column region from the input grid centered on a vertical gray stripe and recolors it.
    """
    input_grid = np.array(input_grid)
    center_col = find_gray_stripe_center(input_grid)
    
    if center_col == -1:
        return None # No gray stripe found

    # Define the 3-column region
    start_row = 0
    end_row = input_grid.shape[0]
    start_col = max(0, center_col - 1) # Ensure start_col is within bounds
    end_col = min(input_grid.shape[1], center_col + 2) # Ensure end_col is within bounds

    # Extract the region
    region = input_grid[start_row:end_row, start_col:end_col]
    
    # Create output grid
    output_grid = np.zeros_like(region)
    
    # recolor output based on input region
    for i in range(region.shape[0]):
        for j in range(region.shape[1]):
            if region[i,j] == 5:
                output_grid[i,j] = 2  # Gray becomes red
            elif region[i, j] == 0 or region[i,j] == 1:
                output_grid[i,j] = 0 # White or blue becomes white

    return output_grid.tolist()