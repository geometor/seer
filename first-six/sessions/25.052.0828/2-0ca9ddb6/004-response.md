# 2-0ca9ddb6 • 004 • refine_code - CODE

---
```python
"""
The transformation is a "decoration" rule focused on the red and blue cells present in the input grid.  The red cell is preserved, and a yellow cross is constructed *centered* on the red cell.  The blue cell is also preserved, and orange cells are placed adjacent to it in the four cardinal (North, South, East, West) directions.

1. **Identify Key Cells:** Locate the positions of the single red cell (color code 2) and the single blue cell (color code 1) in the input grid.

2. **Preserve Key Cells:**  Copy the red and blue cells from the input grid to the output grid at their original positions.

3. **Construct Yellow Cross:** Centered on the red cell's location, place yellow cells (color code 4) one cell away in each of the four cardinal directions (up, down, left, and right).  The red cell itself remains unchanged.

4. **Surround Blue Cell:**  For the blue cell, place orange cells (color code 7) one cell away in each of the four cardinal directions. If a cell is out of bounds, do not place it. The blue cell is unchanged.
"""

import numpy as np

def find_object(grid, color):
    # Find the coordinates of a single-cell object of the specified color.
    coords = np.where(grid == color)
    if len(coords[0]) > 0:
        return (coords[0][0], coords[1][0])  # Return the first occurrence
    return None

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find the red (2) and blue (1) cells
    red_pos = find_object(input_grid, 2)
    blue_pos = find_object(input_grid, 1)

    # Create the yellow cross around the red cell
    if red_pos:
        y, x = red_pos
        if y > 0:
            output_grid[y-1, x] = 4  # Above
        if y < output_grid.shape[0]-1:
            output_grid[y+1, x] = 4  # Below
        if x > 0:
            output_grid[y, x-1] = 4  # Left
        if x < output_grid.shape[1]-1:
            output_grid[y, x+1] = 4  # Right

    # Surround blue cell with orange cells.
    if blue_pos:
      y,x = blue_pos
      if y > 0:
          output_grid[y-1,x] = 7
      if y < output_grid.shape[0]-1:
          output_grid[y+1,x] = 7
      if x > 0:
          output_grid[y,x-1] = 7
      if x < output_grid.shape[1]-1:
          output_grid[y,x+1] = 7

    return output_grid
```

