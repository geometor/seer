"""
1.  **Copy Input:** Create a copy of the input grid as the output grid.
2.  **Preserve Top Rows:** The first two rows of the input grid remain unchanged in the output grid.
3.  **Iterate through Remaining Rows:** Starting from the third row (index 2), iterate through each subsequent row of the output grid.
4.  **Cyclic Replacement:** For each pixel in the current row:
    *   If the pixel value is 0 (white):
        *   Replace it with the corresponding value from the first row, using a cyclic index. The column index for the first row is calculated as `current_column_index % width_of_first_row`.
5.  **Repeat Replacement**: Repeat replacing 0 (white) with the cyclic index for the entire input grid.
6.  **Output:** Return the modified output grid.
"""

import numpy as np

def transform(input_grid):
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Preserve top two rows (already done by copying)

    # Iterate through remaining rows
    for i in range(2, rows):
        for j in range(cols):
            # Cyclic Replacement
            if output_grid[i, j] == 0:
                first_row_index = j % cols  # Cyclic index for the first row
                output_grid[i, j] = input_grid[0, first_row_index]

    return output_grid