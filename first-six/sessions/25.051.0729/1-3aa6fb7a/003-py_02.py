import numpy as np

def find_contiguous_objects(grid, color):
    """
    Finds contiguous objects of a given color in the grid.

    Args:
    grid (numpy.ndarray): The input grid.
    color (int): The color to look for.

    Returns:
    list: A list of lists, where each inner list contains (row, col) tuples
          representing a contiguous object.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        # Check all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(r + dr, c + dc, current_object)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def find_isolated_cells(grid, color):
    """Finds isolated cells of a given color, considering diagonal adjacency."""
    objects = find_contiguous_objects(grid, color)
    isolated_cells = []
    for obj in objects:
        if len(obj) == 1:
            isolated_cells.extend(obj)  # Use extend since obj is a list of tuples
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
    if len(isolated_azure_cells) >= 1:
        # Top isolated azure cell: place blue cell to the right
        top_azure_row, top_azure_col = isolated_azure_cells[0]
        if top_azure_col + 1 < cols:  # Check bounds
            output_grid[top_azure_row, top_azure_col + 1] = 1

    if len(isolated_azure_cells) >= 2:

        # Bottom isolated azure cell: place blue cell to the left
        bottom_azure_row, bottom_azure_col = isolated_azure_cells[-1]
        if bottom_azure_col - 1 >= 0:  # Check bounds
            output_grid[bottom_azure_row, bottom_azure_col - 1] = 1

    return output_grid