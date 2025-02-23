# c909285e • 010 • refine_coder

---
```python
"""
1.  **Identify Potential Frame:** Inspect the input grid and identify potential frame colors by looking at pixels at the edges, checking for the largest contiguous blocks of the same color.

2.  **Determine Frame Color:** If a frame color is found, determine the frame color. If more than one exists, analyze inside each frame and select the frame that completely contains another object.

3. **Locate Inner Object:** Locate the largest rectangular object contained completely within the frame.

4.  **Extract Sub-grid:** Extract the inner object (rectangle) from the input grid.

5.  **Return Sub-grid:** Return the extracted sub-grid. If no frame is found or if the frame does not contain a complete rectangular object, return an empty grid.
"""

import numpy as np

def get_perimeter_colors(grid):
    """Gets the colors present on the perimeter of the grid."""
    rows, cols = grid.shape
    perimeter_colors = set()

    # Top and bottom rows
    for c in range(cols):
        perimeter_colors.add(grid[0, c])
        perimeter_colors.add(grid[rows - 1, c])

    # Left and right columns (excluding corners)
    for r in range(1, rows - 1):
        perimeter_colors.add(grid[r, 0])
        perimeter_colors.add(grid[r, cols - 1])

    return list(perimeter_colors)

def find_framed_region(grid, frame_color):
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

def find_inner_rectangle(grid, top_left, bottom_right):
    """Finds the largest rectangle inside the frame."""
    
    if not top_left:
        return None
    
    inner_top_left = (top_left[0] + 1, top_left[1] + 1)
    inner_bottom_right = (bottom_right[0] - 1, bottom_right[1] -1)

    #check not out of bounds
    if inner_top_left[0] > inner_bottom_right[0] or inner_top_left[1] > inner_bottom_right[1]:
        return None
    
    return inner_top_left, inner_bottom_right

def transform(input_grid):
    """Extracts the rectangular region enclosed by a dynamically determined frame."""
    grid = np.array(input_grid)
    perimeter_colors = get_perimeter_colors(grid)
    
    best_frame_color = None
    best_top_left = None
    best_bottom_right = None
    
    for frame_color in perimeter_colors:
        top_left, bottom_right = find_framed_region(grid, frame_color)
        inner_top_left, inner_bottom_right = find_inner_rectangle(grid, top_left, bottom_right)

        if inner_top_left: # frame and inner object exist

            if best_top_left is None: #first found
                best_frame_color = frame_color
                best_top_left = top_left
                best_bottom_right = bottom_right
            else:
                # compare areas
                current_area = (inner_bottom_right[0] - inner_top_left[0] + 1) * (inner_bottom_right[1] - inner_top_left[1] + 1)
                best_area = (best_bottom_right[0] - best_top_left[0] -1 ) * (best_bottom_right[1] - best_top_left[1] - 1)
                if current_area > best_area:
                    best_frame_color = frame_color
                    best_top_left = top_left
                    best_bottom_right = bottom_right

    if best_top_left:
        inner_top_left, inner_bottom_right = find_inner_rectangle(grid, best_top_left, best_bottom_right)
        output_grid = grid[inner_top_left[0]:inner_bottom_right[0]+1, inner_top_left[1]:inner_bottom_right[1]+1].tolist()
    else:
      output_grid = []

    return output_grid
```
