# 2-0ca9ddb6 • 010 • example_2 - CODE

---
```python
"""
1.  **Initialization:** Start with the input grid.
2.  **Iteration:** Iterate through all possible *pairs* of non-white pixels in the input grid.
3.  **Distance Check**: If two non-white pixels are exactly 3 cells apart, horizontally, vertically, or diagonally (Manhattan distance == 3)
4.  **Color Creation:*** Place two yellow pixels. One to the left and one to the right, or one above and one below relative to the original pair.
5. **Orange Filling** Fill the three by three area including the original pair with orange (7).
6.  **Preservation:** Any non-white pixels from the input grid that *do not* participate in a 3-distance relationship with another pixel, are copied to the output grid unchanged.
"""

import numpy as np

def get_non_white_pixels(grid):
    """Finds coordinates of non-white pixels."""
    rows, cols = np.where(grid != 0)
    return list(zip(rows, cols))

def manhattan_distance(p1, p2):
    """Calculates Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    non_white_pixels = get_non_white_pixels(input_grid)

    # iterate pairs of non-white pixels
    processed_pixels = set()
    for i in range(len(non_white_pixels)):
      for j in range(i + 1, len(non_white_pixels)):
        p1 = non_white_pixels[i]
        p2 = non_white_pixels[j]

        if manhattan_distance(p1,p2) == 3:
            #Color Creation.  
            
            #horizontal
            if (p1[0] == p2[0]):
              output_grid[p1[0], min(p1[1],p2[1])-1] = 4
              output_grid[p1[0], max(p1[1],p2[1])+1] = 4
            #vertical
            if (p1[1] == p2[1]):
              output_grid[min(p1[0],p2[0])-1, p1[1]] = 4
              output_grid[max(p1[0],p2[0])+1, p1[1]] = 4
            
            # fill a 3x3 box with orange around the two pixels
            min_row = min(p1[0], p2[0])
            max_row = max(p1[0], p2[0])
            min_col = min(p1[1], p2[1])
            max_col = max(p1[1], p2[1])

            for row in range(min_row -1, max_row + 2):
              for col in range(min_col - 1, max_col + 2):
                if 0 <= row < output_grid.shape[0] and 0<= col < output_grid.shape[1]:
                    output_grid[row,col] = 7
            
            processed_pixels.add(p1)
            processed_pixels.add(p2)


    # preservation of other non-white pixels
    for p in non_white_pixels:
        if p not in processed_pixels:
            output_grid[p] = input_grid[p]
            

    return output_grid
```
