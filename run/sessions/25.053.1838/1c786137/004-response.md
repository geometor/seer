# 1c786137 • 004 • refine_coder

---
```python
"""
1.  **Identify the Bordered Region:** Within the input grid, find a contiguous region of any shape that is completely enclosed by a border of black (color 0) pixels.  The border must be one pixel thick.
2.  **Define Interior:** The "interior" is all pixels *inside* the border, regardless of their color.
3.  **Extract Interior:** Create a new, smaller grid consisting *only* of the pixels within the identified bordered region.  Exclude the black border pixels.
4. **Output:** The new grid from step 3 is the output.
"""

import numpy as np

def find_interior(grid, border_color=0):
    """Finds the interior pixels of a bordered region."""
    rows, cols = grid.shape
    interior_mask = np.zeros_like(grid, dtype=bool)
    
    # Use a flood fill algorithm to find the interior.
    # Start from every border, mark all connected non-border pixels

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def flood_fill(r, c):
          if not is_valid(r,c) or grid[r, c] == border_color or interior_mask[r,c] == True:
                return
          
          interior_mask[r,c] = True
          
          flood_fill(r+1,c)
          flood_fill(r-1,c)
          flood_fill(r,c+1)
          flood_fill(r,c-1)

    # Find top-left of object
    border_found = False
    for r in range(rows):
      for c in range(cols):
          if grid[r,c] == border_color:
            start_row = r
            start_col = c
            border_found = True
            break
      if border_found:
        break
    
    # find inside point of object
    inside_row = -1
    inside_col = -1
    for r in range(start_row+1,rows):
        if grid[r, start_col] != border_color:
            inside_row = r
            inside_col = start_col
            break
    if inside_row == -1:
        return interior_mask #return all false - no interior found

    #Flood fill from inside point
    flood_fill(inside_row, inside_col)

    return interior_mask
    


def transform(input_grid):
    """Transforms the input grid by extracting the region within a bordered region."""
    input_grid = np.array(input_grid)
    
    # Find the interior pixels using the flood fill approach.
    interior_mask = find_interior(input_grid)

    # Extract the interior region based on the mask.
    rows, cols = np.where(interior_mask)
    
    if len(rows) == 0: #no interior, return empty grid
        return []
    
    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    output_grid = input_grid[min_row:max_row+1, min_col:max_col+1]

    return output_grid.tolist()
```
