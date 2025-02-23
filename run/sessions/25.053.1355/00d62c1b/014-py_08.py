"""
1.  **Identify the Green Shape:** Locate all contiguous blocks of green (3) pixels within the input grid. Combine these into a single green shape.
2.  **Identify the True Perimeter:** Iterate through all pixels within the green shape. A pixel is part of the perimeter if it meets *either* of these conditions:
    *   It is on the edge of the entire grid (top row, bottom row, leftmost column, or rightmost column).
    *   It has at least one direct neighbor (up, down, left, or right – *not* diagonal) that is *not* part of the green shape.
3.  **Modify Interior Pixels:** Iterate through all pixels of the green shape. If a pixel is *not* in the perimeter set, change its color to yellow (4).
4.  **Preserve Other Pixels:** Ensure all other pixels in the grid retain their original colors. The output grid must be the same size as the input grid. The final output grid represents the modified input.
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

def find_true_perimeter(block, rows, cols):
    """
    Finds the true perimeter pixels of a contiguous block, considering only direct neighbors.
    """
    perimeter = set()
    for r, c in block:
        # Check if it's on the edge of the grid
        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
            perimeter.add((r, c))
            continue

        # Check direct neighbors (up, down, left, right)
        is_perimeter = False
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Only direct neighbors
            nr, nc = r + dr, c + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in block:
                is_perimeter = True
                break
        if is_perimeter:
            perimeter.add((r, c))
    return perimeter

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify the Shape (all green blocks)
    green_blocks = find_contiguous_blocks(input_grid, 3)

    # Combine all blocks into one shape
    green_shape = set()
    for block in green_blocks:
      green_shape.update(block)

    # Find the true perimeter of combined shape
    perimeter = find_true_perimeter(green_shape, rows, cols)

    # Modify Interior Pixels
    for r, c in green_shape:
        if (r,c) not in perimeter:
            output_grid[r, c] = 4

    return output_grid