"""
Identifies contiguous green regions in a grid and changes the color of green
pixels to yellow if they are on the bottom or right side of a horizontal or
vertical green segment.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """Gets the cardinal neighbors of a given cell."""
    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))  # Up
    if r < rows - 1:
        neighbors.append((r + 1, c))  # Down
    if c > 0:
        neighbors.append((r, c - 1))  # Left
    if c < cols - 1:
        neighbors.append((r, c + 1))  # Right
    return neighbors

def is_right_edge(grid, r, c, green_region):
    """Checks if a green pixel is a right edge."""
    rows, cols = grid.shape
    if c == cols - 1:
        return True  # Right edge of the grid
    if (r, c + 1) not in green_region:
      return True
    return False

def is_bottom_edge(grid, r, c, green_region):
    """Checks if a green pixel is a bottom edge."""
    rows, cols = grid.shape
    if r == rows - 1:
        return True # Bottom edge
    if (r + 1, c) not in green_region:
        return True
    return False


def transform(input_grid):
    """
    Transforms the input grid according to the observed rule.

    Args:
        input_grid (list of lists): The input grid of pixel values.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    visited = set()

    # Iterate through each pixel
    for r in range(rows):
        for c in range(cols):
            # Process only green pixels that haven't been visited
            if input_grid[r, c] == 3 and (r, c) not in visited:
                green_region = set()
                queue = [(r, c)]
                visited.add((r, c))

                # Find contiguous green region using BFS
                while queue:
                    curr_r, curr_c = queue.pop(0)
                    green_region.add((curr_r, curr_c))

                    for nr, nc in get_neighbors(input_grid, curr_r, curr_c):
                        if input_grid[nr, nc] == 3 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

                # Iterate through identified green region
                for gr, gc in green_region:
                    if is_right_edge(input_grid, gr, gc, green_region) or is_bottom_edge(input_grid, gr, gc, green_region):
                        output_grid[gr, gc] = 4

    return output_grid.tolist()