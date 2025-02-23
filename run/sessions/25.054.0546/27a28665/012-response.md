# 27a28665 • 012 • refine_coder

---
```python
"""
1. Examine Corners: Identify the four corner pixels of the input grid: top-left, top-right, bottom-left, and bottom-right.
2. Count Specific Colors:
    *   If all four corners are of color '8' (azure), the output is 2.
    *   If all four corners are of color '5'(grey), the output is 2.
    *   If the top-left and bottom-right corners are the same color, and the top-right and bottom-left corners are black (value 0), the result is 1.
    *   If two of the corners, top-right and bottom-left are of same color, and other corners are black, the result is 3.
    *   If all four corners are black (value 0), the output is 6.
    *    Otherwise, if top-left and bottom-right corners are of the same color while other two don't match, then result is 1.
3. Create Output: Create a 1x1 output grid. The single pixel's value is the result of the counting logic.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the colors of its corner pixels.
    """
    rows, cols = input_grid.shape
    top_left = input_grid[0, 0]
    top_right = input_grid[0, cols - 1]
    bottom_left = input_grid[rows - 1, 0]
    bottom_right = input_grid[rows - 1, cols - 1]

    if top_left == top_right == bottom_left == bottom_right == 8:
        count = 2
    elif top_left == top_right == bottom_left == bottom_right == 5:
        count = 2
    elif top_left == bottom_right and top_right == bottom_left == 0:
        count = 1
    elif top_right == bottom_left and top_left==bottom_right==0:
        count = 3
    elif top_left == top_right == bottom_left == bottom_right == 0:
        count = 6
    elif top_left == bottom_right and top_left != top_right and top_left != bottom_left:
        count = 1

    else:
        count=0 # default

    output_grid = np.array([[count]])
    return output_grid
```
