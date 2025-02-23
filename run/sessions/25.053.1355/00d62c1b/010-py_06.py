"""
1.  **Identify the Shape:** Locate the contiguous block of green (3) pixels within the input grid.
2.  **Find Interior Pixel:** Within the identified shape, locate a single green pixel which surrounded by other green pixels.
3.  **Modify Pixel:** Change the color of this interior pixel from green (3) to yellow (4).
4.  **Preserve Remainder:** Copy the input grid data, with the changed pixel, creating the output grid.
"""

import numpy as np

def find_contiguous_blocks(grid, color):
    """
    Finds contiguous blocks of a specified color in a grid.
    Returns a list of sets, where each set contains the coordinates of a contiguous block.
    """
    visited = set()
    blocks = []

    def dfs(r, c, current_block):
        if (r, c) in visited or not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_block.add((r, c))
        dfs(r + 1, c, current_block)
        dfs(r - 1, c, current_block)
        dfs(r, c + 1, current_block)
        dfs(r, c - 1, current_block)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if (r, c) not in visited and grid[r, c] == color:
                current_block = set()
                dfs(r, c, current_block)
                blocks.append(current_block)
    return blocks

def is_surrounded(grid, r, c, color):
    """
    Checks if a cell at (r, c) is surrounded by cells of the same color.
    """
    rows, cols = grid.shape
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr, nc] != color:
                return False
    return True

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the Shape
    green_blocks = find_contiguous_blocks(input_grid, 3)

    # Find Interior Pixel & Modify
    if green_blocks:  # Ensure there's at least one green block
        for r in range(rows):
            for c in range(cols):
                if output_grid[r,c] == 3 and is_surrounded(output_grid, r, c, 3):
                  output_grid[r,c] = 4
                  return output_grid

    return output_grid