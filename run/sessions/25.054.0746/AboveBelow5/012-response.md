# AboveBelow5 • 012 • refine_coder

---
```python
"""
1.  **Identify Target Column:** Focus on the second column (index 1) of the input grid.
2.  **Find First Orange Pixel:**  Find the first pixel of color orange (7) in the second column.
3.  **Determine Propagation Extent:** The original row index of this first orange pixel determines the number of cells at the top of column 2 which turn orange.
4.  **Propagate Orange:** Change the color of the top *n* cells of the second column to orange, where *n* is the row index of the originally found orange pixel in the input.
5.  **Replace other Orange with Yellow:** Find all the *other* pixels of color orange (7) in the second column. If these orange pixel exists, and it's row index > 0, change its color to yellow (4).
"""

import numpy as np

def find_first_pixel_by_color_in_column(grid, color, column_index):
    # Find the coordinates (row, col) of the first pixel of the specified color within a given column.
    for row_index, row in enumerate(grid):
        if row[column_index] == color:
            return (row_index, column_index)
    return None  # Return None if no such pixel is found.

def find_all_pixels_by_color_in_column(grid, color, column_index):
    # Find the coordinates (row, col) of all pixels of a specified color within a column.
    pixels = []
    for row_index, row in enumerate(grid):
      if row[column_index] == color:
        pixels.append((row_index, column_index))
    return pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find the first orange pixel in the second column (index 1).
    first_orange_pixel_coords = find_first_pixel_by_color_in_column(input_grid, 7, 1)

    # if there is no orange in column 2, return
    if first_orange_pixel_coords is None:
        return output_grid

    # Determine the number of cells to change to orange.
    n = first_orange_pixel_coords[0]
    
    # Propagate the orange color to the top n cells in column 2.
    for i in range(n + 1):  # Include the original orange pixel's row
       if i < output_grid.shape[0]: # prevent index from going out of bounds.
            output_grid[i, 1] = 7
    
    # find all orange pixels
    orange_pixels = find_all_pixels_by_color_in_column(input_grid, 7, 1)
    
    # change all other orange to yellow
    for pixel in orange_pixels:
        if pixel[0] > n:
            output_grid[pixel[0]][1] = 4

    return output_grid
```

