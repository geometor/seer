"""
The transformation rule is: Extract a subgrid around a specific color object.

- If the object of color 1 (blue) exists and is unique:
    Extract the 3x3 subgrid centered around the blue object.
    Pad with background color 4 (yellow) if necessary to ensure a 3x3 output.
- Else, if the object of color 8 (azure) exists and is unique:
    Extract the 5x5 subgrid centered around the azure object.
    Pad with background color 3 (green) if necessary to ensure a 5x5 output.
- Else, if the object of color 8 (azure) and 4 (yellow) exists on the border corners of the input:
    Extract the 2x2 bottom-left corner of the input grid.
- Otherwise, return the original input grid.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts a subgrid based on the presence and uniqueness of specific colored objects.
    Prioritizes blue (color 1), then azure (color 8), and finally the bottom-left corner.
    """
    input_array = np.array(input_grid)

    # Check for unique blue object (color 1)
    blue_coords = np.argwhere(input_array == 1)
    if len(blue_coords) == 1:
        row, col = blue_coords[0]
        min_row = max(0, row - 1)
        max_row = min(input_array.shape[0], row + 2)
        min_col = max(0, col - 1)
        max_col = min(input_array.shape[1], col + 2)
        output_grid = input_array[min_row:max_row, min_col:max_col]

        rows, cols = output_grid.shape
        background_color = 4  # yellow background
        if rows < 3:
            pad_rows = 3 - rows
            pad_before = pad_rows // 2
            pad_after = pad_rows - pad_before
            output_grid = np.pad(output_grid, ((pad_before, pad_after), (0, 0)), mode='constant', constant_values=background_color)
        if cols < 3:
            pad_cols = 3 - cols
            pad_before = pad_cols // 2
            pad_after = pad_cols - pad_before
            output_grid = np.pad(output_grid, ((0, 0), (pad_before, pad_after)), mode='constant', constant_values=background_color)
        return output_grid.tolist()

    # Check for unique azure object (color 8)
    azure_coords = np.argwhere(input_array == 8)
    if len(azure_coords) == 1:
        row, col = azure_coords[0]
        min_row = max(0, row - 2)
        max_row = min(input_array.shape[0], row + 3)
        min_col = max(0, col - 2)
        max_col = min(input_array.shape[1], col + 3)
        output_grid = input_array[min_row:max_row, min_col:max_col]

        rows, cols = output_grid.shape
        background_color = 3  # green background
        if rows < 5:
            pad_rows = 5 - rows
            pad_before = pad_rows // 2
            pad_after = pad_rows - pad_before
            output_grid = np.pad(output_grid, ((pad_before, pad_after), (0, 0)), mode='constant', constant_values=background_color)
        if cols < 5:
            pad_cols = 5 - cols
            pad_before = pad_cols // 2
            pad_after = pad_cols - pad_before
            output_grid = np.pad(output_grid, ((0, 0), (pad_before, pad_after)), mode='constant', constant_values=background_color)

        return output_grid.tolist()
    
    # Check for 2x2 bottom-left corner condition
    rows, cols = input_array.shape
    if rows >= 2 and cols >= 2:
        bottom_left_corner = input_array[rows-2:rows, 0:2]
        unique_colors = np.unique(bottom_left_corner)
        if set(unique_colors).issubset({4, 8}):
            return bottom_left_corner.tolist()


    return input_array.tolist()