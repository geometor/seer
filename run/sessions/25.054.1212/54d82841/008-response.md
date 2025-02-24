# 54d82841 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify Input Objects:** Locate all cells in the input grid that are green (value 3).
2.  **Calculate Centroid:**
    *   Sum the row indices of all green cells.
    *   Sum the column indices of all green cells.
    *   Divide each sum by the number of green cells. If it is float use floor division.
3.  **Place Output Object:** In the output grid, change the cell at the calculated (row, column) coordinates to yellow (value 4).
4.  **Preserve Unchanged:** All other cells in the input grid remain unchanged in the output grid.
"""

import numpy as np

def find_green_cells(grid):
    # Find coordinates of green cells (value 3).
    green_cells = []
    for row_index, row in enumerate(grid):
        for col_index, cell_value in enumerate(row):
            if cell_value == 3:
                green_cells.append((row_index, col_index))
    return green_cells

def calculate_centroid(coords):
    # Calculate the centroid of a list of coordinates.
    if not coords:
        return None  # Handle the case where there are no green cells.

    sum_row = sum(coord[0] for coord in coords)
    sum_col = sum(coord[1] for coord in coords)
    centroid_row = sum_row // len(coords)
    centroid_col = sum_col // len(coords)
    return (centroid_row, centroid_col)

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    
    # find green cells
    green_cells = find_green_cells(input_grid)

    # calculate the centroid location
    centroid = calculate_centroid(green_cells)

    # if a centroid exists, set the color to yellow
    if centroid:
      output_grid[centroid[0], centroid[1]] = 4

    return output_grid
```
