# 32597951 • 012 • refine_coder

---
```python
"""
The input is a grid of pixels. The algorithm identifies a contiguous region of '8' (azure) pixels. Within this region, a cross pattern is created by changing specific '8' pixels to '3' (green). The cross is centered within the azure region. If the region has an odd number of rows and columns, the cross is a single row and column. If the region has an even number of rows or columns, the cross occupies two rows and two columns centered in the region. Pixels not part of the azure region are unchanged.
"""

import numpy as np

def find_contiguous_region(grid, value):
    # Find the coordinates of all cells with the specified value.
    coords = np.argwhere(grid == value)
    if coords.size == 0:
        return None, None

    # Find top-left and bottom-right using min/max of the coordinates
    min_row = coords[:, 0].min()
    max_row = coords[:, 0].max()
    min_col = coords[:, 1].min()
    max_col = coords[:, 1].max()

    return (min_row, min_col), (max_row, max_col)

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    input_grid_np = np.array(input_grid)

    # Find the contiguous region of '8's
    top_left, bottom_right = find_contiguous_region(input_grid_np, 8)

    if top_left is None :
      return output_grid

    # Calculate the dimensions of the region.
    height = bottom_right[0] - top_left[0] + 1
    width = bottom_right[1] - top_left[1] + 1

    # Calculate center row and column
    center_row = top_left[0] + height // 2
    center_col = top_left[1] + width // 2
    
    # Iterate through the '8' region and change to '3' based on the cross pattern.
    for row in range(top_left[0], bottom_right[0] + 1):
        for col in range(top_left[1], bottom_right[1] + 1):
            if output_grid[row, col] == 8:
                #If height and width are odd, center cross on row and col
                if height % 2 != 0 and width % 2 != 0:
                    if row == center_row or col == center_col:
                       output_grid[row, col] = 3
                #If height is even
                elif height % 2 == 0 and width % 2 != 0:
                    if (row == center_row or row == center_row - 1) or col == center_col:
                        output_grid[row,col] = 3
                #if width is even
                elif width % 2 == 0 and height % 2 != 0:
                    if row == center_row or (col == center_col or col == center_col -1):
                        output_grid[row,col] = 3
                #If height and width are even, cross will use two rows and two cols
                else:
                    if (row == center_row or row == center_row - 1) and (col == center_col or col == center_col - 1) :
                       output_grid[row, col] = 3
    return output_grid.tolist()
```
