# b8825c91 • 011 • refine_coder

---
```python
"""
1.  **Identify Changed Pixels:** Determine all pixels that have a different color in the output grid compared to the input grid.

2.  **Analyze Surroundings:** For each changed pixel, find the contiguous shape it belonged to in the *input* grid. Determine the set of colors directly adjacent (up, down, left, right) to that shape.

3.  **Apply Transformation Rules:**
    *   If a pixel of color 4 is surrounded by colors including 6, and is directly above, below, to the left or to the right of a pixel of color 4, then:
        * if the surroundings also include 9, change color 4 to color 3.
        * If the surroundings also include 1 and 8, change color 4 to 8.
        * If the surroundings also include 5, change color 4 to 1
        * If the surroundings also include 8, change color 4 to 1.
    * If a pixel of color 1 is surrounded by colors including 6, and is directly above, below, to the left or to the right of a pixel of color 4, then:
        * if the surroundings also include 9, change color 1 to 9.
        * If the surroundings also include 8, change color 1 to 5.
        * if the surroundings also include 2, change color 1 to 5.
        * If the surroundings also include 3 and 7, change color 1 to 2.
        * If the surroundings also include 8, change color 1 to 2.
    * If a pixel of color 4 is surrounded by 1,2,7,8,9, change to 2
    * If a pixel of color 4 is surrounded by 1,3,6,7,9, change to 5
    * Otherwise, the pixel's color remains unchanged.

4. Create new grid based on rules.
"""

import numpy as np

def get_contiguous_shape(grid, start_row, start_col, color):
    """
    Finds the contiguous shape containing the starting pixel.
    """
    rows, cols = grid.shape
    visited = set()
    shape = []

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        shape.append((row, col))
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    dfs(start_row, start_col)
    return shape

def get_surrounding_colors(grid, shape):
    """
    Gets the colors of the pixels surrounding a given shape.
    """
    rows, cols = grid.shape
    surrounding_colors = set()
    for r, c in shape:
        # Check adjacent cells (up, down, left, right)
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                surrounding_colors.add(grid[nr, nc])
    return surrounding_colors

def is_adjacent_to_color(grid, shape, color):
    rows, cols = grid.shape
    for r, c in shape:
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr,nc] == color:
                return True
    return False

def transform(input_grid):
    # initialize output_grid
    output_grid = input_grid.copy()
    rows, cols = input_grid.shape
    
    for r in range(rows):
        for c in range(cols):
            # color 4 changes
            if input_grid[r,c] == 4:
                shape = get_contiguous_shape(input_grid, r, c, 4)
                surround = get_surrounding_colors(input_grid, shape)
                if 6 in surround and is_adjacent_to_color(input_grid,shape,4):
                    if 9 in surround:
                        output_grid[r,c] = 3
                    elif 1 in surround and 8 in surround:
                        output_grid[r,c] = 8
                    elif 5 in surround:
                        output_grid[r,c] = 1
                    elif 8 in surround:
                        output_grid[r,c] = 1
                elif all(x in surround for x in [1,2,7,8,9]):
                    output_grid[r,c] = 2
                elif all(x in surround for x in [1,3,6,7,9]):
                    output_grid[r,c] = 5
            # color 1 changes
            elif input_grid[r,c] == 1:
                shape = get_contiguous_shape(input_grid, r,c,1)
                surround = get_surrounding_colors(input_grid,shape)
                if 6 in surround and is_adjacent_to_color(input_grid,shape,4):
                    if 9 in surround:
                        output_grid[r,c] = 9
                    elif 8 in surround:
                        output_grid[r,c] = 5
                    elif 2 in surround:
                        output_grid[r,c] = 5
                    elif 3 in surround and 7 in surround:
                        output_grid[r,c] = 2
                    elif 8 in surround:
                        output_grid[r,c] = 2
    return output_grid
```
