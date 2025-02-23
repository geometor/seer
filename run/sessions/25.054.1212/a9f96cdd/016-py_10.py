"""
1.  **Locate** the red pixel (value 2) in the input grid.
2.  **Remove** the red pixel from the output grid.
3.  **Conditional Azure/Orange Placement:**
    *   If the red pixel is *not* in the last row:
        *   Place an azure pixel (value 8) one row *below* and one column *to the left* of the red pixel's original position.
        *   Place an orange pixel (value 7) one row *below* and one column *to the right* of the red pixel's original position.
4.  **Conditional Green/Magenta Placement:**
    *  If the red pixel is *not* in the first row AND *not* in the first column:
        * Place a green pixel (value 3) one row *above* and one column *to the left* of the red pixel's original position.
    *  If the red pixel is *not* in the first row AND *not* in the last column:
       *   Place a magenta pixel (value 6) one row *above* and one column *to the right* of the red pixel's original position.
5. **Output Grid**: maintain original grid size and all white pixels that were not replaced.
"""

import numpy as np

def find_pixel_by_value(grid, value):
    # Find the coordinates of a pixel with a specific value.
    coords = np.where(grid == value)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return the first occurrence
    return None

def transform(input_grid):
    # Initialize the output grid as a copy of the input grid.
    output_grid = np.copy(input_grid)

    # Find the red pixel (value 2).
    red_pixel_coords = find_pixel_by_value(input_grid, 2)

    if red_pixel_coords:
        # Remove the red pixel.
        output_grid[red_pixel_coords] = 0

        # Conditional Azure/Orange Placement.
        if red_pixel_coords[0] < output_grid.shape[0] - 1:
            azure_coords = (red_pixel_coords[0] + 1, red_pixel_coords[1] - 1)
            orange_coords = (red_pixel_coords[0] + 1, red_pixel_coords[1] + 1)

            if 0 <= azure_coords[1] < output_grid.shape[1]:
                output_grid[azure_coords] = 8
            if 0 <= orange_coords[1] < output_grid.shape[1]:
                output_grid[orange_coords] = 7

        # Conditional Green/Magenta Placement
        if red_pixel_coords[0] > 0:
            if red_pixel_coords[1] > 0:
                green_coords = (red_pixel_coords[0] - 1, red_pixel_coords[1] -1)
                output_grid[green_coords] = 3
            if red_pixel_coords[1] < input_grid.shape[1] - 1:
                magenta_coords = (red_pixel_coords[0] - 1, red_pixel_coords[1] + 1)
                output_grid[magenta_coords] = 6

    return output_grid