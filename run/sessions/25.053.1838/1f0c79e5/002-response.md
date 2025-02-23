# 1f0c79e5 • 002 • example_1 - CODE

---
```python
"""
1.  **Identify the Object:** Locate the connected region of non-zero pixels in the input grid.
2.  **Bounding shape:** identify the smallest rectangle that fits the object.
3. **Area Calculation**: calculate the area of that rectangle
4.  **Construct Transformed Shape:** Starting from the top-left corner, form the square with the closest area by expanding 1 unit in each direction (up, down, right, left)
5.  **Color Transformation:** All original colors of the object change to the most frequent color of the original object, in this case yellow (4).
"""

import numpy as np

def get_object(grid):
    # Find non-zero pixels
    non_zero_pixels = np.argwhere(grid != 0)

    # if no object return none
    if len(non_zero_pixels) == 0:
      return None

    # Find top-left and bottom-right corners
    min_row, min_col = non_zero_pixels.min(axis=0)
    max_row, max_col = non_zero_pixels.max(axis=0)

    # Create object mask
    object_mask = (grid[min_row:max_row+1, min_col:max_col+1] != 0)

    # return object grid, start coordinate
    return grid[min_row:max_row+1, min_col:max_col+1], (min_row, min_col)

def get_most_frequent_color(grid):
    # Flatten the grid and remove zeros
    non_zero_values = grid[grid != 0]

    # Count occurrences of each color
    unique, counts = np.unique(non_zero_values, return_counts=True)
    if len(unique) > 0:
        most_frequent_index = np.argmax(counts)
        return unique[most_frequent_index]
    return 0

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find the object and its bounding box
    obj, (min_row, min_col) = get_object(input_grid)

    # if not object found, return the original
    if obj is None:
        return output_grid
    
    # Get object height and width
    height, width = obj.shape

    # Calculate Area
    area = height * width

    # find closest square
    side = int(np.ceil(np.sqrt(area)))

    # Get most frequent color
    most_frequent_color = get_most_frequent_color(obj)

    # resize the original object area to background 0 in ouput grid
    output_grid[min_row:min_row+height, min_col:min_col+width] = 0

    # Construct the transformed shape - square
    for i in range(side):
        for j in range(side):
            row = min_row + i
            col = min_col + j
            if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1]:
                output_grid[row, col] = most_frequent_color

    return output_grid
```
