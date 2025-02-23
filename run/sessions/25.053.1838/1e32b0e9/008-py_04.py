"""
1.  **Identify the Red Cross:** Locate the contiguous block of red (2) pixels forming the cross shape.

2.  **Identify Internal Blue Pixels:** Locate the blue (1) pixels within the arms of the red cross.

3.  **Locate White Regions inside the Cross:** Identify the regions of white (0) pixels adjacent to the red cross on the inside of the cross and adjacent to blue pixels.

4. **Conditional Fill:**
    Iterate over each white pixel inside the cross:
    - If the white pixel is the part of a 3x3 square of other white pixels (including diagonal) AND shares an edge or diagonal with at least one of the blue (1) pixels identified in Step 2, change color to red (2)

In essence, the transformation fills in specific white areas within the red cross structure with red, contingent upon their proximity to both other white pixels in a 3x3 grid, and existing blue pixels.
"""

import numpy as np

def find_object(grid, color):
    # returns a list of (r,c) tuples for a given color
    coords = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == color:
                coords.append((r, c))
    return coords

def is_within_cross(coord, red_cross_coords):
    # determine of coord is within the cross shape defined by red_cross_coords
    r, c = coord
    min_r = min([x[0] for x in red_cross_coords])
    max_r = max([x[0] for x in red_cross_coords])
    min_c = min([x[1] for x in red_cross_coords])
    max_c = max([x[1] for x in red_cross_coords])

    return min_r < r < max_r and min_c < c < max_c

def is_adjacent(coord1, coord2):
     # Check if two coordinates are adjacent (including diagonals)
    r1, c1 = coord1
    r2, c2 = coord2
    return abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1

def has_3x3_square(grid, coord, color):
    # Check if a cell has a 3x3 area filled with color, around it.
    r, c = coord
    count = 0
    for i in range(max(0, r - 1), min(len(grid), r + 2)):
        for j in range(max(0, c - 1), min(len(grid[0]), c + 2)):
            if grid[i][j] == color:
                count+=1
    return count == 9

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find object coords
    red_cross_coords = find_object(input_grid, 2)
    blue_coords = find_object(input_grid, 1)
    white_coords = find_object(input_grid, 0)

    # filter white coords
    internal_white_coords = [coord for coord in white_coords if is_within_cross(coord, red_cross_coords)]

    # fill by condition
    for r, c in internal_white_coords:
        if has_3x3_square(input_grid, (r,c), 0):
            for blue_coord in blue_coords:
                if is_adjacent((r, c), blue_coord):
                    output_grid[r, c] = 2
                    break
    return output_grid