"""
1.  **Identify the Bordered Region:** Find a contiguous region within the input grid that is completely enclosed by a border of black (color 0) pixels. The border must be one pixel thick. The bordered region will form a rectangle.

2.  **Identify Interior:** The "interior" consists of all pixels *inside* the black border.

3.  **Extract Interior:** Create a new, smaller grid containing *only* the pixels within the identified bordered region, *excluding* the black border pixels. The dimensions of the new grid will match the height and width of the interior region.

4.  **Output:** Return the extracted interior region as the new grid. If no black border exists, the output will be an empty grid. The output grid includes only the inside of the rectangle.
"""

import numpy as np

def find_border_and_interior(grid, border_color=0):
    """Finds the bounding box of the interior of a bordered region."""
    rows, cols = grid.shape
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1

    # Check for border and interior existence.
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == border_color:
                # Check surrounding pixels for interior
                if r + 1 < rows and grid[r+1, c] != border_color:
                   
                    max_row = max(max_row, r)
                    min_row = min(min_row, r)
                    max_col = max(max_col,c)
                    min_col = min(min_col,c)
                elif c+1 < cols and grid[r,c+1] != border_color:
                    
                    max_row = max(max_row, r)
                    min_row = min(min_row, r)
                    max_col = max(max_col,c)
                    min_col = min(min_col,c)
                elif r - 1 >= 0 and grid[r-1, c] != border_color:
                   
                    max_row = max(max_row, r)
                    min_row = min(min_row, r)
                    max_col = max(max_col,c)
                    min_col = min(min_col,c)
                elif c - 1 >= 0 and grid[r, c-1] != border_color:
                    
                    max_row = max(max_row, r)
                    min_row = min(min_row, r)
                    max_col = max(max_col,c)
                    min_col = min(min_col,c)
    #Move inwards to exclude border
    if max_row > -1:
        min_row +=1
        max_row -= -1
        min_col += 1
        max_col -=1
    
    
    return min_row, max_row, min_col, max_col


def transform(input_grid):
    """Transforms the input grid by extracting the region within a bordered region."""
    input_grid = np.array(input_grid)
    
    # Find the bounding box of interior
    min_row, max_row, min_col, max_col = find_border_and_interior(input_grid)


    if max_row == -1: # Handle cases with no border.
        return [[]]

    # Extract interior
    output_grid = input_grid[min_row:max_row, min_col:max_col]
    
    return output_grid.tolist()