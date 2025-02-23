"""
1. Excise Column: Remove the fourth column (all gray/5s) of the input grid.
2. Condense: Reduce to a 3x3 grid by:
   - copying the "left half" (first three numbers), skipping any complete blue (1) vertical columns.
3. Color Conversion: The blue cells (1) bordered on two sides (either vertical or horizontal, not diagonal) are changed to color red(2)
"""

import numpy as np

def get_neighbors(grid, r, c):
    neighbors = []
    if r > 0:
        neighbors.append(grid[r-1][c])  # Up
    if r < len(grid) - 1:
        neighbors.append(grid[r+1][c])  # Down
    if c > 0:
        neighbors.append(grid[r][c-1])  # Left
    if c < len(grid[0]) - 1:
        neighbors.append(grid[r][c+1])  # Right
    return neighbors

def transform(input_grid):
    # initialize output_grid
    grid = np.array(input_grid)

    # 1. Excise Column: Remove the fourth column (index 3).
    grid = np.delete(grid, 3, axis=1)

    # 2. Condense & 3. Color Conversion in one pass
    output_grid = np.zeros((3, 3), dtype=int)
    
    grid_rows, grid_cols = grid.shape
    
    
    # Create a mapping between original grid and reduced grid
    k=0
    for j in range(grid_cols):
      if len(np.where(grid[:,j] == 1)[0]) < grid_rows:
          #print(f'copying col {j} to {k}')
          for i in range(grid_rows):
            output_grid[i,k] = grid[i,j]
          k=k+1
          if k>2:
            break

    #print(output_grid)

    for r in range(3):
        for c in range(3):
            if output_grid[r, c] == 1:
                neighbors = get_neighbors(output_grid, r, c)
                if neighbors.count(0) >= 2:
                    output_grid[r, c] = 2

    return output_grid