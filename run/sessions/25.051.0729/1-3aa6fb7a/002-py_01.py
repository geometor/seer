"""
The transformation rule involves the addition of two blue cells (color 1) in specific positions relative to isolated azure cells. One blue cell is placed to the right of the top-isolated azure cell, and the other is placed to the left of the lower-isolated azure cell. The two azure vertical rectangles do not seem to have any influence over the transformation.
"""

import numpy as np

def find_isolated_cells(grid, color):
    """
    Finds isolated cells of a given color in the grid.
    Isolated means that there are no other cells of the same color
    in direct vicinity, horizontally, vertically.

    Args:
    grid (numpy.ndarray): The input grid.
    color (int): The color to look for.

    Returns:
    list: A list of (row, col) tuples of isolated cells.
    """
    isolated_cells = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                # Check neighbors
                is_isolated = True
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == color:
                        is_isolated = False
                        break
                if is_isolated:
                    isolated_cells.append((r, c))
    return isolated_cells

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find isolated azure (color 8) cells
    isolated_azure_cells = find_isolated_cells(input_grid, 8)

    # Sort isolated cells by row to distinguish top and bottom
    isolated_azure_cells.sort()

    # Apply the transformation based on the position of isolated azure cells
    if len(isolated_azure_cells) >= 2:
        # Top isolated azure cell: place blue cell to the right
        top_azure_row, top_azure_col = isolated_azure_cells[0]
        if top_azure_col + 1 < cols:  # Check bounds
            output_grid[top_azure_row, top_azure_col + 1] = 1

        # Bottom isolated azure cell: place blue cell to the left
        bottom_azure_row, bottom_azure_col = isolated_azure_cells[-1]
        if bottom_azure_col - 1 >= 0:  # Check bounds
            output_grid[bottom_azure_row, bottom_azure_col - 1] = 1

    return output_grid