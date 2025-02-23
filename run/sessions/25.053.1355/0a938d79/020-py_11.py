"""
1.  **Identify Colored Pixels:** Find all pixels in the input grid that are not white (value is not 0).
2.  **Horizontal Fill:** For each colored pixel, fill its entire row in the output grid with that pixel's color.
3.  **Interleaved Vertical Fill:**
     * Consider all the colored input rows identified
     * For each row of the output grid, the row is filled with the color that corresponds to the input row with colored object at an index based on simple modular arithmetic of the output row.
"""

import numpy as np

def get_colored_rows(grid):
    """Finds the row indices and colors of rows with non-white pixels."""
    colored_rows = []
    for row_idx, row in enumerate(grid):
        for pixel in row:
            if pixel != 0:
                colored_rows.append((row_idx, pixel))  # Store row index and the first non-zero color
                break  # Move to the next row once a colored pixel is found
    return colored_rows

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Find colored rows and their first non-zero colors
    colored_rows = get_colored_rows(input_grid)
    num_colored_rows = len(colored_rows)

    # Horizontal and Interleaved Vertical Fill
    for row_idx in range(output_grid.shape[0]):
      # use mod operator to pick color
      if (num_colored_rows > 0):
        source_row_idx, color = colored_rows[row_idx % num_colored_rows]
        output_grid[row_idx, :] = color

    
    return output_grid