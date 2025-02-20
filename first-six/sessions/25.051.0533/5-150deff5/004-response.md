# 5-150deff5 • 004 • example_2 - CODE

---
```python
"""
The transformation rule can be summarized as follows:

1. Replace all gray (5) cells with azure (8) cells.
2.  Identify contiguous azure (8) regions.
3. For horizontally or vertically adjacent azure regions, fill the gap between them with red (2) cells, provided the gap is only one cell wide.
"""

import numpy as np

def find_objects(grid, color):
    """
    Find contiguous regions of the specified color.
    Returns a list of objects, where each object is a set of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, current_object):
        if (row, col) in visited or row < 0 or row >= rows or col < 0 or col >= cols or grid[row, col] != color:
            return
        visited.add((row, col))
        current_object.add((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == color and (row, col) not in visited:
                current_object = set()
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    # Initialize output grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find gray objects and replace with azure
    gray_objects = find_objects(input_grid, 5)
    for obj in gray_objects:
        for row, col in obj:
            output_grid[row, col] = 8

    # Fill gaps between adjacent azure regions
    azure_objects = find_objects(output_grid, 8)
    filled = set()  # Keep track of filled cells to avoid double filling

    for obj1 in azure_objects:
        for row1, col1 in obj1:
            for obj2 in azure_objects:
                if obj1 == obj2:
                    continue
                for row2, col2 in obj2:
                    # Check for horizontal adjacency and one-cell gap
                    if row1 == row2 and abs(col1 - col2) > 1:
                        min_col, max_col = sorted([col1, col2])
                        if max_col - min_col == 2:
                            if (row1,min_col+1) not in filled:
                                output_grid[row1, min_col + 1] = 2
                                filled.add((row1,min_col + 1))
                        else: # Check that all the cells are 0
                            fill = True
                            for c in range(min_col+1, max_col):
                                if output_grid[row1,c] != 0:
                                     fill = False
                            if fill:
                                for c in range(min_col+1, max_col):
                                    output_grid[row1,c] = 2

                    #  Check for vertical adjacency and one-cell gap
                    elif col1 == col2 and abs(row1 - row2) > 1:
                        min_row, max_row = sorted([row1, row2])
                        if max_row - min_row == 2:
                            if (min_row + 1, col1) not in filled:
                                output_grid[min_row + 1, col1] = 2
                                filled.add((min_row+1, col1))
                        else:  # Check all the cells are 0
                            fill = True
                            for r in range(min_row+1,max_row):
                                if output_grid[r,col1] != 0:
                                    fill = False
                            if fill:
                                for r in range(min_row+1,max_row):
                                    output_grid[r,col1]=2


    return output_grid
```

