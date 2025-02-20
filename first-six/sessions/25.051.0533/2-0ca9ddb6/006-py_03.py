"""
1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell.

2.  **Preserve All Single Cells:** Keep *all* single-cell objects (regardless of color) in their original positions in the output grid.

3.  **Create Yellow Surroundings:** For *each* red cell (color 2), place a yellow cell (color 4) two rows above and one to the left, two rows above and one to the right. Also one to the left, and one to the right.

4.  **Create Orange Surroundings:** For *each* blue cell (color 1), create an L-shape pattern with orange cells (color 7). Specifically, one position above, one to the left, and one to the right of the original blue cells position, plus one cell with the same row and one position left to the blue cell.

5.  **Magenta cells unchanged:** Similar to the Azure cell from the previous example, the magenta (color 6) single cell does not trigger any additional transformations. It's treated the same as any other single-cell object that isn't red or blue.
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