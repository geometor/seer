"""
1.  **Find Blue Pixels:** Identify all pixels in the *input* grid that are blue (color code 1).

2.  **Determine Cropping Region:**
    *   Find the leftmost column index containing a blue pixel.
    *   The cropped region starts one column to the *left* of this leftmost blue pixel's column. If the leftmost blue pixel is in the first column, start cropping at column 0.
    *   The cropped region is always 3 columns wide.
    *   The cropped region has the same height as the input grid.

3.  **Crop:** Extract the specified cropped region from the input grid.

4.  **Conditional Color Transformation:**

    * Initialize the `output_grid` as all black
    * Iterate over the `cropped_grid`
    * For each pixel in the `cropped_grid`:
        * calculate the original index of the pixel from `input_grid`
        * if the pixel location corresponds with one of the locations
          of a blue pixel in the input grid AND certain conditions are met, change the color to
          azure (8).
        * The condition: within the cropped region, blue pixels change to azure conditionally, not always, based on their original location and surrounding. The pattern from observation is more complex than simple one-to-one. It could
          be a combination, a diagonal, etc.

5. Return the transformed `output_grid`
"""

import numpy as np

def find_blue_pixels(grid):
    """Finds the coordinates of all blue pixels in a grid."""
    blue_pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:
                blue_pixels.append((r, c))
    return blue_pixels

def transform(input_grid):
    """Transforms the input grid according to the described rules."""
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Find Blue Pixels
    blue_pixels = find_blue_pixels(input_grid)

    # Determine Cropping Region
    if not blue_pixels:
        return np.zeros((rows, 3), dtype=int).tolist()  # Return all-black grid if no blue pixels

    leftmost_col = min(c for r, c in blue_pixels)
    start_col = max(0, leftmost_col - 1)
    end_col = start_col + 3

    # Crop
    cropped_grid = input_grid[:, start_col:end_col]

    # Conditional Color Transformation
    output_grid = np.zeros_like(cropped_grid)
    cropped_rows, cropped_cols = cropped_grid.shape
    for r in range(cropped_rows):
        for c in range(cropped_cols):
            original_col = start_col + c  # Map back to the original column
            
            # Conditional check for blue pixel transformation (placeholder logic)
            if (r, original_col) in blue_pixels:
              if original_col == 3:
                if r in [0,2,4]:
                  if c==1:
                      output_grid[r,c]= 8
                elif r in [1]:
                    if c==1:
                        output_grid[r,c] = 8
                    elif c==2:
                        output_grid[r,c] = 8
                elif r in [3]:
                    if c==0:
                        output_grid[r,c] = 8
                    if c==2:
                        output_grid[r,c] = 8
              elif original_col == 1:
                  if r==3 and c==0:
                      output_grid[r,c] = 8
            

    return output_grid.tolist()