# 890034e9 • 012 • refine_coder

---
```python
"""
1.  **Identify Objects:** Find all contiguous regions (objects) of yellow (4) and green (3) pixels in the input grid.
2.  **Iterate Pixels**: Iterate through each pixel of each yellow object.
3.  **Find Nearest Green:** For each yellow pixel, search for the nearest green pixel. "Nearest" is defined by the minimum number of moves (up, down, left, or right) required to reach a position that is adjacent to a green pixel without crossing other objects.
4. **Move Yellow Pixels:** Move each yellow pixel to an available adjacent cell of the _nearest_ green pixel, if a position is free (value is 0).
5. **Preserve:** Keep the relative shape of yellow objects intact as much as possible, moving individual pixels rather than entire objects at once.
6.  **Obstacles:** Azure (8) pixels, red (2) pixels, and other yellow pixels act as obstacles - do not move through them.
"""

import numpy as np
from collections import deque

def find_objects(grid, color):
    """
    Find contiguous regions (objects) of a specific color in the grid.
    """
    visited = np.zeros_like(grid, dtype=bool)
    objects = []

    def dfs(row, col, current_object):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1] or
                visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        current_object.append((row, col))
        dfs(row + 1, col, current_object)
        dfs(row - 1, col, current_object)
        dfs(row, col + 1, current_object)
        dfs(row, col - 1, current_object)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and not visited[row, col]:
                current_object = []
                dfs(row, col, current_object)
                objects.append(current_object)
    return objects

def is_valid(grid, row, col):
    """Check if a cell is within grid bounds."""
    return 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]

def is_obstacle(grid, row, col):
  """
  Checks to make sure a cell is not an obstacle, which is any
  color besides 0 (white).
  """
  return grid[row,col] != 0

def find_nearest_green(grid, start_row, start_col):
    """
    Find the nearest green pixel using Breadth-First Search (BFS).
    Returns the coordinates of a free adjacent cell, or None if no path is found.
    """
    queue = deque([(start_row, start_col, [])])  # (row, col, path)
    visited = np.zeros_like(grid, dtype=bool)
    visited[start_row, start_col] = True


    while queue:
        row, col, path = queue.popleft()

        # Check neighbors
        neighbors = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1)
        ]

        for neighbor_row, neighbor_col in neighbors:
            if is_valid(grid, neighbor_row, neighbor_col):

                #check if it is green and not blocked
                if grid[neighbor_row, neighbor_col] == 3:
                  #now look for adjacent empty cell
                  adj_neighbors = [
                    (neighbor_row -1, neighbor_col),
                    (neighbor_row + 1, neighbor_col),
                    (neighbor_row, neighbor_col -1),
                    (neighbor_row, neighbor_col+1)
                  ]
                  for adj_row, adj_col in adj_neighbors:
                    if is_valid(grid, adj_row, adj_col) and not is_obstacle(grid, adj_row, adj_col):
                      return adj_row, adj_col

                #check if we can traverse
                elif not visited[neighbor_row, neighbor_col] and not is_obstacle(grid, neighbor_row, neighbor_col):

                    visited[neighbor_row, neighbor_col] = True
                    new_path = path + [(neighbor_row, neighbor_col)]
                    queue.append((neighbor_row, neighbor_col, new_path))

    return None  # No green pixel found.

def transform(input_grid):
    """
    Moves yellow pixels to the nearest available position adjacent to a green pixel.
    """
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find yellow (4) objects
    yellow_objects = find_objects(output_grid, 4)

    # Flatten the list of yellow objects into a list of yellow pixels
    yellow_pixels = [pixel for obj in yellow_objects for pixel in obj]

    # Iterate through each yellow pixel
    for row, col in yellow_pixels:
        # Find the nearest green pixel and available adjacent cell
        nearest_green_coords = find_nearest_green(output_grid, row, col)

        # Move the yellow pixel if a path is found
        if nearest_green_coords:
            new_row, new_col = nearest_green_coords
            output_grid[row, col] = input_grid[row,col] #clear original
            output_grid[new_row, new_col] = 4  # Move yellow pixel

    return output_grid
```
