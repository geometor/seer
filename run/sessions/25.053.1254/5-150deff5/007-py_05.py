"""
1.  **Identify Gray Object:** Locate the contiguous region of gray (5) pixels in the input grid. This forms the input object.

2.  **Determine Bounding Box:**  Find the minimum and maximum x and y coordinates of the gray object. This defines its bounding box.

3.  **Vertical Split and Color Replacement:** The gray object is replaced by azure (8) and red (2) pixels. The replacement follows a vertical splitting pattern within the bounding box. Azure pixels generally replace gray pixels on the "right" or "outer" parts of the shape, and red pixels replace gray pixels on the "left" or "inner" parts of the shape, relative to a vertical axis that could shift.

4. **Precise Rule for Split and Assignment**
    - Examine each column of pixels (constant `y` value) within the grey object, from `min_y` to `max_y`
        - If the column contains gray pixels:
            - Consider the `x` coordinates of the gray pixels in that column.
            - If the x coordinate is the lowest x of gray in the column, color it red.
            - If the x coordinate is the highest x of gray in the column, color it azure.
            - If there are other x values in this column, alternate assigning red and azure

5. **Output:** Create a new grid where the original gray pixels are replaced according to the rules above, all other pixels remain unchanged.
"""

import numpy as np

def get_object_pixels(grid, color):
    return [(x,y) for x,row in enumerate(grid) for y, pixel in enumerate(row) if pixel == color]

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    gray_pixels = get_object_pixels(input_grid, 5)
    
    if not gray_pixels:
        return output_grid

    x_coords, y_coords = zip(*gray_pixels)
    min_y, max_y = min(y_coords), max(y_coords)

    # Iterate through each column (y-coordinate)
    for y in range(min_y, max_y + 1):
        column_pixels = [(x, y) for x, y in gray_pixels if y == y]
        if column_pixels:
            x_in_column = [x for x, _ in column_pixels]
            min_x_in_column = min(x_in_column)
            max_x_in_column = max(x_in_column)

            # Iterate through gray pixels in the current column
            for x, y in column_pixels:

                if x == min_x_in_column:
                    output_grid[x, y] = 2 #red
                elif x == max_x_in_column:
                    output_grid[x,y] = 8  #azure
                else:
                  # Alternate colors for pixels between min and max
                  if (x - min_x_in_column) % 2 == 0:
                      output_grid[x,y] = 2
                  else:
                      output_grid[x,y] = 8
    return output_grid