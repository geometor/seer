"""
  1.  Identify "L-shaped" objects composed of 3 pixels.
  2.  Transform these L-shapes:
      a. If Azure, create a 2x2 Azure square in the center.
      b. If Blue, create a 2x2 Blue square in the center.
      c. If Yellow, create a 3x3 cross where the center pixel is blank (0), and the remaining cross pixels are surrounded by pixels of the same color.
  3. Find large shapes on left, convert to a frame.
"""

import numpy as np

def find_objects(grid):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, color, current_object):
        if not is_valid(r, c) or visited[r, c] or grid[r, c] != color:
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, color, current_object)
        dfs(r - 1, c, color, current_object)
        dfs(r, c + 1, color, current_object)
        dfs(r, c - 1, color, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c] and grid[r, c] != 0:
                current_object = []
                dfs(r, c, grid[r, c], current_object)
                objects.append((grid[r, c], current_object))
    return objects

def is_l_shape(pixels):
    if len(pixels) != 3:
        return False
    # Convert pixel coordinates to numpy arrays for easier calculation
    pixels = np.array(pixels)
    # Calculate distances between all pairs of points
    distances = np.sum((pixels[:, np.newaxis, :] - pixels[np.newaxis, :, :]) ** 2, axis=2)
    # Check if the distances correspond to an L-shape (two distances of 1 and one distance of 2)
    distances = np.sort(distances[np.triu_indices(3, k=1)])
    return np.array_equal(distances, [1, 1, 2])

def create_frame(grid, color):
  height = 0
  width = 0

  # get height and width
  for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
      if grid[r,c] != 0:
        height += 1
        break
  for c in range(grid.shape[1]):
    for r in range(grid.shape[0]):
      if grid[r,c] != 0:
        width += 1
        break

  output_grid = np.zeros((height, width), dtype=int)
  for r in range(height):
    for c in range(width):
      if r == 0 or r == height - 1 or c == 0 or c == width - 1:
          output_grid[r,c] = color
  return output_grid

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    objects = find_objects(input_grid)
    output_grid = None
    frame_color = None

    # Find Frame Object and its dimensions
    for color, pixels in objects:
        # Find leftmost non-zero pixel, and its color
        min_col = min(p[1] for p in pixels)
        if all(p[1] >= min_col for p in pixels):
          frame_color = color
          output_grid = create_frame(input_grid, frame_color)
          break;

    if output_grid is None:
      output_grid = np.zeros((5,5), dtype=int) #default if not found
      # raise Exception("No framing object found")

    center_r = output_grid.shape[0] // 2
    center_c = output_grid.shape[1] // 2

    # change output pixels
    for color, pixels in objects:
        if is_l_shape(pixels):
            if color == 8:  # Azure
                output_grid[center_r-1:center_r+1, center_c-1:center_c+1] = 8
            elif color == 1:  # Blue
                output_grid[center_r-1:center_r+1, center_c-1:center_c+1] = 1
            elif color == 4:  # Yellow
              # Clear Center, then add the cross
              output_grid[center_r-1:center_r+2, center_c-1:center_c+2] = 4
              output_grid[center_r,center_c] = 0


    return output_grid