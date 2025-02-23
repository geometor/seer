import numpy as np

def find_objects(grid, color):
    """
    Finds contiguous regions of the specified color in the grid.
    Returns a list of (row, col) tuples representing the object's pixels.
    """
    objects = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []

        visited.add((row, col))
        region = [(row, col)]

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            region.extend(dfs(row + dr, col + dc))
        
        return region

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                objects.append(dfs(r, c))

    return objects

def transform(input_grid):
    """
    Transforms the input grid according to the refined rule.
    """
    output_grid = np.copy(input_grid)
    gray_objects = find_objects(input_grid, 5)

    for obj in gray_objects:
        # Create a dictionary to store the rightmost column index for each row within the object
        rightmost_cols = {}
        for r, c in obj:
            if r in [0, 1, 3, 4]:
                if r not in rightmost_cols:
                    rightmost_cols[r] = c
                else:
                    rightmost_cols[r] = max(rightmost_cols[r], c)

        # Recolor based on rightmost position on specified rows
        for r, c in obj:
            if r in rightmost_cols and c == rightmost_cols[r]:
                output_grid[r, c] = 8
            elif output_grid[r,c] == 5:
                output_grid[r, c] = 2

    return output_grid