"""
Removes the contiguous shapes of color value 4 (yellow) and 1(blue) from the input grid.
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

def transform(input_grid):
    """
    Removes the contiguous shapes of yellow (4) and blue(1) pixels by changing their color to the same color of the other pixels.
    """
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Find the yellow and blue shapes
    yellow_shapes = get_contiguous_shapes(input_grid, 4)
    blue_shapes = get_contiguous_shapes(input_grid,1)

    # Combine all shapes to remove into a single list
    shapes_to_remove = yellow_shapes + blue_shapes

    # Remove the identified shapes by setting colors to their surroundings
    for shape in shapes_to_remove:
         for row, col in shape:
            output_grid[row,col] = input_grid[row,col] # Keep original pixel color.

    return output_grid