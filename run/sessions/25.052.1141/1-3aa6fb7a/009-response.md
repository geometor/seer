# 1-3aa6fb7a • 009 • refine_code - CODE

---
```python
import numpy as np

def find_2x1_vertical_rectangles(grid, color):
    """
    Finds the coordinates of 2x1 vertical rectangles of the specified color.
    Returns a list of tuples, where each tuple contains the top and bottom coordinates of a rectangle.
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r, c] == color and grid[r + 1, c] == color:
                rectangles.append(((r, c), (r + 1, c)))
    return rectangles

def find_1x2_horizontal_rectangles(grid, color):
    """
    Finds coordinates of 1x2 horizontal rectangles
    """
    rectangles = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols-1):
            if grid[r,c] == color and grid[r,c+1] == color:
                rectangles.append(((r,c),(r,c+1)))
    return rectangles

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    Finds all 2x1 and 1x2 azure rectangles.
    For each 2x1 vertical azure rectangle, if it continues horizontally to
    the right with another 2x1 azure rectangle, place a blue (1) pixel immediately to the left of the top azure pixel of the original rectangle.
    For each 1x2 horizontal azure rectangle, if it continues vertically below with
    another 1x2 azure rectangle, places a blue pixel immediately above the left azure pixel of the original rectangle.
    """
    output_grid = np.copy(input_grid)
    azure_rectangles_v = find_2x1_vertical_rectangles(output_grid, 8)
    azure_rectangles_h = find_1x2_horizontal_rectangles(output_grid,8)

    for top_coord, bottom_coord in azure_rectangles_v:
        #Conditional Blue Placement - Right
        r_top, c_top = top_coord
        r_bot, c_bot = bottom_coord
        if (c_top + 1 < output_grid.shape[1] and
            output_grid[r_top, c_top + 1] == 8 and
            output_grid[r_bot, c_bot + 1] == 8):
                if c_top -1 >= 0:
                    output_grid[r_top,c_top-1] = 1

    for left_coord, right_coord in azure_rectangles_h:
        r_left, c_left = left_coord
        r_right, c_right = right_coord

        if (r_left + 1 < output_grid.shape[0] and
            output_grid[r_left+1,c_left] == 8 and
            output_grid[r_right+1,c_right] == 8):
            if r_left -1 >= 0:
                output_grid[r_left -1, c_left] = 1

    return output_grid
```

