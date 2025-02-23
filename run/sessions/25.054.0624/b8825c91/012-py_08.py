"""
Identifies and removes "surrounded" yellow (color 4) shapes from a grid. A yellow shape is considered "surrounded" if all its pixels have neighbors (up, down, left, right) that are either non-yellow or are outside the grid boundaries.
"""

import numpy as np

def get_contiguous_shapes(grid, color):
    """
    Finds and returns a set of coordinates for contiguous shapes of the given color.
    """
    visited = set()
    shapes = []

    def dfs(row, col):
        """Depth-first search to find contiguous pixels."""
        if (row, col) in visited or not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != color:
            return []

        visited.add((row, col))
        shape = [(row, col)]

        # Explore adjacent cells
        shape.extend(dfs(row + 1, col))
        shape.extend(dfs(row - 1, col))
        shape.extend(dfs(row, col + 1))
        shape.extend(dfs(row, col - 1))

        return shape

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == color and (row, col) not in visited:
                shapes.append(dfs(row, col))

    return shapes

def is_surrounded(grid, shape):
    """
    Checks if a shape is surrounded by non-yellow pixels or grid boundaries.
    """
    rows, cols = grid.shape
    for r, c in shape:
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr, nc] == 4:
                    return False  # Found a yellow neighbor, so not surrounded
            # else: it is a valid boundary, implicitly not 4.
        
    return True # No yellow neighbors, so it is surrounded.

def transform(input_grid):
    """
    Removes the surrounded contiguous shapes of yellow (4) pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify Yellow Shapes
    yellow_shapes = get_contiguous_shapes(input_grid, 4)

    # 2. Determine Surrounded Shapes
    surrounded_shapes = [shape for shape in yellow_shapes if is_surrounded(input_grid, shape)]

    # 3. Remove Surrounded Shapes: Iterate through surrounded shapes
    for shape in surrounded_shapes:
        for row, col in shape:
            output_grid[row,col] = input_grid[row,col] # Keep colors the same, as described in program.
    return output_grid