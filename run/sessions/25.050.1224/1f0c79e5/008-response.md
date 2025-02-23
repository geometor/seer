# 1f0c79e5 • 008 • example_4 - CODE

---
```python
"""
The transformation rule can be summarized as follows:

1. Identify single-cell objects (any color).
2. Identify L-shaped objects (any color, 3 contiguous pixels forming an "L").
3. If an L-shape and a single cell of different colors coexist:
   - Remove the L-shaped object.
   - Expand the single-cell object into a partial tilted 5x5 square.
4. The expansion direction of the square depends on relative position between single-cell and the "corner" of the L-shape:
      * cell has row major than corner row and col major than corner col: expand down-right, top-left 3x3 sub-square is missing.
      * cell has row major than corner row and col minor than corner col: expand down-left, top-right 3x3 sub-square is missing.
      * cell has row minor than corner row and col major than corner col: expand up-right, bottom-left 3x3 sub-square is missing.
      * cell has row minor than corner row and col minor than corner col: expand up-left, bottom-right 3x3 sub-square is missing.
    If the single-cell has same row or same col of corner, we assume same expansion direction of cases where row or col are major.
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

def get_expansion_direction(l_corner, cell_coord):
    """Determines the expansion direction based on L-shape corner and single cell position."""
    row_c, col_c = l_corner
    row_s, col_s = cell_coord
    
    # Determine expansion direction
    if row_s > row_c and col_s > col_c:
      return 'down_right'
    elif row_s > row_c and col_s < col_c:
      return 'down_left'
    elif row_s < row_c and col_s > col_c:
      return 'up_right'
    elif row_s < row_c and col_s < col_c:
      return 'up_left'
    else:
      # same row or col
      if row_s == row_c:
        if col_s > col_c: return 'down_right' # same row, col maj
        else: return 'up_left' # same row, col min
      else:
        if row_s > row_c: return 'down_right' # col is the same, row maj
        else: return 'up_left' # col is the same, row min

def transform(input_grid):
    """Transforms the input grid according to the final rule."""
    output_grid = np.zeros_like(input_grid)

    # 1. Identify Objects and their properties
    single_cells = []
    l_shapes = []
    for color in range(10):
      coords = find_object(input_grid, color)
      
      # Single cell
      if len(coords) == 1:
        single_cells.append((color,coords[0]))
      
      # L shape
      l_shape = detect_l_shape(coords)
      if l_shape is not None:
        l_shapes.append((color, l_shape))

    # 2 & 3. Expand Single cell based on L position and remove L
    for color_cell, cell in single_cells:
        for color_l, l_shape in l_shapes:
            if color_cell != color_l:
              orientation, corner = l_shape
              expansion_dir = get_expansion_direction(corner, cell)
              start_row, start_col = cell

              if expansion_dir == 'down_right':
                  for i in range(5):
                      for j in range(5):
                          row = start_row + i - j
                          col = start_col + i + j - 1
                          if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i < 3 and j < 3):
                              output_grid[row, col] = color_cell

              elif expansion_dir == 'down_left':
                  for i in range(5):
                      for j in range(5):
                          row = start_row + i + j -3
                          col = start_col - i + j -1
                          if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i >= 2 and j < 3):
                              output_grid[row, col] = color_cell
              
              elif expansion_dir == 'up_right':
                  for i in range(5):
                      for j in range(5):
                          row = start_row - i - j + 1
                          col = start_col + i - j - 1
                          if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i < 3 and j >= 2):
                              output_grid[row, col] = color_cell

              elif expansion_dir == 'up_left':
                  for i in range(5):
                      for j in range(5):
                          row = start_row - 4 + i + j
                          col = start_col + 4 - i - 3 + j
                          if 0 <= row < output_grid.shape[0] and 0 <= col < output_grid.shape[1] and not(i >= 2 and j >= 2):
                              output_grid[row, col] = color_cell

    return output_grid
```

