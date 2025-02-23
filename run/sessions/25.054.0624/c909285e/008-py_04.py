"""
1.  **Identify the Target Region:** Locate the largest rectangular region within the input grid that is completely enclosed by a continuous border of pixels with the value '2' (red).

2.  **Extract Sub-grid:** Extract this framed region from the input grid.

3. **Return extracted sub-grid**: The output is exactly equal to the extracted sub-grid, with no changes to colors, dimensions, or values.
"""

import numpy as np

def find_framed_region(grid, frame_color=2):
    """Finds the largest rectangular region enclosed by a frame of the specified color."""
    rows, cols = grid.shape
    top_left = None
    bottom_right = None

    # Find top-left corner of frame
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == frame_color:
                # Check if this is a valid top-left corner
                if (c + 1 < cols and grid[r, c+1] == frame_color) or (r + 1 < rows and grid[r+1,c] == frame_color):
                    top_left = (r, c)
                    break
        if top_left:
            break
    
    if not top_left:
        return None, None

    # Find bottom-right corner
    r = top_left[0]
    c = top_left[1]
    
    # get width
    while c < cols and grid[r,c] == frame_color:
      c += 1
    width = c - top_left[1]

    #get height
    c = top_left[1]
    while r < rows and grid[r, c] == frame_color:
        r += 1
    height = r - top_left[0]  
    
    bottom_right = (top_left[0] + height -1, top_left[1] + width -1 )

    #check full frame is valid
    for i in range(top_left[1], bottom_right[1] + 1):
        if not (grid[top_left[0], i] == frame_color and grid[bottom_right[0],i] == frame_color):
            return None, None
    for i in range(top_left[0], bottom_right[0] + 1):
      if not (grid[i, top_left[1]] == frame_color and grid[i, bottom_right[1]] == frame_color ):
          return None, None
    
    return top_left, (bottom_right[0], bottom_right[1] )


def transform(input_grid):
    """Extracts the rectangular region enclosed by a red (2) frame."""
    # Convert to numpy array
    grid = np.array(input_grid)

    # Find the framed region
    top_left, bottom_right = find_framed_region(grid)

    # Extract the sub-grid
    if top_left and bottom_right:
        output_grid = grid[top_left[0]:bottom_right[0]+1, top_left[1]:bottom_right[1]+1].tolist()
    else:
        output_grid = []  # Return an empty grid if no framed region is found

    return output_grid