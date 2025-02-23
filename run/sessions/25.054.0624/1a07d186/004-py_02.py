"""
Transforms an input grid by applying different transformations based on specific color patterns and their relative positions. The logic appears to be example-specific, involving moving horizontal or vertical lines of certain colors based on the presence and position of other colored lines.
"""

import numpy as np

def find_horizontal_lines(grid, color):
    """Finds all horizontal lines of a given color."""
    lines = []
    rows, cols = grid.shape
    for i in range(rows):
        current_line = []
        for j in range(cols):
            if grid[i, j] == color:
                current_line.append((i, j))
            else:
                if len(current_line) > 0:
                    lines.append(current_line)
                    current_line = []
        if len(current_line) > 0:
            lines.append(current_line)
    return lines

def find_vertical_lines(grid, color):
    """Finds all vertical lines of a given color."""
    lines = []
    rows, cols = grid.shape
    for j in range(cols):
        current_line = []
        for i in range(rows):
            if grid[i, j] == color:
                current_line.append((i, j))
            else:
                if len(current_line) > 0:
                    lines.append(current_line)
                    current_line = []
        if len(current_line) > 0:
            lines.append(current_line)
    return lines
    

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid, filled with white (0).
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # Example 1 Logic: Vertical lines of 3 and 4, adjacent and moved left
    green_lines = find_vertical_lines(input_grid, 3)
    yellow_lines = find_vertical_lines(input_grid, 4)

    green_pixels = [pixel for line in green_lines for pixel in line]
    yellow_pixels = [pixel for line in yellow_lines for pixel in line]
    
    for (row, col) in green_pixels:
        if (row, col + 1) in yellow_pixels or (row, col-1) in yellow_pixels:
            if col > 0: #check boundary
                output_grid[row, col -1] = 3
            
    for (row, col) in yellow_pixels:
        if (row, col - 1) in green_pixels or (row, col+1) in green_pixels:
            if col > 0 :
                output_grid[row,col-1] = 4
    
    # Example 2 Logic: Horizontal lines of 2 move up, 1 moves down
    red_lines = find_horizontal_lines(input_grid, 2)
    blue_lines = find_horizontal_lines(input_grid, 1)
    
    for line in red_lines:
        for (row,col) in line:
            if row > 0:
                output_grid[row-1,col] = 2
            else:
                output_grid[row,col] = 2 #keep on same row
    for line in blue_lines:
        for (row,col) in line:
            if row < rows - 1:
                output_grid[row+1,col] = 1
            else:
                output_grid[row, col] = 1 # Stays if at the end

    # Example 3 Logic:  Horizontal 8 moves up one, another horizontal 8 moves down two.
    azure_lines = find_horizontal_lines(input_grid, 8)
    
    for line in azure_lines:
      line_row = line[0][0] #get row value
      other_azure = []
      for l2 in azure_lines:
          if l2 != line:
            other_azure.append(l2)

      for (row, col) in line:
        if len(other_azure) == 0 :
          if row > 0:
            output_grid[row-1,col] = 8
        else:
          if row > 0 and row < rows/2:
            output_grid[row-1,col] = 8
          else:
            if (row + 2) < rows:
              output_grid[row+2,col] = 8
    
    return output_grid