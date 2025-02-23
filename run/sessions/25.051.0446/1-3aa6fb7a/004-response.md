# 1-3aa6fb7a • 004 • example_2 - CODE

---
```python
"""
The L shapes of azure color are kept, and in each "corner" a blue pixel is created, inside the L-shape, at a Manhattan distance of 1 of the meeting of the two segments of the L.
"""

import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specified color in the grid.
    Returns a list of dictionaries, each containing the 'elbow' and 'leg' coordinates.
    """
    l_shapes = []
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_l):
        visited[r, c] = True
        current_l.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            if is_valid(nr, nc) and not visited[nr, nc] and grid[nr, nc] == color:
                dfs(nr, nc, current_l)
    
    # Find the first point of the L.
    for r in range(rows):
        for c in range(cols):
            if grid[r,c] == color and not visited[r,c]:
                current_l = []
                dfs(r,c,current_l)
                
                # Check if this forms the L.
                if len(current_l) == 3:
                  # determine elbow.
                  elbow_candidates = []
                  for r_test,c_test in current_l:
                    count = 0
                    neighbors = [(r_test - 1, c_test), (r_test + 1, c_test), (r_test, c_test - 1), (r_test, c_test + 1)]
                    for nr, nc in neighbors:
                      if (nr,nc) in current_l:
                        count += 1
                    if count == 2:
                      elbow_candidates.append((r_test,c_test))

                  if len(elbow_candidates) == 1:
                    l_shapes.append({"elbow": elbow_candidates[0], "legs": current_l})

    return l_shapes

def transform(input_grid):
    """
    Transforms the input grid according to the rule:
    Keep the L shapes of azure color, and in each "corner" a blue pixel is created,
    inside the L-shape, at a Manhattan distance of 1 of the meeting of the two segments.
    """
    output_grid = np.copy(input_grid)
    azure = 8
    blue = 1

    l_shapes = find_l_shapes(input_grid, azure)

    for l_shape in l_shapes:
        elbow_row, elbow_col = l_shape['elbow']
        
        #find insertion points:
        insertion_points = []
        for leg_row, leg_col in l_shape["legs"]:
          if (leg_row,leg_col) != (elbow_row,elbow_col):
            insertion_points.append((leg_row,leg_col))
        
        # insert points
        for ins_row, ins_col in insertion_points:
          output_grid[ins_row,ins_col] = blue

    return output_grid
```

