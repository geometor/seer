"""
1.  **Identify Single-Cell Objects:** Locate all objects in the input grid that consist of a single cell. In this case, we have a red cell (color 2) at (3, 2) and a blue cell (color 1) at (6, 6).

2.  **Create Yellow Surroundings:** For the red cell, we will create two yellow cells, one two rows above and one column to the left. The same two rows above and one column to the right.
    
3.  **Create Orange Surroundings:** For the blue cell, create an L shape with orange color surrounding the identified blue cell. It is placed one row above.
    The corner of the L shape is in (6,6).

4.  **Preserve Original Cells:** Keep the original red and blue single-cell objects in their original positions.
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
            output_grid[r - 2, c - 1] = 4
            output_grid[r - 2, c + 1] = 4
            output_grid[r, c-1] = 4
            output_grid[r, c+1] = 4

        elif color == 1:  # Blue cell
            # Create orange surroundings (L-shape)
            output_grid[r-1, c] = 7
            output_grid[r , c-1] = 7
            output_grid[r-1, c-1] = 7
            output_grid[r-1, c + 1] = 7


    return output_grid