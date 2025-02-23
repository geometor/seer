"""
1.  **Identify Contiguous Green Blocks:** Find all contiguous blocks of green (3) pixels in the input grid. A contiguous block is defined as a group of green pixels where each pixel is directly adjacent (up, down, left, or right, but not diagonally) to at least one other green pixel in the same block.

2.  **Identify Exterior and Interior Pixels:** Within each identified green block, classify each pixel as either exterior or interior.
    *   **Exterior Pixel:** A green pixel that is part of the block, and is adjacent to at least one pixel that is *not* part of the *same* green block (either a different color, or the boundary of the input grid). Adjacency is defined as up, down, left, or right.
    *   **Interior Pixel:** A green pixel where *all* its directly adjacent pixels (up, down, left, and right) are *also* part of the *same* green block.

3.  **Transform Interior Pixels:** Change the color of all identified *interior* green pixels to yellow (4).

4.  **Preserve Other Pixels:** All other pixels in the grid (non-green pixels, and exterior green pixels) remain unchanged.
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

def is_exterior(grid, r, c, block):
    """Checks if a pixel is an exterior pixel of its block."""
    rows, cols = grid.shape
    neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for nr, nc in neighbors:
        if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) not in block:
            return True  # Exterior if any neighbor is outside or not in the block
    return False

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # 1. Identify contiguous blocks of green pixels.
    green_blocks = get_contiguous_blocks(input_grid, 3)

    # 2. & 3. Iterate, classify, and change interior pixels to yellow.
    for block in green_blocks:
        for r, c in block:
            # Check if pixel is exterior. If not, it's interior.
            if not is_exterior(input_grid, r, c, block):
                output_grid[r, c] = 4  # Change interior pixels to yellow

    return output_grid