# db3e9e38 • 006 • refine_coder

---
```python
"""
1.  **Identify Object:** Locate the isolated vertical line of orange (7) pixels. An isolated line means that no other orange pixels are directly adjacent to it, either vertically or horizontally.
2.  **Store Initial Position:** Record the row and column indices of each pixel in the orange line.
3.  **Shift:** Move the original orange (7) line upwards by one pixel. If the line is already at the top, parts will disappear off the edge.
4. **Store Final and Combined Positions** Record the row and column indices of the *new* position of the vertical line. Combine both positions for use when drawing the frame
5.  **Frame:** Create a single-pixel thick frame of azure (8) that surrounds both the initial *and* final positions of the orange line.
"""

import numpy as np

def find_vertical_line(grid, color):
    rows, cols = grid.shape
    for c in range(cols):
        for r in range(rows):
            if grid[r, c] == color:
                # Check if it's a vertical line
                start_row = r
                end_row = r
                while end_row + 1 < rows and grid[end_row + 1, c] == color:
                    end_row += 1
                
                # verify that it is isolated
                if (start_row == 0 or grid[start_row-1,c] != color) and \
                 (end_row == rows-1 or grid[end_row+1, c] != color):

                  # if it's not isolated on the sides, return none
                  if (c > 0 and grid[start_row:end_row+1, c-1].any() == color) or \
                     (c < cols -1 and grid[start_row:end_row+1, c+1].any() == color):
                      return None, None, None
                  
                  return c, start_row, end_row
    return None, None, None

def get_positions(col, start_row, end_row):
    # return positions of pixels in a vertical line
    positions = []
    for r in range(start_row, end_row + 1):
        positions.append((r, col))
    return positions

def shift_positions(positions, shift_amount, rows):
    # shift the positions up
    shifted_positions = []
    for r, c in positions:
        new_r = max(0, r + shift_amount) # Ensure we don't go out of bounds
        shifted_positions.append((new_r,c))
    return shifted_positions
    

def add_frame(grid, positions, frame_color):
    # create a combined set of initial and final positions
    rows, cols = grid.shape
    
    # Add frame around combined positions
    for r, c in positions:
      # frame above
      if r-1 >= 0:
        grid[r - 1, c] = frame_color

      # frame below
      if r+1 < rows:
        grid[r + 1, c] = frame_color
      
      # frame to the left
      if c-1 >= 0:
          grid[r,c-1] = frame_color
      
      # frame to the right
      if c+1 < cols:
          grid[r,c+1] = frame_color

      # frame to top left
      if r-1 >= 0 and c-1 >= 0:
        grid[r-1,c-1] = frame_color

      # frame to top right
      if r-1 >= 0 and c+1 < cols:
        grid[r-1, c+1] = frame_color
      
      # frame to bottom left
      if r+1 < rows and c-1 >= 0:
        grid[r+1, c-1] = frame_color
      
      # frame to bottom right
      if r+1 < rows and c+1 < cols:
          grid[r+1, c+1] = frame_color
    return grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find the vertical line of orange (7) pixels
    col, start_row, end_row = find_vertical_line(output_grid, 7)

    if col is not None:
        # Store initial position
        initial_positions = get_positions(col, start_row, end_row)

        # Shift the line and store new position (-1 for up)
        shifted_positions = shift_positions(initial_positions, -1, rows)
        
        # clear original positions
        for r,c in initial_positions:
          output_grid[r,c] = 0

        # set shifted positions
        for r,c in shifted_positions:
          output_grid[r,c] = 7
        
        # combine positions
        combined_positions = list(set(initial_positions + shifted_positions))

        # Create a frame of azure (8) around the combined positions
        output_grid = add_frame(output_grid, combined_positions, 8)

    return output_grid
```
