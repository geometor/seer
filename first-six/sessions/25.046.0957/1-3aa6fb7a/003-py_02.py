"""
The transformation identifies distinct "L"-shaped objects formed by azure (color 8) pixels.
For each azure 'L' shape, the transformation finds the azure pixel which is closest to the top-left,
relative to the other pixels in that object. It places a blue pixel immediately to the *right* of that pixel.
"""

import numpy as np

def find_top_left_azure(grid, azure_positions):
    """Finds the top-leftmost azure pixel within a connected component."""
    min_row = grid.shape[0]
    min_col = grid.shape[1]

    for r, c in azure_positions:
        if r < min_row:
            min_row = r
            min_col = c
        elif r == min_row and c < min_col:
            min_col = c
    return (min_row, min_col)

def get_connected_components(grid, color):
    """
    Finds connected components of a given color in the grid.
    Uses a simple flood-fill algorithm.
    """
    visited = set()
    components = []

    def dfs(row, col, current_component):
      
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return

        visited.add((row, col))
        current_component.append((row, col))

        dfs(row + 1, col, current_component)
        dfs(row - 1, col, current_component)
        dfs(row, col + 1, current_component)
        dfs(row, col - 1, current_component)


    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == color and (row, col) not in visited:
                current_component = []
                dfs(row, col, current_component)
                components.append(current_component)

    return components

def transform(input_grid):
    """Transforms the input grid according to the rule."""

    grid = np.array(input_grid)
    output_grid = np.copy(grid)
    
    azure_components = get_connected_components(grid, 8)
    
    for component in azure_components:
      top_left_azure = find_top_left_azure(grid, component)
      
      # Place blue pixel to the right
      blue_row = top_left_azure[0]
      blue_col = top_left_azure[1] + 1

      # Check bounds
      if 0 <= blue_row < grid.shape[0] and 0 <= blue_col < grid.shape[1]:
          output_grid[blue_row, blue_col] = 1

    return output_grid.tolist()  # Convert back to list for comparison


if __name__ == '__main__':

    input = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    output = transform(input)

    if output == expected_output:
        print("SUCCESS!\n")
    else:
        print("FAILED!\n")
        print("Expected Output:", expected_output)
        print("Transformed Output:", output)

    print()
    assert output == expected_output, "Transformed output does not match expected output."