"""
The transformation rule is: Extract the 5x5 subgrid centered around the azure object.
If there is no azure object, return the original grid. If there is more than one azure
object, return the original grid. Pad with background color 3 (green), to get a 5x5
grid, if the azure object is near the border.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the 5x5 subgrid centered on the azure (color 8) object.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Find the coordinates of the azure pixel (color 8).
    azure_coords = np.argwhere(input_array == 8)
    
    #There is no azure object
    if len(azure_coords) == 0:
        return input_array.tolist()

    # Ensure there's only one azure pixel.  If not, return original.
    if len(azure_coords) > 1:
        return input_array.tolist()

    row, col = azure_coords[0]

    # Extract the 5x5 subgrid centered on the azure pixel.
    # Handle edge cases where the azure pixel is near the boundary.
    min_row = max(0, row - 2)
    max_row = min(input_array.shape[0], row + 3)
    min_col = max(0, col - 2)
    max_col = min(input_array.shape[1], col + 3)

    output_grid = input_array[min_row:max_row, min_col:max_col]
    
    # Ensure output grid will be 5x5 padding with background color if needed
    rows, cols = output_grid.shape
    
    background_color = 3 # green background
    
    if rows < 5:
        pad_rows = 5-rows
        pad_before = pad_rows // 2
        pad_after = pad_rows-pad_before
        
        output_grid = np.pad(output_grid, 
                             ((pad_before,pad_after),(0,0)),
                             mode='constant', constant_values=background_color)
    if cols < 5:
        pad_cols = 5-cols
        pad_before = pad_cols // 2
        pad_after = pad_cols-pad_before
        
        output_grid = np.pad(output_grid, 
                             ((0,0), (pad_before,pad_after)),
                             mode='constant', constant_values=background_color)

    return output_grid.tolist()