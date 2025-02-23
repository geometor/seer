"""
The transformation identifies single-cell objects in the input, retains them and creates a cross pattern from adjacent cells around them in the output using distinct colors for different objects of the input.
The exception is the single-cell object of color 6, that remains unchanged.
"""

import numpy as np

def find_single_cell_objects(grid):
    # Find single-cell objects and their positions
    objects = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                # Check if it's a single-cell object
                is_single = True
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if (dr != 0 or dc != 0) and 0 <= r + dr < rows and 0 <= c + dc < cols:
                            if grid[r + dr, c + dc] == grid[r, c]:
                                is_single = False
                                break
                    if not is_single:
                        break
                if is_single:
                    objects.append((grid[r, c], (r, c)))
    return objects

def draw_cross(grid, position, color):
    # Draw a cross pattern around the given position with specified color.
    r, c = position
    rows, cols = grid.shape
    # Define cross positions: up, down, left, right
    cross_positions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for cross_pos in cross_positions:
      cr, cc = cross_pos
      if 0 <= cr < rows and 0 <= cc < cols:
          grid[cr, cc] = color

    return grid


def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)

    # Find single-cell objects
    single_cell_objects = find_single_cell_objects(input_grid)

    # Draw cross for each single cell object based on the color of input cell
    for color, pos in single_cell_objects:
        if color == 2:  # Red cell
            output_grid = draw_cross(output_grid, pos, 4)  # Yellow cross
        elif color == 1:  # Blue cell
            output_grid = draw_cross(output_grid, pos, 7)  # Orange cross
        # Color 6 remains unchanged

    return output_grid