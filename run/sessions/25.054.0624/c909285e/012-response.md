# c909285e • 012 • refine_coder

---
```python
"""
1.  **Identify Potential Frames:** Examine the input grid and identify potential frame colors by considering colors on the edges and large contiguous blocks.
2.  **Prioritize Single-Color Frames:** Check for frames consisting of a single color. If found, proceed with extracting the inner region.
3.  **Handle Multi-Color Frames:** If no single-color frame is found, look for frames composed of multiple colors but with consistent boundaries.  Prioritize frames that completely enclose another region.
4.  **Extract Inner Region:** Once a suitable frame is identified (either single-color or multi-color), extract the region enclosed by the frame.
5.  **Return Sub-grid:** Return the extracted sub-grid. If no suitable frame is found, return an empty grid.
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

def find_single_color_frame(grid, frame_color):
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
    
    return top_left, bottom_right

def extract_inner_region(grid, top_left, bottom_right):
    """Extracts the inner region defined by the frame corners."""
    if top_left is None or bottom_right is None:
        return []

    inner_top_left = (top_left[0] + 1, top_left[1] + 1)
    inner_bottom_right = (bottom_right[0] - 1, bottom_right[1] - 1)

    if inner_top_left[0] > inner_bottom_right[0] or inner_top_left[1] > inner_bottom_right[1]:
      return []

    return grid[inner_top_left[0]:inner_bottom_right[0]+1, inner_top_left[1]:inner_bottom_right[1]+1].tolist()


def transform(input_grid):
    """Extracts the rectangular region enclosed by a dynamically determined frame, prioritizing single-color frames."""
    grid = np.array(input_grid)
    perimeter_colors = get_perimeter_colors(grid)
    
    # Prioritize single-color frames
    for frame_color in perimeter_colors:
        top_left, bottom_right = find_single_color_frame(grid, frame_color)
        if top_left:
          output_grid = extract_inner_region(grid,top_left, bottom_right)
          return output_grid

    #if we get here, there is no good single color frame
    return []
```
