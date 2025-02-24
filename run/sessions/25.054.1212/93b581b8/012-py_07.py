"""
Transforms the input grid by identifying a 2x2 core cluster of four unique,
non-zero colored pixels. It mirrors this cluster horizontally and vertically,
placing the mirrored clusters relative to the original cluster's position.
The output grid combines the original cluster and its mirrored copies,
maintaining the original input grid size.
"""

import numpy as np

def find_core_cluster(grid):
    """Finds the 2x2 core cluster with four unique non-zero colors."""
    rows, cols = grid.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            colors = [grid[r, c], grid[r + 1, c], grid[r, c + 1], grid[r + 1, c + 1]]
            if all(color != 0 for color in colors) and len(set(colors)) == 4:
                return r, c, colors
    return None, None, None

def horizontal_mirror(grid, core_row, core_col, colors):
    """Mirrors the core cluster horizontally, two rows above or below."""
    rows, cols = grid.shape
    # Try above
    new_row = core_row - 2
    if new_row >= 0:
        grid[new_row, core_col:core_col+2] = [colors[2], colors[3]]
        grid[new_row+1, core_col:core_col+2] = [colors[0], colors[1]]
    else: #try below
        new_row = core_row + 2
        if new_row < rows -1:
          grid[new_row, core_col:core_col+2] = [colors[2], colors[3]]
          grid[new_row+1, core_col:core_col+2] = [colors[0], colors[1]]

    return grid

def vertical_mirror(grid, core_row, core_col, colors):
    """Mirrors the core cluster vertically, two columns to the right or left."""
    rows, cols = grid.shape
    # Try right
    new_col = core_col + 2
    if new_col <= cols - 2:
        grid[core_row: core_row+2, new_col] = [colors[1], colors[0]]
        grid[core_row: core_row+2, new_col+1] = [colors[3], colors[2]]
    else:  #try left
        new_col = core_col-2
        if new_col >= 0:
          grid[core_row: core_row+2, new_col] = [colors[1], colors[0]]
          grid[core_row: core_row+2, new_col+1] = [colors[3], colors[2]]

    return grid

def transform(input_grid):
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find the core cluster
    core_row, core_col, colors = find_core_cluster(input_grid)

    if core_row is None:
        return output_grid

    # Apply horizontal mirroring
    output_grid = horizontal_mirror(output_grid, core_row, core_col, colors)

    # Apply vertical mirroring
    output_grid = vertical_mirror(output_grid, core_row, core_col, colors)

    return output_grid