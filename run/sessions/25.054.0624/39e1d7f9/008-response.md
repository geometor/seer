# 39e1d7f9 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Objects:** Locate the 3x3 yellow square, and the two 3x3 magenta squares. Also observe the regular pattern of green (3) and white(0) that seems to be a background that remains largely fixed except some green becomes magenta in the area around the magenta squares and some green becomes yellow in the area around the yellow square.

2.  **Determine Shift:** Find the first magenta square in the input.
The top magenta square is moved to the location of first magenta square on first row, and the second one is moved to the location of second magenta square on the first row.

3.  **Apply Shift:** Move the top-left-most magenta square so it aligns with the location of the top-left-most magenta square in the input.

4. Move the bottom right magenta sqaure to the first row.

5.  The yellow square does not seem to get re-located in the input.

"""

import numpy as np

def find_object(grid, color, shape=(3, 3)):
    """Finds the top-left corner coordinates of an object with a given color and shape."""
    rows, cols = grid.shape
    for i in range(rows - shape[0] + 1):
        for j in range(cols - shape[1] + 1):
            if np.all(grid[i:i+shape[0], j:j+shape[1]] == color):
                return (i, j)
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # Find objects
    magenta_squares = []
    rows, cols = input_grid.shape
    for r in range(rows - 2):
        for c in range(cols - 2):
            if np.all(input_grid[r:r+3, c:c+3] == 6):
                magenta_squares.append((r, c))
    yellow_square = find_object(input_grid, 4)

    # Find first row magenta square locations
    first_row_magenta_locations = []

    rows, cols = input_grid.shape
    for c in range(cols-2):
        if np.all(input_grid[0:3, c:c+3] == 6):
           first_row_magenta_locations.append((0,c))
    
    if len(magenta_squares) >= 2 and len(first_row_magenta_locations) >=2 :
    
      # Move the first magenta square
      output_grid[first_row_magenta_locations[0][0]:first_row_magenta_locations[0][0]+3, first_row_magenta_locations[0][1]:first_row_magenta_locations[0][1]+3] = 6
      
      #clear original location of first square
      output_grid[magenta_squares[0][0]:magenta_squares[0][0]+3, magenta_squares[0][1]:magenta_squares[0][1]+3] = input_grid[magenta_squares[0][0]:magenta_squares[0][0]+3, magenta_squares[0][1]:magenta_squares[0][1]+3]
    
    
      # Move the second magenta square
      output_grid[first_row_magenta_locations[1][0]:first_row_magenta_locations[1][0]+3, first_row_magenta_locations[1][1]:first_row_magenta_locations[1][1]+3] = 6

      #clear original location of second square
      output_grid[magenta_squares[1][0]:magenta_squares[1][0]+3, magenta_squares[1][1]:magenta_squares[1][1]+3] = input_grid[magenta_squares[1][0]:magenta_squares[1][0]+3, magenta_squares[1][1]:magenta_squares[1][1]+3]

    return output_grid
```
