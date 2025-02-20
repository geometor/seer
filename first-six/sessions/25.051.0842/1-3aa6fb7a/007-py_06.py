import numpy as np

def find_objects(grid):
    """
    Finds contiguous regions of the same color.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, positions):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        positions.append((row, col))
        dfs(row + 1, col, color, positions)
        dfs(row - 1, col, color, positions)
        dfs(row, col + 1, color, positions)
        dfs(row, col - 1, color, positions)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                color = grid[row, col]
                positions = []
                dfs(row, col, color, positions)
                if positions:
                    objects.append({'color': color, 'positions': positions})
    return objects

def is_2x1_vertical_rectangle(positions):
    """
    Checks if the positions form a 2x1 vertical rectangle.
    """
    if len(positions) != 2:
        return False
    row1, col1 = positions[0]
    row2, col2 = positions[1]
    return (col1 == col2) and (abs(row1 - row2) == 1)

def transform(input_grid):
    """
    Transforms the input grid based on 2x1 azure rectangles.
    """
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    for obj in objects:
        if obj['color'] == 8 and is_2x1_vertical_rectangle(obj['positions']):
            positions = sorted(obj['positions'])  # Ensure top-bottom order
            top_row, top_col = positions[0]
            bottom_row, bottom_col = positions[1]

            # Check space to the right of the top cell
            if top_col + 1 < output_grid.shape[1] and output_grid[top_row, top_col + 1] == 0:
                output_grid[top_row, top_col + 1] = 1
            # Else, check space to the left of the bottom cell
            elif bottom_col - 1 >= 0 and output_grid[bottom_row, bottom_col - 1] == 0:
                output_grid[bottom_row, bottom_col - 1] = 1

    return output_grid