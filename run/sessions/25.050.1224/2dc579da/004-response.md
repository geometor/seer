# 2dc579da • 004 • example_2 - CODE

---
```python
"""
The transformation rule is: Extract the 3x3 subgrid centered around the blue object.
If there is no blue object, return the original grid. If there is more than one blue
object, return the original grid. Pad with background color 4 (yellow), to get a 3x3
grid, if the blue object is near the border.
"""

import numpy as np

def transform(input_grid):
    """
    Extracts the 3x3 subgrid centered on the blue (color 1) object.
    """
    # Convert the input grid to a NumPy array.
    input_array = np.array(input_grid)

    # Find the coordinates of the blue pixel (color 1).
    blue_coords = np.argwhere(input_array == 1)
    
    #There is no blue object
    if len(blue_coords) == 0:
        return input_array.tolist()

    # Ensure there's only one blue pixel.  If not, return original.
    if len(blue_coords) > 1:
        return input_array.tolist()

    row, col = blue_coords[0]

    # Extract the 3x3 subgrid centered on the blue pixel.
    # Handle edge cases where the blue pixel is near the boundary.
    min_row = max(0, row - 1)
    max_row = min(input_array.shape[0], row + 2)
    min_col = max(0, col - 1)
    max_col = min(input_array.shape[1], col + 2)

    output_grid = input_array[min_row:max_row, min_col:max_col]
    
    # Ensure output grid will be 3x3 padding with background color if needed
    rows, cols = output_grid.shape
    
    background_color = 4 # yellow background
    
    if rows < 3:
        pad_rows = 3-rows
        pad_before = pad_rows // 2
        pad_after = pad_rows-pad_before
        
        output_grid = np.pad(output_grid, 
                             ((pad_before,pad_after),(0,0)),
                             mode='constant', constant_values=background_color)
    if cols < 3:
        pad_cols = 3-cols
        pad_before = pad_cols // 2
        pad_after = pad_cols-pad_before
        
        output_grid = np.pad(output_grid, 
                             ((0,0), (pad_before,pad_after)),
                             mode='constant', constant_values=background_color)

    return output_grid.tolist()
```

