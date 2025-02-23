"""
1. Find every object of size 1 in the input.
2. For each of those objects:
   - if the object is red:
     - Place a yellow cell above it.
     - Place a yellow cell below it.
     - Place a yellow cell two positions to its left.
   - if the object is blue:
     - Place 3 orange cells to form a vertical line at its left.
     - Place one orange cell at the bottom-right of the blue cell, with distance 1.
3. Maintain original objects of size 1.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all single-cell objects
    objects = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] != 0:
                # Check if it's a single-cell object (not part of a larger object)
                is_single = True
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0 and dx == 0) or not (0 <= y + dy < grid.shape[0] and 0 <= x + dx < grid.shape[1]):
                            continue
                        if grid[y + dy, x + dx] == grid[y, x]:
                            is_single = False
                            break
                    if not is_single:
                        break
                if is_single:
                    objects.append((y, x, grid[y, x]))
    return objects

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    
    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)
    
    # Process each single-cell object
    for y, x, color in single_cell_objects:
        if color == 8:
          continue
        if color == 2:  # Red
            if y > 0:
                output_grid[y - 1, x] = 4  # Above
            if y < output_grid.shape[0] - 1:
                output_grid[y + 1, x] = 4  # Below
            if x > 0 :
                output_grid[y-1,x-1] = 4
            if x > 0:
                output_grid[y+1,x-1] = 4
            
        elif color == 1:  # Blue
            if x > 0:
              for i in range(3):
                if 0 <= y - 1 + i < output_grid.shape[0] :
                  output_grid[y - 1 + i, x - 1] = 7  # Left
            if y < output_grid.shape[0] - 1 and x < output_grid.shape[1] -1 :
              output_grid[y + 1, x + 1] = 7  # Bottom-right
    
    return output_grid