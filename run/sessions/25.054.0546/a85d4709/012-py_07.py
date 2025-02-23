"""
The output grid is constructed row by row based on the position of gray pixels.

1. Iterate through each row of the input grid.
2. For each row, check the position of the gray (value 5) pixel.
3. Based on the gray pixel's column in the input grid, fill the corresponding output grid's row:
   - If the gray pixel is in the first column of the input row, fill the entire output row with red (value 2).
   - If the gray pixel is in the second column of the input row, fill the entire output row with yellow (value 4).
   - If the gray pixel is in the third column of the input row, fill the entire output row with green (value 3).
   - If no gray pixel is in the row, skip
4. Return output grid
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the column position of gray pixels (value 5) within each row.

    Args:
        input_grid (list of lists): A 2D array representing the input grid.

    Returns:
        list of lists: A 2D array representing the transformed grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)  # Initialize with zeros

    for row_index, row in enumerate(input_grid):
        # Find the column index of the gray pixel (value 5) in the current row
        gray_column_indices = np.where(row == 5)[0]

        if gray_column_indices.size > 0:
            # use first gray, if multiple
            gray_column_index = gray_column_indices[0]

            # Determine the output value based on the column index
            if gray_column_index == 0:
                output_value = 2  # Red
            elif gray_column_index == 1:
                output_value = 4  # Yellow
            elif gray_column_index == 2:
                output_value = 3  # Green
            else:
                # this condition should not happen
                continue

            # Fill the entire output row with the determined value
            output_grid[row_index, :] = output_value

    return output_grid.tolist()