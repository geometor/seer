"""
The input is a 10x10 grid of pixels. Each pixel has a color value of 0 (white) or 3 (green).
Identify green (3) pixels that are part of a 2x2 block of green (3) pixels which share at least one side and/or at least one corner.
Change the color value of the identified "internal" or "surrounded" green (3) pixels from green (3) to yellow (4).
Ensure all other pixels, those colored white, and those green pixels not part of an identified "internal" block retain their original values.
The output is a 10x10 grid with the same dimensions as the input, but with the specified color changes applied.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """
    Returns a list of neighbors, 4-connectivity.
    """
    rows, cols = grid.shape
    neighbors = []
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append((r, c))
            
    return neighbors

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # change output pixels 
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 3:
                neighbors = get_neighbors(input_grid, row, col)
                green_neighbors_count = 0
                
                for r,c in neighbors:                  
                    if input_grid[r,c] == 3:
                        green_neighbors_count += 1
                
                #look for a 2x2 block, either adjancent or corners
                if green_neighbors_count >=1 : # > 0 is sufficient for the example, more data to confirm
                    # check at least one 2x2 block
                    found_2x2 = False
                    for r1,c1 in neighbors:
                         if input_grid[r1,c1] == 3:  # a green neighbor exist.
                            neighbors2 = get_neighbors(input_grid,r1,c1)
                            for r2, c2 in neighbors2:
                                if (r2,c2) != (row, col) and input_grid[r2,c2] == 3:  #found another green linked to r1,c1
                                    output_grid[row,col] = 4 # change it
                                    found_2x2 = True
                                    break
                         if found_2x2:
                            break
    return output_grid