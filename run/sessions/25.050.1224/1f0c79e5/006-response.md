# 1f0c79e5 • 006 • example_3 - CODE

---
```python
"""
The transformation rule can be summarized as follows:

1. Identify the L-shaped object (any color).
2. Identify the single red objects.
3. Remove the red cells.
4. Expand the L-shaped object into a tilted 5x5 square:
   - Determine the "corner" of the L-shape.
   - Based on relative position of the red cells, expand as follow:
    - If the red cells are placed to have both a cell with same row of a pixel of the L and a cell with same col of a pixel of the L, the L expands into a tilted, partial 5x5 square as follow:
      * red cells contains a cell with row major than corner row and col major than corner col: expand down-right, top-left 3x3 sub-square is missing.
      * red cells contains a cell with row major than corner row and col minor than corner col: expand down-left, top-right 3x3 sub-square is missing.
      * red cells contains a cell with row minor than corner row and col major than corner col: expand up-right, bottom-left 3x3 sub-square is missing.
      * red cells contains a cell with row minor than corner row and col minor than corner col: expand up-left, bottom-right 3x3 sub-square is missing.

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

def get_expansion_direction(l_corner, red_coords):
    """Determines the expansion direction based on L-shape corner and red cells positions."""
    row_c, col_c = l_corner
    
    # Check existence and relative position of red cells
    row_major = False
    row_minor = False
    col_major = False
    col_minor = False
    for r_coord in red_coords:
      row_r, col_r = r_coord
      row_major = row_major or row_r > row_c
      row_minor = row_minor or row_r < row_c
      col_major = col_major or col_r > col_c
      col_minor = col_minor or col_r < col_c
    
    # Determine expansion direction
    if row_major and col_major:
      return 'down_right'
    elif row_major and col_minor:
      return 'down_left'
    elif row_minor and col_major:
      return 'up_right'
    elif row_minor and col_minor:
      return 'up_left'
    else: return None

def transform(input_grid):
    """Transforms the input grid according to the final rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Objects and their properties
    l_colors = []
    for color in range(10):  # Check all possible colors
        l_coords = find_object(input_grid, color)
        l_shape = detect_l_shape(l_coords)
        if l_shape is not None:
            l_colors.append((color, l_shape))

    red_coords = find_object(input_grid, 2)

    # 2 & 3. Expand L-shape based on red position and remove red
    for color, l_shape in l_colors:
        orientation, corner = l_shape
        expansion_dir = get_expansion_direction(corner, red_coords)
        start_row, start_col = corner

        if expansion_dir == 'down_right':
            for i in range(5):
                for j in range(5):
                    row = start_row + i - j
                    col = start_col + i + j - 1
                    if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i < 3 and j < 3):
                        output_grid[row, col] = color

        elif expansion_dir == 'down_left':
            for i in range(5):
                for j in range(5):
                    row = start_row + i + j -3
                    col = start_col - i + j -1
                    if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i >= 2 and j < 3):
                        output_grid[row, col] = color
        
        elif expansion_dir == 'up_right':
            for i in range(5):
                for j in range(5):
                    row = start_row - i - j + 1
                    col = start_col + i - j - 1
                    if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i < 3 and j >= 2):
                        output_grid[row, col] = color

        elif expansion_dir == 'up_left':
            for i in range(5):
                for j in range(5):
                    row = start_row - 4 + i + j
                    col = start_col + 4 - i - 3 + j
                    if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i >= 2 and j >= 2):
                        output_grid[row, col] = color

    return output_grid
```

