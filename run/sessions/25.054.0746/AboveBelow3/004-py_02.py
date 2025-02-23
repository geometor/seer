"""
Find all horizontal lines or line segments (contiguous pixels of the same color) in the input grid.
Identify the top-most line segment.
If the identified top-most line segment spans 3 or fewer columns and is located, at most, from the first to the third column, inclusive, of the image, delete that line segment and add an empty row to the top of the grid. Otherwise the output grid is the same as the input grid.
"""

import numpy as np

def find_horizontal_lines(grid):
    lines = []
    for i, row in enumerate(grid):
        start = -1
        for j, pixel in enumerate(row):
            if start == -1:
                if pixel != 0:
                  start = j
            elif pixel != grid[i,start]:
                lines.append((i, start, j - 1, grid[i,start]))
                start = -1 if pixel == 0 else j
        if start != -1:
            lines.append((i, start, len(row) - 1, grid[i,start]))
    return lines

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all horizontal lines
    lines = find_horizontal_lines(output_grid)
    
    #find top line
    if not lines:
      return output_grid
    
    top_line = min(lines, key=lambda x: x[0])

    # Check if the top-most line spans 3 or fewer columns and all members are within the first 3 columns.
    if (top_line[2] - top_line[1] + 1) <= 3 and top_line[2] <= 2:
        #remove line
        for col in range(top_line[1], top_line[2] + 1):
            output_grid[top_line[0]][col] = 0
        #add empty row at top
        output_grid = np.vstack([np.zeros((1, output_grid.shape[1])), output_grid[:-1,:]])

    return output_grid