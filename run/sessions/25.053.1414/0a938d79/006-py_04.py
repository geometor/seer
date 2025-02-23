"""
1.  **Identify Source Rows:** Iterate through each row of the input grid. A row is considered a "source row" if it contains at least one non-zero (non-white) pixel.

2.  **Replicate Horizontally (Corrected):** For each source row, replicate its pattern. For each non-zero pixel, copy its value to all pixels to its right until another non-zero pixel is encountered. Repeat this process to the end of the line.

3.  **Stack and Repeat:** Create the output grid by stacking the replicated source rows. Repeat the entire set of replicated source rows until the output grid has the same number of rows as the input grid. Empty rows in the input that do not contain any colored pixels result in blank/all-zero rows in the output.
"""

import numpy as np

def _find_source_rows(grid):
    """Identifies and returns a list of row indices that contain at least one non-zero pixel."""
    source_rows = []
    for i, row in enumerate(grid):
        if any(pixel != 0 for pixel in row):
            source_rows.append(i)
    return source_rows

def _replicate_row_horizontally(row):
    """Replicates the non-zero pixels of a row across the row, maintaining pattern."""
    new_row = [0] * len(row)
    last_non_zero = 0
    for i, pixel in enumerate(row):
        if pixel != 0:
            last_non_zero = pixel
        if last_non_zero != 0:
          new_row[i] = last_non_zero
    return new_row

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Find source rows
    source_row_indices = _find_source_rows(input_grid)
    replicated_rows = []

    # Replicate source rows horizontally
    for y in source_row_indices:
      replicated_rows.append(_replicate_row_horizontally(input_grid[y,:]))

    # Stack and repeat
    num_replicated_rows = len(replicated_rows)

    if num_replicated_rows > 0:
        for y in range(output_grid.shape[0]):
          output_grid[y,:] = replicated_rows[y % num_replicated_rows]
    
    return output_grid.tolist()