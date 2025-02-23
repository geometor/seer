# 9565186b • 008 • example_2 • investigate_coder

---
```python
"""
Transforms a 3x3 input grid to a 3x3 output grid based on color adjacency rules.
Pixels in the top row remain unchanged. Other non-blue pixels are replaced with gray if 
they are horizontally or vertically adjacent to an azure pixel.
"""

import numpy as np

def get_adjacent_pixels(grid, row, col):
    """
    Gets the horizontally and vertically adjacent pixels to a given cell.
    
    Args:
      grid: The 2D numpy array representing the grid.
      row: Row index of the cell.
      col: Column index of the cell.
      
    Returns:
      A list of (row, col) tuples representing adjacent pixels.
    """

    rows, cols = grid.shape
    adjacent = []
    if row > 0:
        adjacent.append((row - 1, col))  # Up
    if row < rows - 1:
        adjacent.append((row + 1, col))  # Down
    if col > 0:
        adjacent.append((row, col - 1))  # Left
    if col < cols - 1:
        adjacent.append((row, col + 1))  # Right
    return adjacent

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Iterate through the grid, skipping the top row
    for row in range(rows):
        for col in range(cols):
            # Preserve top row
            if row == 0:
                continue

            # Check for adjacency to azure (8) for non-blue pixels
            if output_grid[row, col] != 1:
                adjacent_coords = get_adjacent_pixels(output_grid, row, col)
                for adj_row, adj_col in adjacent_coords:
                    if output_grid[adj_row, adj_col] == 8:
                        output_grid[row, col] = 5  # Replace with gray (5)
                        break  # Once replaced, no need to check other neighbors

    return output_grid
```
