# 7df24a62 • 020 • example_4 • investigate_coder

---
```python
"""
1.  **Identify Existing Objects:** Locate the existing 3x3 blue square and all yellow pixels in the input grid.

2.  **Yellow Pixel Interaction:**
    *   If a yellow pixel is directly adjacent (up, down, left, or right, but not diagonally) to any pixel of the existing 3x3 blue square, change that yellow pixel to blue in the output.
    *   If a yellow pixel is not adjacent to the existing blue square, there are two cases. First, consider expansion of yellow to blue in proximity of existing blue:
        * if yellow is immediately to the left of existing blue, new blue is generated to the immediate left of existing yellow.
        * if yellow is immediately above existing blue, new blue is generated one position above existing yellow
    * else, if yellow is not one of the above cases, keep it as black/background (0) in the output.

3. **Preserve Existing Blue:** Maintain the original 3x3 blue square in its original position in the output.

4.  **Background:** All other pixels that are not part of the identified objects or changed by the interaction rules remain black/background (0).

"""

import numpy as np

def find_objects(grid, color):
    """Finds contiguous regions of the specified color."""
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, current_object):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def is_adjacent(pixel, blue_square):
    """Checks if a pixel is adjacent to any pixel in the blue square."""
    r, c = pixel
    for br, bc in blue_square:
        if (abs(r - br) == 1 and c == bc) or (abs(c - bc) == 1 and r == br):
            return True
    return False

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the 3x3 blue square and yellow pixel locations.
    blue_objects = find_objects(input_grid, 1)
    blue_square = None
    
    #find blue square object
    for obj in blue_objects:
        if len(obj) == 9:
            is_square = True
            rows = set()
            cols = set()
            for r,c in obj:
                rows.add(r)
                cols.add(c)
            if len(rows) == 3 and len(cols) == 3:
                row_vals = sorted(list(rows))
                col_vals = sorted(list(cols))
                #check continuous
                if row_vals[0] + 1 == row_vals[1] and row_vals[1] + 1 == row_vals[2]:
                  if col_vals[0] + 1 == col_vals[1] and col_vals[1] + 1 == col_vals[2]:
                    blue_square = obj
                    break
    if blue_square is None:
        #handle no blue square case - just return input grid
        return output_grid
        

    yellow_pixels = []
    rows, cols = input_grid.shape
    for r in range(rows):
      for c in range(cols):
        if input_grid[r,c] == 4:
          yellow_pixels.append((r,c))

    # Iterate through yellow pixels and apply interaction rules.
    for r, c in yellow_pixels:
        if is_adjacent((r, c), blue_square):
            output_grid[r, c] = 1  # Change yellow to blue
        else:
            #check for yellow to left of blue
            found_blue_right = False
            for br, bc in blue_square:
                if r == br and c + 1 == bc:
                  output_grid[r,c] = 0
                  if r >= 0 and r < rows and c - 1 >= 0 and c - 1 < cols:
                    output_grid[r, c-1] = 1
                    found_blue_right = True
                    break
            if not found_blue_right:
                #check yellow above blue
                found_blue_below = False
                for br, bc in blue_square:
                  if r + 1 == br and c == bc:
                    output_grid[r,c] = 0
                    if r - 1 >= 0 and r - 1 < rows and c >= 0 and c < cols:
                      output_grid[r-1,c] = 1
                      found_blue_below = True
                      break
                if not found_blue_below:
                  output_grid[r,c] = 0 #set all others to zero

    return output_grid
```
