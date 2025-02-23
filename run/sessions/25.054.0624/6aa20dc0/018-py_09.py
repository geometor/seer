"""
Identifies isolated pixels or small groups of pixels (color islands) that differ from the background color and replicates them, creating small clusters, while preserving the background.
"""

import numpy as np

def get_background_color(grid):
    # Flatten the grid and count the occurrences of each color
    unique, counts = np.unique(grid, return_counts=True)
    # Return the color with the highest count
    return unique[np.argmax(counts)]

def is_isolated(grid, r, c, background_color):
    rows, cols = len(grid), len(grid[0])
    color = grid[r][c]
    if color == background_color:
        return False

    neighbors = []
    if r > 0:
        neighbors.append(grid[r-1][c])
    if r < rows - 1:
        neighbors.append(grid[r+1][c])
    if c > 0:
        neighbors.append(grid[r][c-1])
    if c < cols - 1:
        neighbors.append(grid[r][c+1])

    for neighbor_color in neighbors:
        if neighbor_color == color:
            return False
    return True

def get_object_size_and_type(grid, r, c, background_color):
    rows, cols = len(grid), len(grid[0])
    color = grid[r][c]
    if color == background_color:
      return (0,0), "background"

    visited = set()
    q = [(r,c)]
    visited.add((r,c))
    min_r, max_r = r, r
    min_c, max_c = c, c

    while q:
      cur_r, cur_c = q.pop(0)
      min_r = min(min_r, cur_r)
      max_r = max(max_r, cur_r)
      min_c = min(min_c, cur_c)
      max_c = max(max_c, cur_c)

      neighbors = []
      if cur_r > 0:
          neighbors.append((cur_r - 1, cur_c))
      if cur_r < rows - 1:
          neighbors.append((cur_r + 1, cur_c))
      if cur_c > 0:
            neighbors.append((cur_r, cur_c -1))
      if cur_c < cols - 1:
          neighbors.append((cur_r, cur_c + 1))

      for nr, nc in neighbors:
        if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == color:
          q.append((nr, nc))
          visited.add((nr, nc))

    height = max_r - min_r + 1
    width = max_c - min_c + 1
    if height == 1 and width == 1:
      object_type = "isolated_pixel"
    elif height <= 3 and width <=3:
        object_type = "small_group"
    else:
      object_type = "large_group" #should not occur

    return (height, width), object_type, (min_r, min_c)
  

def transform(input_grid):
    input_grid = np.array(input_grid)
    rows, cols = len(input_grid), len(input_grid[0])
    output_grid = input_grid.copy()
    background_color = get_background_color(input_grid)

    for r in range(rows):
        for c in range(cols):
          object_size, object_type, top_left = get_object_size_and_type(input_grid, r, c, background_color)
          if object_type == "isolated_pixel":
            #Replicate down and right
            new_r = (r + 1) % rows
            new_c = (c + 1) % cols
            output_grid[new_r, new_c] = input_grid[r,c]

          elif object_type == "small_group":
            height, width = object_size
            start_r, start_c = top_left

            if (height,width) == (2,1) or (height, width) == (1,2) or (height,width) == (2,2):
                for i in range(2):
                  for j in range(2):
                    new_r = (start_r + i) % rows
                    new_c = (start_c + j) % cols
                    output_grid[new_r,new_c] = input_grid[start_r,start_c]

            elif (height, width) == (3,1) or (height, width) == (1,3):
                for i in range(3):
                  for j in range(3):
                    new_r = (start_r + i) % rows
                    new_c = (start_c + j) % cols
                    output_grid[new_r, new_c] = input_grid[start_r, start_c]
    return output_grid.tolist()