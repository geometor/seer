# 50846271 • 006 • refine_coder

---
```python
"""
Identifies red (2) pixels in the input grid. Changes red pixels that form
a three-pixel L shape to azure (8), but only if the L-shape is not adjacent to a red line
of length greater than 2. Other pixels remain unchanged.
"""

import numpy as np

def is_l_shape(grid, row, col):
    """Checks if a red pixel at (row, col) is the center of a 3-pixel L-shape."""
    rows, cols = grid.shape
    color = grid[row, col]
    neighbors = 0
    
    #check the direct neighbors
    neighbor_coords = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            neighbors += 1
            neighbor_coords.append((nr,nc))

    if neighbors == 2:
        #check if the two neighbors create a vertical or horizontal line, if so it's a line and not an L
        if neighbor_coords[0][0] == neighbor_coords[1][0] or neighbor_coords[0][1] == neighbor_coords[1][1]:
          return False #it's a line of three, not an L
        return True
    
    return False

def is_part_of_line(grid, row, col):
    """
    Checks if a red pixel at (row, col) is part of a horizontal, vertical, or diagonal line
    of length greater than 2.
    """
    rows, cols = grid.shape
    color = grid[row, col]

    # Check in all four directions
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        count = 1  # Count the current pixel
        # Extend in the positive direction
        nr, nc = row + dr, col + dc
        while 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            count += 1
            nr, nc = nr + dr, nc + dc
        # Extend in the negative direction
        nr, nc = row - dr, col - dc
        while 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            count += 1
            nr, nc = nr - dr, nc - dc
        if count > 2:
            return True

    # Check diagonals
    for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        count = 1
        nr, nc = row + dr, col + dc
        while 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            count += 1
            nr, nc = nr + dr, nc + dc

        nr, nc = row - dr, col - dc
        while 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
            count +=1
            nr, nc = nr - dr, nc - dc
        if count > 2:
            return True

    return False

def is_adjacent_to_line(grid, row, col, l_neighbors):
    rows, cols = grid.shape
    for nr, nc in l_neighbors:      
        if is_part_of_line(grid, nr, nc):
            return True
    return False
    

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each pixel of the grid
    for row in range(rows):
        for col in range(cols):
            # Check if the pixel is red (2)
            if input_grid[row, col] == 2:
                #check if part of line
                if is_part_of_line(output_grid, row, col):
                    continue #skip lines
                
                # Check if L shape
                if is_l_shape(output_grid, row, col):
                    #get the neighbors to check for adjacency
                    color = grid[row, col]
                    neighbor_coords = []
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
                            neighbor_coords.append((nr,nc))
                    #check adjacency to line
                    if not is_adjacent_to_line(output_grid, row, col, neighbor_coords):
                        output_grid[row, col] = 8


    return output_grid
```
