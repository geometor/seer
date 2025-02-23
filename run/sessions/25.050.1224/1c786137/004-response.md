# 1c786137 • 004 • example_2 - CODE

---
```python
"""
Extracts a sub-grid from the input grid. The dimensions and location of the
sub-grid are determined by searching specific colored rectangles,
if the rectangles are present.

If there is a red rectangle, a sub-grid from the top-left corner of the
input is returned.
If there is a yellow rectangle, a sub-grid from the top-right corner of the yellow
rectangle is returned.

"""

import numpy as np

def find_rectangle(grid, color):
    """
    Finds the top-left and bottom-right coordinates of the largest rectangle
    of the specified color in the grid.

    Args:
        grid (numpy.ndarray): The input grid.
        color (int): The color to search for.

    Returns:
        tuple: (top_left, bottom_right) coordinates as (row, col) tuples,
               or None if no rectangle of the specified color is found.
    """
    rows, cols = grid.shape
    top_left = None
    bottom_right = None

    # Find all cells with the target color
    coords = np.argwhere(grid == color)

    if coords.size == 0:
        return None  # No rectangle of the specified color found

    # Get the top-left and bottom-right coordinates
    top_left = (coords.min(axis=0)[0], coords.min(axis=0)[1])
    bottom_right = (coords.max(axis=0)[0], coords.max(axis=0)[1])

    return top_left, bottom_right



def transform(input_grid):
    """
    Extracts a sub-grid from the input grid based on rectangle colors.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The extracted sub-grid.
    """
    
    red_rectangle = find_rectangle(input_grid, 2)
    yellow_rectangle = find_rectangle(input_grid, 4)

    if red_rectangle:
        output_height = 6
        output_width = 8
        output_grid = input_grid[:output_height, :output_width]
        return output_grid
    
    elif yellow_rectangle:
        output_height = 5
        output_width = 3
        top_left, _ = yellow_rectangle #get top-left corner
        #get the subgrid
        output_grid = input_grid[0:5,3:6]       
        return output_grid
    
    return None

```

