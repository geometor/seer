"""
1.  **Identify** all contiguous blocks of green (3) pixels in the input grid.  A contiguous block is a set of green pixels where each pixel is directly adjacent (up, down, left, or right) to at least one other pixel in the same block.

2.  **Identify** the exterior and interior pixels within each green block:
    *   An **exterior** green pixel is part of the block and is adjacent to at least one pixel that is *not* part of the same green block (either a different color or the boundary of the grid).
    *   An **interior** green pixel is part of the block, and all of its directly adjacent pixels (up, down, left, and right) are *also* part of the same green block.

3.  **Change** all interior green pixels within each block to yellow (4).

4.  All other pixels in the grid remain **unchanged**.
"""

import numpy as np

def get_contiguous_blocks(grid, color):
    """Finds contiguous blocks of a given color in the grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    blocks = []

    def dfs(r, c, current_block):
        """Depth-first search to find contiguous pixels."""
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_block.append((r, c))
        dfs(r + 1, c, current_block)
        dfs(r - 1, c, current_block)
        dfs(r, c + 1, current_block)
        dfs(r, c - 1, current_block)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_block = []
                dfs(r, c, current_block)
                blocks.append(current_block)
    return blocks

def is_interior(grid, r, c, block):
    """Checks if a pixel is an interior pixel of its block."""
    rows, cols = grid.shape
    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for nr, nc in neighbors:
        if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in block:
            return False  # Not interior if any neighbor is outside the grid or not in the block
    return True

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify contiguous blocks of green pixels.
    green_blocks = get_contiguous_blocks(input_grid, 3)

    # 2. & 3. Iterate through blocks and change interior pixels to yellow.
    for block in green_blocks:
        for r, c in block:
            # Check if the current pixel is an interior pixel
            if is_interior(input_grid, r, c, block):
                output_grid[r, c] = 4

    return output_grid