"""
1.  **Identify the Topmost Object:** Find the topmost row that contains any non-zero pixels. Identify the contiguous "object" in this row, regardless of the colors of the pixels. An object is a group of adjacent pixels above other pixels.

2.  **Shift Up:** Shift the top row of pixels in the object up by one row.

3. **Repeat** Shift the next row of the object until the entire object has been moved up.

4.  **Boundary Condition:** If the object is already at the very top of the grid (row 0), do not shift it.

5. Preserve input pixels.
"""

import numpy as np

def find_topmost_object(grid):
    """Finds the topmost contiguous object in the grid, regardless of color."""
    rows, cols = grid.shape
    topmost_row = -1
    
    # Find the highest row with any non-zero pixels
    for r in range(rows):
        if np.any(grid[r] != 0):
            topmost_row = r
            break

    if topmost_row == -1:
        return []

    object_pixels = []
    visited = set()

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    def dfs(row, col):
        if (row, col) in visited or not is_valid(row, col) or grid[row, col] == 0:
            return
        visited.add((row, col))
        object_pixels.append((row, col))

        # Explore adjacent cells (up, down, left, right)
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    #find a starting pixel in topmost_row
    for start_col in range(cols):
      if grid[topmost_row, start_col] != 0:
        dfs(topmost_row, start_col)
        break #we only want one object

    return object_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the top-most object
    topmost_object = find_topmost_object(input_grid)

    if not topmost_object:
      return output_grid
    
    #sort object pixels by row so we process from top down
    topmost_object.sort()

    # shift each row of object up one at a time
    moved_pixels = set()
    for r, c in topmost_object:
        if (r,c) in moved_pixels:
            continue
    
        color = output_grid[r,c]
        output_grid[r, c] = 0  # Clear the original cell

        new_r = r - 1
        if new_r >= 0:
          output_grid[new_r,c] = color
          moved_pixels.add((new_r,c))
        else:
            #add back to original if at the top edge
            output_grid[r,c] = color
            moved_pixels.add((r,c))


    return output_grid