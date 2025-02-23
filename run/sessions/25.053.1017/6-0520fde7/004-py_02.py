"""
The transformation rule is as follows:
1.  **Identify Key Column:** Locate the vertical column in the input grid where all pixels are gray (5).
2.  **Extract Adjacent Columns:** Consider the columns immediately to the left and right of the key gray column.
3.  **Create Output Grid:** Create a new 3x3 grid.
4. **Populate White:** Populate the output grid with white pixels, everywhere
5. **Translate and Transform Pixels**: If, in the columns extracted, a pixel is blue(1), then a red(2) pixel occupies that index in the output.
6. Ignore the gray column, and other input data, it is used to establish the columns to transform, but has not other data related to the transformation.
"""

import numpy as np

def find_gray_column(grid):
    # Find the column index where all elements are gray (5)
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == 5):
            return j
    return -1  # Return -1 if no such column is found

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    # Convert input_grid to numpy array for easier manipulation
    input_grid = np.array(input_grid)

    # 1. Identify Key Column
    gray_column_index = find_gray_column(input_grid)

    # If no gray column is found, return a 3x3 white grid
    if gray_column_index == -1:
          return np.zeros((3, 3), dtype=int)

    # 2. Extract Adjacent Columns
    left_column_index = max(0, gray_column_index - 1)
    right_column_index = min(input_grid.shape[1] - 1, gray_column_index + 1)
    
    # 3. Create Output Grid (3x3, initialized with white)
    output_grid = np.zeros((3, 3), dtype=int)

    # 4 & 5 Translate and Transform
    for i in range(3):
        if i < input_grid.shape[0]: #make sure within dims
            if input_grid[i, left_column_index] == 1:
                output_grid[i, 0] = 2
            if input_grid[i, right_column_index] == 1:
                output_grid[i, 2] = 2

    return output_grid