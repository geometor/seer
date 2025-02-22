import numpy as np

def is_l_shape(grid, x, y, color):
    """
    Checks if a pixel at (x, y) is part of an L-shape of the specified color.
    An L-shape is defined as a 2x2 area with one missing block.
    """
    if grid[x][y] != color:
        return False

    neighbors = 0
    coords = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx][ny] == color:
                neighbors += 1
                coords.append((nx,ny))

    if neighbors == 2:
          coords.append((x,y))
          return coords
    else:
        return False
    

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    output_grid = np.copy(input_grid)
    l_shapes = []
    
    for x in range(input_grid.shape[0]):
        for y in range(input_grid.shape[1]):
          result = is_l_shape(input_grid, x, y, 8)
          if result:
            l_shapes.append(result)

    # iterate by l_shapes found
    if len(l_shapes) > 0:
        for shape in l_shapes:
          # Find the right-most and bottom-most pixels in the L-shape.
          rightmost_pixel = max(shape, key=lambda p: p[1])
          bottommost_pixel = max(shape, key=lambda p: p[0])

          # Determine which pixel to change based on the shape
          if rightmost_pixel[0] < bottommost_pixel[0]: # check x coordinates to know the figure position
              #if the rightmost is first, replace it
              output_grid[rightmost_pixel] = 1
          else:
              #if bottom is first or at the same level, change it
              output_grid[bottommost_pixel] = 1

    return output_grid