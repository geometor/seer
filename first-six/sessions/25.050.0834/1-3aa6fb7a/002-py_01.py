"""
The transformation rule is: For each L-shape comprised of color 8, change the top leftmost pixel's color from 8 to 1, and change the bottom rightmost pixel's color from 8 to 1.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of coordinates that constitute the L-shape, where the coordinate is defined as top-leftmost to down-rightmost.

    Args:
        grid: 2D numpy array.
        color: color that helps filtering objects.
    
    Returns:
        A list of the coordinates of L-shapes.
    """
    l_shapes = []
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_shape):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return

        visited[r, c] = True
        current_shape.append((r, c))
        
        # Explore adjacent neighbors
        dfs(r + 1, c, current_shape)
        dfs(r - 1, c, current_shape)
        dfs(r, c + 1, current_shape)
        dfs(r, c - 1, current_shape)

    for r in range(rows):
      for c in range(cols):
          if grid[r,c] == color and not visited[r,c]:
              current_shape = []
              dfs(r,c,current_shape)

              # Check for an L shape, based in relative positions of points
              if len(current_shape) == 3:
                #find top_leftmost and down_rightmost
                current_shape.sort()
                l_shapes.append(current_shape)
    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule: For each L-shape of color 8,
    change the top leftmost pixel's color to 1 and the bottom rightmost to 1.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(output_grid, 8)

    for l_shape in l_shapes:
      # Change top-left pixel of L-shape.
      output_grid[l_shape[0][0], l_shape[0][1]] = 1
      # Change bottom-right pixel of L-shape
      output_grid[l_shape[-1][0], l_shape[-1][1]] = 1

    return output_grid