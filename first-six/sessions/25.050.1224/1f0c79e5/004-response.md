# 1f0c79e5 • 004 • example_2 - CODE

---
```python
"""
The transformation rule can be summarized as follows:

1. Identify the "L" shaped object (either yellow or green in the examples) and a single-celled red object.
2. Remove the red cell.
3. Expand the "L" shaped object into a 5x5 tilted square. The direction of the tilt depends on the initial orientation of the "L":
   - If the "L" points down and right (yellow example), the expansion is upwards and leftwards, forming a tilted square missing the bottom-right 3x3 area.
   - If the "L" points up and right (green example), the expansion is downwards and rightwards, forming a tilted square missing the top-left 3x3 area.
   The top-left or bottom-right corner of the incomplete tilted square corresponds to the corner cell of the initial L-shape.

"""

import numpy as np

def find_object(grid, color):
    """Finds coordinates of cells with a specific color."""
    coords = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == color:
                coords.append((r, c))
    return coords

def detect_l_shape(coords):
    """Detects if the given coordinates form an L-shape and determines its orientation."""
    if len(coords) != 3:
        return None  # Not an L-shape

    # Convert to numpy array for easier calculations
    coords = np.array(coords)

    # Calculate differences between coordinates
    diffs = np.diff(coords, axis=0)

    # Check if it's an L-shape
    if (np.all(diffs[0] == [0, 1]) and np.all(diffs[1] == [1, 0])) or \
       (np.all(diffs[0] == [1, 0]) and np.all(diffs[1] == [0, 1])) :
      # case 1:  _|_  
      return 'down_right', coords[0]
    elif (np.all(diffs[0] == [0, 1]) and np.all(diffs[1] == [-1, 0])) or \
       (np.all(diffs[0] == [-1, 0]) and np.all(diffs[1] == [0, 1])) :
      # case 2:   _|  
      return 'down_left',  coords[0] if  (np.all(diffs[0] == [0, 1])) else coords[1]
    elif (np.all(diffs[0] == [0, -1]) and np.all(diffs[1] == [-1, 0])) or \
       (np.all(diffs[0] == [-1, 0]) and np.all(diffs[1] == [0, -1])) :
       # case 3: |_
       return 'up_left', coords[0] if  (np.all(diffs[0] == [0, -1])) else coords[1]
    elif (np.all(diffs[0] == [0, -1]) and np.all(diffs[1] == [1, 0])) or \
       (np.all(diffs[0] == [1, 0]) and np.all(diffs[1] == [0, -1])) :
       # case 4:  -|
       return 'up_right',  coords[1] if  (np.all(diffs[0] == [1, 0])) else coords[0]
    else:
      # sorting coords to handle different input L orders
      coords = sorted(coords, key=lambda x: (x[0],x[1]))
      coords = np.array(coords)
      diffs = np.diff(coords, axis=0)
      if (np.all(diffs[0] == [1, 0]) and np.all(diffs[1] == [0, 1])) or \
         (np.all(diffs[0] == [0, 1]) and np.all(diffs[1] == [1, 0])) :
        # case 1:  _|_  
        return 'down_right', coords[0]
      elif (np.all(diffs[0] == [0, 1]) and np.all(diffs[1] == [-1, 0])) or \
        (np.all(diffs[0] == [-1, 0]) and np.all(diffs[1] == [0, 1])) :
        # case 2:   _|
        return 'down_left', coords[0] if (np.all(diffs[0] == [-1, 0])) else coords[2]
      elif (np.all(diffs[0] == [0, -1]) and np.all(diffs[1] == [-1, 0])) or \
        (np.all(diffs[0] == [-1, 0]) and np.all(diffs[1] == [0, -1])) :
        # case 3: |_
        return 'up_left',  coords[0] if (np.all(diffs[0] == [-1, 0])) else coords[2]
      elif (np.all(diffs[0] == [1, 0]) and np.all(diffs[1] == [0, -1])) or \
         (np.all(diffs[0] == [0, -1]) and np.all(diffs[1] == [1, 0])) :
        # case 4:  -|
        return 'up_right', coords[0]
    
    return None

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Objects and their properties
    l_colors = []
    for color in range(10):
      l_coords = find_object(input_grid, color)
      l_shape = detect_l_shape(l_coords)
      if l_shape != None:
        l_colors.append((color, l_shape))

    red_coords = find_object(input_grid, 2)

    # 2 & 3. Expand L-shape and remove red
    for color, l_shape in l_colors:
          orientation, corner = l_shape
          start_row, start_col = corner

          if orientation == 'down_right' or orientation == 'up_left':
              for i in range(5):
                  for j in range(5):
                      row = start_row - 4 + i + j
                      col = start_col + 4 - i - 3 + j
                      if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i >= 2 and j >= 2):
                          output_grid[row, col] = color

          elif orientation == 'up_right' or orientation == 'down_left':
              for i in range(5):
                  for j in range(5):
                      row = start_row + i - j
                      col = start_col + i + j - 1
                      if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i < 3 and j < 3):
                          output_grid[row, col] = color
    return output_grid
```
