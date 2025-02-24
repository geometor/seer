"""
1.  **Identify the Blue Frame:** Locate the outermost rectangular frame of blue (1) pixels within the input grid. This frame may or may not be a complete rectangle, but its corners can always be identified.
2.  **Locate Corners:** Determine the row and column coordinates of the top-left, top-right, bottom-left, and bottom-right corners of this blue frame.
3.  **Extract Adjacent Colors:** For each corner of the blue frame, find the color of the *directly* adjacent pixel *outside* the frame:
    *   Top-left corner:  Pixel above and to the left.
    *   Top-right corner: Pixel above and to the right.
    *   Bottom-left corner: Pixel below and to the left.
    *   Bottom-right corner: Pixel below and to the right.
    *   If a corner is at the edge of the input grid and has no adjacent pixel in the specified direction, use the color black (0).
4.  **Create 2x2 Output Grid:** Create a new 2x2 grid.
5.  **Populate Output Quadrants:** Fill each quadrant of the 2x2 output grid with the adjacent colors obtained in step 3:
    *   Top-left quadrant: Color adjacent to the top-left corner of the blue frame.
    *   Top-right quadrant: Color adjacent to the top-right corner of the blue frame.
    *   Bottom-left quadrant: Color adjacent to the bottom-left corner of the blue frame.
    *   Bottom-right quadrant: Color adjacent to the bottom-right corner of the blue frame.
"""

import numpy as np

def get_frame_boundaries(grid):
    # Find the outermost blue (1) frame.
    rows, cols = grid.shape
    top_left = None
    top_right = None
    bottom_left = None
    bottom_right = None

    # Find top-left
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == 1:
                top_left = (r,c)
                break
        if top_left:
            break

    #Find other coners based on knowledge that it is rectangular and 1 pixel wide
    if top_left:
      for r in range(rows):
        for c in range(cols):
          if grid[r,c] == 1:
            if r == top_left[0] and c > top_left[1]:
                top_right = (r,c)
            if c == top_left[1] and r > top_left[0]:
                bottom_left = (r, c)
            if bottom_left and top_right and r > top_left[0] and c > top_left[1] and grid[r, c] ==1:
                bottom_right = (r, c)
    return top_left, top_right, bottom_left, bottom_right

def get_adjacent_color(grid, coord, direction):
    # Get the color of the pixel *directly* adjacent to the given coordinate.
    rows, cols = grid.shape
    r, c = coord

    if direction == 'top_left':
        new_r, new_c = r - 1, c - 1
    elif direction == 'top_right':
        new_r, new_c = r - 1, c + 1
    elif direction == 'bottom_left':
        new_r, new_c = r + 1, c - 1
    elif direction == 'bottom_right':
        new_r, new_c = r + 1, c + 1
    else:
        return 0  # Should not happen
    
    # check direct adjacency above, below, left and right
    if direction == 'top_left':
      if r > 0 and grid[r-1,c] != 1:
          return grid[r-1, c]
      elif c > 0 and grid[r, c-1] != 1:
          return grid[r, c-1]
    elif direction == 'top_right':
      if r > 0 and grid[r-1, c] != 1:
        return grid[r-1, c]
      elif c < cols -1 and grid[r, c+1] != 1:
        return grid[r, c+1]
    elif direction == 'bottom_left':
      if r < rows - 1 and grid[r + 1, c] != 1:
        return grid[r+1, c]
      elif c > 0 and grid[r, c-1] != 1:
        return grid[r, c-1]
    elif direction == 'bottom_right':
      if r < rows -1 and grid[r+1,c] != 1:
        return grid[r+1, c]
      elif c < cols - 1 and grid[r, c+1] != 1:
        return grid[r, c+1]


    if 0 <= new_r < rows and 0 <= new_c < cols:
        if grid[new_r, new_c] != 1:
          return grid[new_r, new_c]
        else: return 0
    else:
        return 0  # Default to black (0) if out of bounds

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""

    # Find the blue frame boundaries
    top_left, top_right, bottom_left, bottom_right = get_frame_boundaries(input_grid)

    # Handle cases where no blue frame is found
    if not all([top_left, top_right, bottom_left, bottom_right]):
        return np.zeros((2, 2), dtype=int)  # Return a 2x2 grid with 0s

    # Extract adjacent colors from input, handling boundary conditions
    corner_colors = {
        'top_left': get_adjacent_color(input_grid, top_left, 'top_left'),
        'top_right': get_adjacent_color(input_grid, top_right, 'top_right'),
        'bottom_left': get_adjacent_color(input_grid, bottom_left, 'bottom_left'),
        'bottom_right': get_adjacent_color(input_grid, bottom_right, 'bottom_right')
    }

    # Create a 2x2 output grid
    output_grid = np.array([
        [corner_colors['top_left'], corner_colors['top_right']],
        [corner_colors['bottom_left'], corner_colors['bottom_right']]
    ], dtype=int)
    
    return output_grid