# 2-0ca9ddb6 • 004 • example_2 - CODE

---
```python
"""
1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell.

2.  **Preserve All Single Cells:** Keep all single-cell objects (regardless of color) in their original positions in the output grid.

3.  **Create Yellow Surroundings:** For *each* red cell (color 2), create yellow cells (color 4) two rows above and one column to the left, and two rows above and one column to the right. Also, one cell to the left and one to the right.

4.  **Create Orange Surroundings:** For *each* blue cell (color 1), create an L-shape pattern with orange cells (color 7) around it. Specifically one position above, one position down, one position to the left and one to the right of the corner of the L. The corner cell of the L is the cell with the same coordinates as the original blue cell.

5. **Azure cells unchanged**: The azure cell (color 8) at (0,3) is unchanged, it is an object that should not generate a transformation.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find coordinates of all cells that form single-cell objects.
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if is_single_cell(grid, r, c):
                objects.append((r, c, grid[r, c]))
    return objects

def is_single_cell(grid, r, c):
    # Check if the cell at (r, c) is a single-cell object.
    rows, cols = grid.shape
    color = grid[r, c]

    # Check neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
                return False  # Has a neighbor of the same color
    return True

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find single-cell objects
    single_cells = find_single_cell_objects(input_grid)

    for r, c, color in single_cells:
        if color == 2:  # Red cell
            # Create yellow surroundings
            if r - 2 >= 0 and c - 1 >= 0:
              output_grid[r - 2, c - 1] = 4
            if r - 2 >= 0 and c + 1 < output_grid.shape[1]:
              output_grid[r - 2, c + 1] = 4
            if c - 1 >= 0:
              output_grid[r, c-1] = 4
            if c+1 < output_grid.shape[1]:
              output_grid[r, c+1] = 4

        elif color == 1:  # Blue cell
            # Create orange surroundings (L-shape)
            if r-1 >= 0:
              output_grid[r-1, c] = 7
            if r < output_grid.shape[0]:
              output_grid[r , c-1] = 7
            if r-1 >= 0 and c - 1 >= 0:
              output_grid[r-1, c-1] = 7
            if r - 1 >= 0 and c + 1 < output_grid.shape[1]:
              output_grid[r-1, c + 1] = 7


    return output_grid
```

