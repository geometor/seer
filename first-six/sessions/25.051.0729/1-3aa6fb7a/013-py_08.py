"""
Transforms the input grid by placing blue cells (color 1) near isolated azure cells (color 8).
The topmost isolated azure cell gets a blue cell to its right, and all other isolated azure cells get a blue cell to their left.
"""

import numpy as np

def find_isolated_cells(grid, color):
    """Finds isolated cells of a given color, considering diagonal adjacency."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    isolated_cells = []

    def flood_fill(r, c):
        """Performs a flood fill to find connected components."""
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            visited[r, c] or grid[r, c] != color):
            return []

        visited[r, c] = True
        component = [(r, c)]

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                component.extend(flood_fill(r + dr, c + dc))
        return component

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                component = flood_fill(r, c)
                if len(component) == 1:
                    isolated_cells.append(component[0])
    return isolated_cells

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find isolated azure (color 8) cells
    isolated_azure_cells = find_isolated_cells(input_grid, 8)

    # Sort isolated cells by row, then column
    isolated_azure_cells.sort()

    # Apply the transformation based on the position of isolated azure cells
    if isolated_azure_cells:
        # Top isolated azure cell: place blue cell to the right
        top_azure_row, top_azure_col = isolated_azure_cells[0]
        if top_azure_col + 1 < cols:  # Check bounds
            output_grid[top_azure_row, top_azure_col + 1] = 1 # Place blue cell

        # All other isolated azure cells: place blue cell to the left
        for i in range(1, len(isolated_azure_cells)):
            azure_row, azure_col = isolated_azure_cells[i]
            if azure_col - 1 >= 0:  # Check bounds
                output_grid[azure_row, azure_col - 1] = 1 # Place blue cell

    return output_grid