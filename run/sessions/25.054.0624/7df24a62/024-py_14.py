"""
1.  **Identify Objects:** Find all contiguous regions (objects) of the same color in the input grid.

2.  **Object Interaction - Yellow and Blue:**
    * If a yellow object is directly adjacent (up, down, left, or right, but *not* diagonally) to any pixel of a blue object, change all pixels in the *entire* yellow object to blue in the output grid.
    * If there is a blue region and a yellow region is directly to the left of the blue region, generate new blue pixels that extend to the left of the blue, and aligned with the rows of the yellow object. The existing yellow pixels are removed.
    * If there is a blue region and a yellow region is directly above the blue region, generate new blue pixels that extend above of the blue, aligned with the columns of the yellow object. The existing yellow pixels are removed.

3.  **Preserve Existing Blue:** Existing blue objects remain blue, and the new adjacent regions.

4. **Other Colors:** If a pixel is not adjacent to a blue object, then it stays as its original color.

5.  **Background:** All pixels that are not affected by an interaction rule will become or remain background/black (0).
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous regions of the same color."""
    objects = {}
    visited = set()
    rows, cols = grid.shape

    def dfs(r, c, color, current_object):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, color, current_object)
        dfs(r - 1, c, color, current_object)
        dfs(r, c + 1, color, current_object)
        dfs(r, c - 1, color, current_object)

    for r in range(rows):
        for c in range(cols):
            color = grid[r, c]
            if (r, c) not in visited:
                current_object = []
                dfs(r, c, color, current_object)
                if color not in objects:
                    objects[color] = []
                objects[color].append(current_object)
    return objects

def is_adjacent(object1, object2):
    """Checks if two objects are directly adjacent (not diagonally)."""
    for r1, c1 in object1:
        for r2, c2 in object2:
            if (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2):
                return True
    return False

def transform(input_grid):
    # initialize output_grid as a copy of input
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all objects
    objects = find_objects(input_grid)

    # Handle Yellow and Blue interactions
    if 1 in objects and 4 in objects:  # If both blue and yellow exist
        blue_objects = objects[1]
        yellow_objects = objects[4]

        for yellow_obj in yellow_objects:
            adjacent_to_blue = False
            for blue_obj in blue_objects:
                if is_adjacent(yellow_obj, blue_obj):
                    # Change all yellow pixels in the object to blue
                    for r, c in yellow_obj:
                        output_grid[r, c] = 1
                    adjacent_to_blue = True
                    break  # Move to the next yellow object

            if not adjacent_to_blue:
                #check for expansion cases
                for blue_obj in blue_objects:
                    #check left expansion
                    leftmost_yellow_col = min(c for r,c in yellow_obj)
                    rightmost_blue_col = max(c for r, c in blue_obj)

                    if rightmost_blue_col + 1 == leftmost_yellow_col:
                        #rows match
                        yellow_rows = set(r for r,c in yellow_obj)
                        blue_rows = set(r for r,c in blue_obj)
                        
                        
                        if yellow_rows.issubset(blue_rows):
                          #expansion
                          for r,c in yellow_obj:
                              output_grid[r,c] = 0 #remove existing
                          for r in yellow_rows:
                              if r >= 0 and r < rows and rightmost_blue_col >= 0 and rightmost_blue_col < cols:
                                output_grid[r,rightmost_blue_col] = 1

                    #check above expansion
                    topmost_yellow_row = min(r for r,c in yellow_obj)
                    bottommost_blue_row = max(r for r,c in blue_obj)

                    if bottommost_blue_row + 1 == topmost_yellow_row:
                        #columns must match
                        yellow_cols = set(c for r,c in yellow_obj)
                        blue_cols = set(c for r,c in blue_obj)

                        if yellow_cols.issubset(blue_cols):
                            for r,c in yellow_obj:
                                output_grid[r,c] = 0
                            for c in yellow_cols:
                              if bottommost_blue_row >= 0 and bottommost_blue_row < rows and c >=0 and c < cols:
                                output_grid[bottommost_blue_row, c] = 1

    #handle pixels not near blue
    for r in range(rows):
        for c in range(cols):
            if output_grid[r,c] != 1:
                #check for adjacent blue pixel
                adjacent_blue = False
                if r - 1 >= 0 and output_grid[r-1,c] == 1:
                    adjacent_blue = True
                if r + 1 < rows and output_grid[r+1, c] == 1:
                    adjacent_blue = True
                if c - 1 >= 0 and output_grid[r, c-1] == 1:
                    adjacent_blue = True
                if c + 1 < cols and output_grid[r, c+1] == 1:
                    adjacent_blue = True
                if not adjacent_blue and input_grid[r,c] != 1:
                    output_grid[r,c] = input_grid[r,c]
                
    return output_grid